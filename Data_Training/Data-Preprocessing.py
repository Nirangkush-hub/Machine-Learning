import numpy as np
import pandas as pd

raw_data = {
    "Employee_ID": [101, 102, 103, 104, 104, 105, 106, 107],
    "Name": [
        "  Alice Smith ",
        "bob Jones",
        "Charlie Brown",
        "David Miller",
        "David Miller",
        "Eva Green",
        "Frank Wright",
        "Grace Lee",
    ],
    "Age": [25, 30, np.nan, 45, 45, 22, 150, 28], 
    "Salary": [
        "50,000",
        "60,000",
        "75,000",
        "90,000",
        "90,000",
        "UNKNOWN",
        "80,000",
        "55,000",
    ],
    "Join_Date": [
        "2021-01-15",
        "2020-05-10",
        "2019-11-23",
        "2018-07-01",
        "2018-07-01",
        "2022/02/14",
        "hello",
        "2021-09-09",
    ],
    "Department": [
        "HR",
        "hr",
        " IT ",
        "IT",
        "IT",
        "Finance",
        "FINANCE",
        "Marketing",
    ],
}

df = pd.DataFrame(raw_data)
print("--- RAW DATA ---")
print(df)

# Check count of duplicate rows
print(f"Duplicate rows: {df.duplicated().sum()}")

# Drop exact duplicate rows
df = df.drop_duplicates().reset_index(drop=True)


df["Name"] = df["Name"].str.strip().str.title()
df["Department"] = df["Department"].str.strip().str.upper()

print(df[["Name", "Department"]])


df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Converting Join_Date to datetime
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

print(df.dtypes)
# Check missing values count per column
print(df.isnull().sum())

# Strategy A: Fill missing Age with median age
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# Strategy B: Fill missing Salary with mean salary
mean_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(mean_salary)

# Strategy C: Drop rows where Join_Date could not be parsed
df = df.dropna(subset=["Join_Date"])


# Detect using IQR(Interquartile Range)
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + (1.5 * IQR)

# Cap outliers to the upper bound or replace with median
df.loc[df["Age"] > 65, "Age"] = df["Age"].median()

print("--- CLEANED DATA ---")
print(df)