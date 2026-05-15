import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Titanic-Dataset.csv")

# Display first 5 rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age values with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill Embarked missing values with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Rename columns
df.rename(columns={
    'PassengerId': 'Passenger_ID',
    'Survived': 'Survival_Status'
}, inplace=True)

# Check dataset info
print("\nDataset Info:")
print(df.info())

# Save cleaned dataset
df.to_csv("dataset/cleaned_titanic.csv", index=False)

print("\nData cleaning completed successfully!")