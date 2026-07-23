import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


f = [
    ['Red', 'Green', 'Blue', 'Yellow'], 
    ['Yellow', 'Green', 'Blue', 'Red', 'Blue'], 
    ['Red', 'Blue', 'Blue', 'Yellow', 'Green']
]

df = pd.DataFrame(f)

encoder = pd.get_dummies(df)
print(encoder)