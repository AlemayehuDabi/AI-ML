# Ex.2: Merge two Datasets and perform Data Transformation - inner merge and adding col called "calculator"

import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "department": ["Sales", "Engineering", "Sales", "HR", "Engineering"],
    "hire_year": [2019, 2018, 2020, 2021, 2017]
})

salaries = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 106],  # 106 is not in employees, 105 is missing here
    "annual_salary": [55000, 90000, 60000, 52000, 95000],
    "performance_score": [85, 92, 78, 70, 88]
})


inner_merge = employees.merge(salaries, how="inner", on='employee_id')
# print("Applied Inner Merge: \n", inner_merge)

inner_merge["calcuator"] = inner_merge["annual_salary"] / inner_merge["performance_score"]
print("Add the col: \n", inner_merge)