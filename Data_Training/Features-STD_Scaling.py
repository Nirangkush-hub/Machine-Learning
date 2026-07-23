import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
df=pd.DataFrame({"Experience":[1,2,3,4,5],"Salary":[30000,45000,60000,90000,120000]})


print("The original Data set: \n",df)
x=df[["Experience"]]
y=df[["Salary"]]
print("Values of the Indepenednt variable(x):\n",x)
print("Vlaues of the Dependent variable(y):\n",y)


x_Train,x_Test,y_Train,y_Test=train_test_split(x,y,test_size=0.2,random_state=1)


print("\n The Split data for TRAINING INDEPENDENT variable(x):\n",x_Train)
print("\n The Split data for TESTING INDEPENDENT variable(x):\n",x_Test)
print("\n The Split data for TRAINING DEPENDENT variable(y):\n",y_Train)
print("\n The Split data for TESTING DEPENDENT variable(x):\n",y_Test)

scaler=StandardScaler()

x_Train_Scaled=scaler.fit_transform(x_Train)
x_Test_Scaled=scaler.transform(x_Test)
y_Train_Scaled=scaler.fit_transform(y_Train)
y_Test_Scaled=scaler.transform(y_Test)
print("\n The Split data After SCALING DEPENDENT variable(x):\n",x_Train_Scaled)
print("\n The Split data After SCALING TESTING INDEPENDENT variable(x):\n",x_Test_Scaled)
print("\n The Split data After SCALING TRAINING DEPENDENT variable(y):\n",y_Train_Scaled)
print("\n The Split data After SCALING TESTING DEPENDENT variable(x):\n",y_Test_Scaled)