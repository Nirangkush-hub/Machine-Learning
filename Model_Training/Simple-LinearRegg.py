import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

print("--- Simple Linear Regression ---")
print("Intercept (c):   ",(model.intercept_[0]))
print("Coefficient (m): ",(model.coef_[0][0]))
print("Mean Squared Error:   ",mean_squared_error(y_test, y_pred))



X_grid = np.linspace(0, 2, 100).reshape(-1, 1)
y_grid_pred = model.predict(X_grid)

plt.scatter(X, y, color="blue", label="Data Points", alpha=0.6)
plt.plot(
    X_grid,
    y_grid_pred,
    color="red",linewidth=2,
    label="Fitted Line (y = mx + c)")
plt.title("Simple Linear Regression")
plt.xlabel("X (Feature)")
plt.ylabel("y (Target)")
plt.legend()
plt.grid(True)
plt.savefig("Simple_Linear_Regression.png")
plt.show()
