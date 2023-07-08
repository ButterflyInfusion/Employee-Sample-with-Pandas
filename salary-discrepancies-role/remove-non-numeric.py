import pandas as pd

#read the csv file
df = pd.read_csv('employee-sample-data.csv', encoding='latin1')

#remove the comma from Annual Salaries column(,)
df['Annual Salary'] = df['Annual Salary'].str.replace(',', '')

#remove dollar sign from the Annual Salaries column($)
df['Annual Salary'] = df['Annual Salary'].str.replace('$', '')

#save the data into csv file
df.to_csv('employee-sample-data.csv', index=False)

#get mean salary grouped by departments
salary_departments = df.groupby('Department')['Annual Salary'].mean()

#print the results
print(salary_departments)

#get role statistics 
role_statistics = grouped_roles.agg({
    'Annual Salary' : ['mean', 'median', 'min', 'max'],
    'Age': ['mean', 'median', 'min', 'max']
})

print(role_statistics)


