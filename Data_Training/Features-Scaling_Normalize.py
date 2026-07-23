import pandas as pd 
import seaborn as sb

from sklearn.preprocessing import Normalizer
df=sb.load_dataset("tips")
print(df)

scaler=Normalizer()
nor=scaler.fit_transform(df[["total_bill","tip"]])

df1=pd.DataFrame(nor,columns=["Bill_Normalized","Tips_new"])
print(df1)

df2=pd.concat(objs=[df,df1],axis=1)
print(df2[["total_bill","tip","Bill_Normalized","Tips_new"]].head())