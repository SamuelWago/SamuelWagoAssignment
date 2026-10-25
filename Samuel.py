
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a dataset with 5 rows and 5 columns
dataset = {
    'Student': ['Samuel', 'Biniam', 'Sosina', 'Firaol', 'Mikiyas'],
    'DS for Surveillance System': [90, 80, 85, 79, 82],
    'Biostatistics': [83, 91, 94, 75, 80],
    'Statistical Computing for DS': [88, 95, 84, 82, 94],
    'DS fundamentals': [95, 87, 75, 90, 92]
}

# Step 2: Converting the data into a DataFrame
df = pd.DataFrame(dataset)

# Step 3: Display the first five rows and columns
print("First five rows and columns:")
print(df.iloc[:5, :5])

# Step 4: Create a bar chart
df.set_index('Student').plot(kind='bar', figsize=(10, 6))

# Step 5: Adding chart labels and title
plt.title('Student Mark by Subject')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.xticks(rotation=0)
plt.legend(title='Subjects')
plt.tight_layout()

# Step 6: Display the chart
plt.show()
