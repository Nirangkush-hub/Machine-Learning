import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data = [["low"], ["medium"], ["high"], ["low"], ["medium"], ["high"]]

df = OrdinalEncoder(categories=[["low", "medium", "high"]])
ordinal = df.fit_transform(data)
print("The order: LOW<MEDIUM<HIGH")
print("Original dataset:",data)
print(f"Order array data:\n {ordinal}")
