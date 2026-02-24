import pandas as pd
#read data from csv file 
df = pd.read_csv("emp.csv")

#show the rows
print("First 5 rows:")
print(df.head())

#select specific coloumns

print("\n Names and Departments:")
print(df[["Name","Department"]])

#filter employees with salasry above 50000

high_salary =df[df["Salary"]>50000]
print("\n Employees with High Salary:")
print(high_salary)

#group by department and calculate avaerage salary 

avg_salary =df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department")
print(avg_salary)

#sort employees by salary (descending)

sorted_df = df.sort_values(by="Salary",ascending=False)
print("\nEmployees Sorted By Salary")
print(sorted_df)