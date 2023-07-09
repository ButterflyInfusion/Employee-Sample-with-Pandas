import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('employee-sample-data.csv')

# Group the data by job title
grouped_roles = df.groupby('Job Title')

# Calculate statistics for annual salary and age
role_statistics = grouped_roles.agg({
    'Annual Salary': ['mean', 'median', 'min', 'max'],
    'Age': ['mean', 'median', 'min', 'max']
})

# Define the positions and width for the bars
job_titles = role_statistics.index
positions = list(range(len(job_titles)))
width = 0.35

# Plotting the grouped bar plot
plt.figure(figsize=(12, 6))
plt.bar(positions, role_statistics['Annual Salary']['mean'], width=width, label='Mean Salary')
plt.bar([p + width for p in positions], role_statistics['Annual Salary']['median'], width=width, label='Median Salary')
plt.xlabel('Job Title')
plt.ylabel('Salary')
plt.title('Role-based Salary Discrepancy')
plt.xticks(positions, job_titles, rotation=90)  # Update x-axis ticks to job_titles
plt.legend()
plt.tight_layout()  # Adjust layout for better visibility
plt.show()
