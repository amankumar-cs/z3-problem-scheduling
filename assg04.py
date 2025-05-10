from z3 import Solver, Int, If, Or, Optimize, sat

def solve_with_z3(group_size, num_problems, problem_times):
    # Initialize Z3 optimizer
    opt = Optimize()

    # Variables: Each problem is assigned a student and a start time
    student_vars = [Int(f"student_{i}") for i in range(num_problems)]
    start_time_vars = [Int(f"start_time_{i}") for i in range(num_problems)]
    end_time_vars = [Int(f"end_time_{i}") for i in range(num_problems)]

    # Constraints: Assign each problem to one student and calculate end time
    for i in range(num_problems):
        opt.add(student_vars[i] >= 0, student_vars[i] < group_size)  # Student index range
        opt.add(start_time_vars[i] >= 0)  # Start time non-negative
        opt.add(end_time_vars[i] == start_time_vars[i] + problem_times[i])  # End time calculation

    # Ensure no overlap for problems assigned to the same student
    for i in range(num_problems):
        for j in range(i + 1, num_problems):
            opt.add(If(student_vars[i] == student_vars[j],
                       Or(end_time_vars[i] <= start_time_vars[j], end_time_vars[j] <= start_time_vars[i]),
                       True))

    # Objective: Minimize the maximum end time across all students
    min_end_time = Int("min_end_time")
    opt.add([min_end_time >= end_time_vars[i] for i in range(num_problems)])
    opt.minimize(min_end_time)

    # Solve the optimization problem
    if opt.check() == sat:
        model = opt.model()
        return model[min_end_time].as_long()
    else:
        return None

# Example usage
group_size = 3
num_problems = 5
problem_times = [17, 16, 18, 9, 15]
print("Minimum time to solve all problems:", solve_with_z3(group_size, num_problems, problem_times))