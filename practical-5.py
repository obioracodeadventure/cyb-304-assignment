import pandas as pd

#Data cleaning pipeline
data = pd.read_csv("students.csv")
print(data.isnull().sum()) # Check missing
cleaned = data.dropna() # Remove missing
cleaned.to_csv("cleaned.csv", index=False)


data = pd.read_csv("students.csv")

print(data.isnull().sum())  # Check missing values

cleaned = data.dropna()  # Remove missing rows

cleaned.to_csv("cleaned.csv", index=False)