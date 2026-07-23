import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

np.random.seed(42)
X = 6 * np.random.rand(100, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1)


poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

plt.scatter(X, y, color="blue", label="Data")
X_sorted = np.sort(X, axis=0)
plt.plot(X_sorted, model.predict(poly.transform(X_sorted)), color="red", label="Fit")

plt.legend()
plt.savefig("Polynnomial_Linear_Regression.jpeg")
plt.show()