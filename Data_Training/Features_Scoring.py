import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2, SelectKBest
data=load_iris()
x=pd.DataFrame(data.data,columns=data.feature_names)
y=data.target

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

Select_K_best = SelectKBest(score_func=chi2, k=2)

x_train_best=Select_K_best.fit_transform(x_train,y_train)
print("Selected Features:",x_train.columns)

print(Select_K_best.get_support())

print("Features:")
for features,score in zip(x_train.columns,Select_K_best.scores_):
    print(features,":",round(score,2))

result=pd.DataFrame(x_train_best,columns=x_train.columns[Select_K_best.get_support()]).head()
print(result)

print("Flowers categories")
for i,flower in enumerate(data.target_names):
    print(i,"=",flower)
