import pandas as pd
print("1. Loading and printing Data with Pandas ")
df = pd.read_csv(r"Bounty.csv")

print("Representing Stored Data")
print(df)

"""Diffrentiating between series and dataframe"""
nam = df["Name"]
print("\nType of 'df'(Original data)\n:",type(df))
print("Type of 'df'(Specific column)\n:",type(nam))
print()
print("Info about the csv file:\n",df.info())
print("\nShowing only first 5 lines: \n",df.head())

print("\nShowing only last 5 lines: \n",df.tail())

print("\n2. Counting Missing Values")

print("Missing values per column:  \n", df.isnull().sum())

print("\n3. Filtering Data")

# Conditional filtering: Get rows where Bounty is greater than 1,000,000
high_values = df[df["Bounty"] > 1000000]
print("High value Bounty rows:")
print(high_values)