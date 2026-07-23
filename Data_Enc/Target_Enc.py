#caategory_encoders
import pandas as pd
import category_encoders as ce

df = pd.DataFrame({"City": ["Guwahati", "Tripura", "Sikkim", "Goa"], 
                   "Pincode": [4.2, 3.5, 3, 3]})

encoder = ce.TargetEncoder(cols=["City"])
df1 = encoder.fit_transform(df["City"], df["Pincode"])
print("Referenced data:\n",df)
print(df1)