# Z3 Problem Scheduling

This project models and solves a parallel scheduling problem using the Z3 SMT solver. It assigns a set of problems to a group of students such that no student works on more than one problem at a time and the overall completion time is minimized.

## 📘 Problem Statement

- You are given:
  - 'M': Number of students
  - 'N': Number of problems
  - A list 'tᵢ' where each value represents the time required to solve problem 'pᵢ'
- Goal: Assign each problem to a student such that:
  - No two problems assigned to the same student overlap in time
  - Total time (maximum end time across all students) is minimized

## 🧠 Solution

- Uses the **Z3 Optimizer**:
  - Models students, problem start times, and end times
  - Adds constraints to prevent overlapping tasks
  - Minimizes the overall time taken

## ⚙️ Requirements

- Python 3.x
- Z3 solver:  
  Install using pip:
  '''bash
  pip install z3-solver

## How to Run
--> Code Examples

from z3 import Solver, Int, If, Or, Optimize, sat

# Problem input
group_size = 3
num_problems = 5
problem_times = {17,16,18,9,15}

# Solve
print("Minimum time to solve all problems:", solve_with_z3(group_size, num_problems, problem_times))

--> Output
Minimum time to solve all problems: 33

# FILES
assg04.py – Contains the core Z3-based scheduling logic and a sample input.

## ✍️ Author

**Aman Kumar**  
MTech in Artificial Intelligence, IIT Patna  
📧 Email: amankumarmfp14@gmail.com

