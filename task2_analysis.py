# Task 2: Hands-On Data Lab Implementation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Sample Data Creation
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Department": ["IT", "HR", "IT", "Marketing", "Finance"],
    "Salary": [65000, 50000, 72000, 58000, 69000],
    "Experience_Years": [3, 2, 5, 4, 4],
}

df = pd.DataFrame(data)

# 2. Data Manipulation & Aggregation
print("Dataset Overview:")
print(df.head())

print("\nDepartment-wise Average Salary:")
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

print("\nStatistical Summary:")
print(df.describe())

# 3. Simple Data Visualization
plt.figure(figsize=(7, 4))
plt.bar(df["Name"], df["Salary"], color="teal", edgecolor="black")
plt.title("Employee Salaries Overview")
plt.xlabel("Employee Name")
plt.ylabel("Salary (INR)")
plt.tight_layout()
plt.savefig("salary_chart.png")
print("\nProcess completed successfully.")
