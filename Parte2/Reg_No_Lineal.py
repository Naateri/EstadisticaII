import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import sqrt

def plot_dispersion(x, y, /, title=0, x_lab=0, y_lab=0):

	if title != 0:
		plt.title(title)
	
	if x_lab != 0:
		plt.xlabel(x_lab)
	
	if y_lab != 0:
		plt.ylabel(y_lab)
	
	plt.scatter(x, y)
	plt.show()
	
def plot_reg(x, y, a, b, /, title=0, x_lab=0, y_lab=0):
	min_x = np.min(x)
	max_x = np.max(x)
	min_y = np.min(y)
	max_y = np.max(y)
	
	x_range = np.linspace(min_x, max_x, 50)
	y_range = np.zeros(50)
	for i in range(50):
		y_range[i] = a + b*x_range[i]
	
	plt.scatter(x, y)
	plt.plot(x_range, y_range, c='orange')
	
	if title != 0:
		plt.title(title)
	
	if x_lab != 0:
		plt.xlabel(x_lab)
	
	if y_lab != 0:
		plt.ylabel(y_lab)
	
	plt.show()

# Problema ejemplo 1 - Clase 05/31

x = np.array([0.01, 0.06, 0.58, 2.24, 15.55, 276.02])
y = np.array([3.32, 4.05, 5.69, 7.06, 8.17, 9.36])

X = x.reshape((-1, 1))

model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print("Coefficient (r): ", sqrt(r_sq))
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("y = {0} + {1}x".format(a, b))

#plot_dispersion(x, y, title="Volumen vs pct de ceniza de particulas de carbon", x_lab="volumen", y_lab="pct ceniza")

#plot_reg(x, y, a, b[0], title="Volumen vs pct de ceniza de particulas de carbon", x_lab="volumen", y_lab="pct ceniza")

print("-----------Log-----------")
logx = np.log(x)

X = logx.reshape((-1, 1))

model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print("Coefficient (r): ", sqrt(r_sq))
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("y = {0} + {1}lnx".format(a, b))

#plot_reg(logx, y, a, b[0], title="Ln(Volumen) vs pct de ceniza de particulas de carbon", x_lab="Ln(volumen)", y_lab="pct ceniza")

print("\n-----------Ejercicio 2------------\n")

x = np.array([3.84, 4.76, 6.08, 7.06, 8.28])
y = np.array([0.44, 0.49, 0.60, 0.64, 0.72])

X = x.reshape((-1, 1))

print("Lineal:")

model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print("Coefficient (r): ", sqrt(r_sq))
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("y = {0} + {1}x".format(a, b))

"""
# Potencia: lnY = ln a + b ln X
logx = np.log(x)
logy = np.log(y)

print("\nPotencia")

X = logx.reshape((-1, 1))

model = LinearRegression().fit(X, logy)
r_sq = model.score(X, logy)
print("Coefficient (r): ", sqrt(r_sq))
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
# Y = Ax^b
print("Y = {0}x^{1}".format(a, b))

print("\nExponencial")

# Exponencial: ln Y = ln a + bX

X = x.reshape((-1, 1))

model = LinearRegression().fit(X, logy)
r_sq = model.score(X, logy)
print("Coefficient (r): ", sqrt(r_sq))
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
# Y = a * (e^(bx))
print("y = {0} * e^({1}x)".format(a, b))
"""
print("\nLogaritmica")

# Logaritmica: Y = a + b ln(X)

X = logx.reshape((-1, 1))

model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print("Coefficient (r): ", sqrt(r_sq))
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
# Y = a + b ln(x)
print("y = {0} + {1} lnx".format(a, b))
