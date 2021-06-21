import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import sqrt
import pandas as pd

def plot_dispersion(x, y):
	plt.scatter(x, y)
	plt.show()
	
def plot_lineas(x, y, xlab, ylab, title):
	if (type(y) == list):
		for i in range(len(y)):
			plt.plot(x, y[i])
	else:
		plt.plot(x, y)
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.title(title)

	plt.show()
	
	
def plot_reg(x, y, a, b, xlab, ylab, title):
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
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.title(title)
	plt.show()


# St = alpha Xt + (1-alpha) S(t-1)
def suavizamiento(St, alpha, Xt):
	St[0] = Xt[0]
	for i in range(1, len(St)):
		St[i] = alpha * Xt[i-1] + (1 - alpha) * St[i-1]
		
# Usar este para cuando no te pide realizar una prediccion
def suavizamiento_NOPRED(St, alpha, Xt):
	St[0] = Xt[0]
	for i in range(1, len(Xt)):
		St[i] = alpha * Xt[i] + (1 - alpha) * St[i-1]
		
def error_cuadratico(St, Xt):
	errores = np.zeros(len(Xt))
	for i in range(len(errores)):
		errores[i] = pow(St[i] - Xt[i], 2)
	
	return errores


year = np.array([1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998])

Xt = np.array([2, 3, 5, 9, 12, 16, 13, 10, 17, 14, 22, 24])

St1 = np.zeros(len(Xt) + 1)

periodos = np.arange(1, len(Xt)+1)
print(periodos)
print(Xt)

# Halle la tendencia lineal

X = periodos.reshape((-1, 1))

model = LinearRegression().fit(X, Xt)
r_sq = model.score(X, Xt)
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("T(t) = {0} + {1}t".format(a, b))

# Medias moviles de tamanho 5

offset = 5//2

media_movil = np.zeros(len(Xt))

for i in range(offset, len(Xt) - offset):
	media = 0
	for j in range(-2, 3):
		media = media + Xt[i + j]
	
	media = media / 5
	
	media_movil[i] = media
	
print(media_movil)

# Grafique

#plot_lineas(periodos, [Xt, media_movil], "Produccion", "Año", "Grafico")

# Determinar tendencia con suavizamiento exponencial con alpha = 0.4

St1 = np.zeros(len(Xt) + 1)

suavizamiento_NOPRED(St1, 0.4, Xt)

print(St1)
#print(St2)

#plot_lineas(periodos, [Xt, St1[:-1]], "Produccion", "Año", "Grafico (Medias moviles)")

# Ejercicio 2

print('---------------')

year = np.array([1992, 1993, 1994, 1995, 1996, 1997, 1998])
Xt = np.array([8, 12, 17, 18, 20, 23, 25])

periodos = np.arange(1, len(year)+1)
print(periodos)
print(Xt) # Ventas

# Para todos los casos: predecir para 1999

# Halle la tendencia lineal

X = periodos.reshape((-1, 1))

model = LinearRegression().fit(X, Xt)
r_sq = model.score(X, Xt)
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("T(t) = {0} + {1}t".format(a, b))

tendencia_lineal = np.zeros(len(Xt)+1)

for i in range(len(tendencia_lineal)):
	tendencia_lineal[i] = (a +  (i+1)*b)

print(tendencia_lineal)

#plot_reg(periodos, Xt, a, b, "Periodos", "Ventas", "Grafico")

# Prediccion con medias moviles de 3

offset = 3//2

media_movil = np.zeros(len(Xt))

for i in range(offset, len(Xt) - offset):
	media = 0
	for j in range(-1, 2):
		media = media + Xt[i + j]
	
	media = media / 3
	
	media_movil[i] = media
	
print(media_movil)

# Suavizamiento exp 

St1 = np.zeros(len(Xt) + 1)
suavizamiento(St1, 0.4, Xt)

print(St1)

print("Comparacion por errores cuadraticos")

ec_tendencia = np.zeros(len(tendencia_lineal)-1)
ec_mma = np.zeros(len(media_movil))
ec_suav = np.zeros(len(St1)-1)

for i in range(len(ec_tendencia)):
	ec_tendencia[i] = pow(Xt[i] - tendencia_lineal[i], 2)
	
# Ojo: esta tomando en cuenta los 0's
	
for i in range(len(ec_mma)):
	ec_mma[i] = pow(Xt[i] - media_movil[i], 2)
	
# Ojo: esta tomando en cuenta los 0's

for i in range(len(ec_suav)):
	ec_suav[i] = pow(Xt[i] - St1[i], 2)
	
print("E.c. medio:")
print("Tendencia lineal: ", np.average(ec_tendencia))
print("Media movil: ", np.average(ec_mma))
print("Suavizamiento: ", np.average(ec_suav))


