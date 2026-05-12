import pandas as pd

employee_data = {
    'Dept': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'Sales'],
    'Status': ['FT', 'FT', 'Contract', 'FT', 'Contract', 'FT', 'Contract', 'FT'],
    'Salary': [95000, 60000, 70000, 80000, 55000, 98000, 72000, 85000]
}
emp_df = pd.DataFrame(employee_data)
print("Employee Data:\n")
print(emp_df)

grouped_data = emp_df.groupby('Dept')['Salary'].agg(['mean', 'max'])
print("\nAverage and Maximum Salary by Department:\n")
print(grouped_data)

pivot_table = pd.pivot_table(
    emp_df,
    index='Dept',
    columns='Status',
    values='Salary',
    aggfunc='count',
    fill_value=0
)
print("\nPivot Table:\n")
print(pivot_table)

sorted_pivot = pivot_table.sort_values(by='Contract', ascending=False)
print("\nDepartments Sorted by Contract Workers:\n")
print(sorted_pivot)