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
	
	plt.plot(x, y)
	plt.plot(x_range, y_range, '--', c='orange')
	plt.xlabel('Periodo')
	plt.ylabel('Produccion anual')
	plt.title('Produccion anual de la empresa')
	plt.show()

# Problema ejemplo 1	

year = np.array([1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998])
producciones = np.array([2, 3, 5, 9, 12, 16, 13, 10, 17, 14, 22, 24])

periodos = np.arange(1, len(year)+1)
print(periodos)

X = periodos.reshape((-1, 1))

model = LinearRegression().fit(X, producciones)
r_sq = model.score(X, producciones)
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("T(t) = {0} + {1}t".format(a, b))

tendencia_lineal = np.zeros(len(producciones))

for i in range(0,len(tendencia_lineal)):
	tendencia_lineal[i] = a + b*periodos[i]
	
residuos = np.zeros(len(producciones))

for i in range(0, len(residuos)):
	residuos[i] = producciones[i] - tendencia_lineal[i]


print (producciones)	
print (tendencia_lineal)
print (residuos)	

plot_reg(periodos, producciones, a, b[0])

######### 

model = LinearRegression().fit(X, residuos)
r_sq = model.score(X, residuos)
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

#print("a: ", a)
#print("b: ", b)
#print("T(t) = {0} + {1}t".format(a, b))

min_x = np.min(periodos)
max_x = np.max(periodos)
min_y = np.min(residuos)
max_y = np.max(residuos)
	

x_range = np.linspace(min_x, max_x, 50)
y_range = np.zeros(50)

for i in range(50):
	y_range[i] = a + b*x_range[i]

plt.scatter(periodos, residuos)
plt.plot(x_range, y_range, '--', c='orange')
plt.xlabel('Periodo')
plt.ylabel('Residuos')
#plt.title('Produccion anual de la empresa')
plt.show()

