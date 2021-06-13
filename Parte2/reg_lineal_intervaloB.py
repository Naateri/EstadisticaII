import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import sqrt

def plot_dispersion(x, y):
	plt.scatter(x, y)
	plt.show()
	
def plot_reg(x, y, a, b):
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
	plt.show()
	
def suma_cuadrados(x):
	n = len(x)
	suma = 0
	for value in x:
		suma = suma + (pow(value, 2))
	
	return suma
	
def suma_multipl(x, y):
	n = len(x)
	suma = 0
	for i in range(n):
		suma = suma + (x[i] * y[i])
	
	return suma
	
def s_regresion(x, y, a, b):
	x2 = suma_cuadrados(x)
	y2 = suma_cuadrados(y)
	xy = suma_multipl(x, y)
	suma_y = sum(y)
	n = len(y)
	
	numerador = y2 - a*suma_y - b*xy
	denominador = n-2
	return sqrt(numerador/denominador)
	
def s_b(s, x):
	x2 = suma_cuadrados(x)
	n = len(x)
	
	media_cuadrado = pow(np.average(x), 2)
	
	denominador = sqrt(x2 - n*media_cuadrado)
	
	return s / denominador

# Problema ejemplo 1	

x = np.array([10, 19, 27, 31, 40, 52, 64]) # Calificacion
y = np.array([44, 47, 58, 60, 62, 64, 68]) # Ventas

X = x.reshape((-1, 1))

model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print("Coefficient (r): ", sqrt(r_sq))

a = model.intercept_
b = model.coef_

s = s_regresion(x, y, a, b[0])

print("a: ", a)
print("b: ", b)
print("y = {0} + {1}x".format(a, b))
print("s: ", s)
print(s_b(s, x))

#plot_reg(x, y, a, b[0])

#plot_dispersion(x, y)
