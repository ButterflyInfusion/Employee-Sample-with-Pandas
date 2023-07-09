Salary Discrepancies Analysis by Role

In this code, I have analyzed salary discrepancies by role within an organization. The main focus is on the "Annual Salaries" column of the dataset. Here are the steps followed in the analysis:

1. Data Cleaning

Initially, the salaries in the column had the format "$123,456" with non-numeric characters (comma and dollar sign). To clean the data, I removed these non-numeric characters and converted the values to integers since they were stored as strings.

2. Mean Salaries per Department

After data cleaning, the first operation performed was to calculate the mean salaries per department. Here are the findings:

-Accounting has the highest mean annual salary among the departments, with an average of approximately $123,147.

-Engineering and Finance also have relatively high mean annual salaries, averaging around $109,035 and $122,803, respectively.

-Human Resources and Sales have average mean annual salaries of approximately $118,058 and $111,050, respectively.

-IT has a slightly lower mean annual salary compared to the above departments, with an average of approximately $97,790.

-Marketing has the highest mean annual salary among all the departments, with an average of around $129,663.

-The mean salary analysis provides insights into the average compensation levels within different departments.

3. Role-based Salary Discrepancies

To further explore potential salary discrepancies, the analysis focused on role-based comparisons. Here are additional insights obtained from this analysis:

-The role with the highest mean annual salary is "Vice President," with an average salary of approximately $222,195.

-Roles such as "Director," "Manager," and "Sr. Manager" also have relatively high mean annual salaries, ranging from around $113,275 to $171,634.

-Roles like "Account Representative," "Analyst," and "Business Partner" have lower mean annual salaries, ranging from approximately $49,560 to $78,929.

-Some roles, such as "Technical Architect," "IT Systems Architect," and "Cloud Infrastructure Architect," have average salaries in the range of $79,000 to $87,000.

-The minimum and maximum salary values provide an understanding of the salary range within each role.

By performing this analysis, we gain insights into salary distributions and potential inequities within the organization based on job roles. This information can be useful for identifying areas of improvement, ensuring fair compensation practices, and maintaining employee satisfaction and morale.

VISUALISATION

1. Extracting job titles and defining bar plot parameters:

2. We extract the job titles from the index of the role_statistics DataFrame.
Positions and width are defined for the bars in the bar plot.
Creating the grouped bar plot:

We create a figure with the desired size using plt.figure().

Two bar plots are created side by side, representing the mean and median salaries for each job title.
Axes labels, title, and legends are added to the plot.

The x-axis tick labels are updated to display the job titles using plt.xticks().

The layout is adjusted for better visibility using plt.tight_layout().
Saving the plot:

The plot is saved as a PNG file using the savefig() function.
Displaying the plot:

The plot is shown using plt.show().

