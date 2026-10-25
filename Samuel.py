
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a dataset with 5 rows and 5 columns
data = {
    'Student': ['Student A', 'Student B', 'Student C', 'Student D', 'Student E'],
    'Python': [85, 90, 78, 92, 88],
    'Statistics': [80, 85, 90, 75, 95],
    'SQL': [75, 88, 82, 90, 85],
    'Machine_Learning': [90, 80, 85, 88, 92]
}

# Step 2: Convert the data into a DataFrame
df = pd.DataFrame(data)

# Step 3: Display the first five rows and columns
print("First five rows and columns:")
print(df.iloc[:5, :5])

# Step 4: Create a bar chart
df.set_index('Student').plot(kind='bar', figsize=(10, 6))

# Step 5: Add chart labels and title
plt.title('Student Performance by Subject')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.xticks(rotation=0)
plt.legend(title='Subjects')
plt.tight_layout()

# Step 6: Display the chart
plt.show()
