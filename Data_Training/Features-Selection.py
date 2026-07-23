import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer

data = load_iris()

x = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)

from sklearn.feature_selection import chi2, SelectKBest

Select_K_best = SelectKBest(score_func=chi2, k=2)

X_train_K_best = Select_K_best.fit_transform(x_train, y_train)

print("Selected features : ", x_train.columns[Select_K_best.get_support()])