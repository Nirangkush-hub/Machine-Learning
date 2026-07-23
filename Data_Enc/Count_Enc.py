import pandas as pd
data = ["red", "green", "blue", "yellow", "red", "green", "red"]
df = pd.DataFrame(data, columns=["Color"])

counts = df["Color"].value_counts()


df["Color_Count"] = df["Color"].map(counts)

print(df)