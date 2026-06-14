import pandas as pd

# Load the wine quality dataset
df = pd.read_csv("../dataset/WineQT.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Show dataset information
print("\nDataset information:")
print(df.info())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Show quality score distribution
print("\nQuality score distribution:")
print(df["quality"].value_counts())