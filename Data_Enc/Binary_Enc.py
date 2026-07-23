import numpy as np
import pandas as pd
import category_encoders as ce

data = ["red", "green", "blue", "yellow", "red"]
encoder = ce.BinaryEncoder(cols=["Color"])
encoded_data = encoder.fit_transform(pd.DataFrame(data, columns=["Color"]))

print(encoded_data)