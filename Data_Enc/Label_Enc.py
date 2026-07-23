#Label encoding
import numpy as np 
import pandas as pd
from sklearn.preprocessing import LabelEncoder

a=['Red-Ball','Green-Ball','Blue-Ball','Blue-Ball','Blue-Ball','Green-Ball']
enc=LabelEncoder()
res=enc.fit_transform(a)
print("ORIGINAL-LIST:  Red-Ball,Green-Ball,Blue-Ball,Blue-Ball,Blue-Ball,Green-Ball\n",res)