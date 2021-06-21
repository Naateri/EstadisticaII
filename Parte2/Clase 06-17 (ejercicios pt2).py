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


year = np.array([1993, 1994, 1995, 1996, 1997, 1998])

Xt = np.array([10, 14, 17, 22,
11, 15, 16, 19,
12, 20, 18, 22,
12, 20, 18, 22,
11, 13, 17, 19,
15, 17, 25, 27,
19, 21, 28, 29])

# Graficar serie de tiempo

periodos = np.arange(1, len(Xt)+1)
print(periodos)
print(Xt)

plot_lineas(periodos, Xt, "Periodo", "Pedidos", "Grafico")

# Hallar estacionalidad (son trimestres)

E = np.zeros(4)

media_global = np.average(Xt)
print("media global: ", media_global)
medias_periodos = np.zeros(4)
total_periodos = np.zeros(4)
for i in range(len(Xt)):
	medias_periodos[i % 4] += Xt[i]
	total_periodos[i % 4] += 1
	
for i in range(4):
	E[i] = (medias_periodos[i] / total_periodos[i]) - media_global
	
print("Estacionalidad: ")
print(E)

# Desestacionalizar la serie
# = X(t) - E(t)

desestacionalizada = np.zeros(len(Xt))
for i in range(len(Xt)):
	desestacionalizada[i] = Xt[i] - E[i%4]
	
print(desestacionalizada)

plot_lineas(periodos, desestacionalizada, "Periodo", "Pedidos", "Grafico (desestacionalizado)")

# Halle la tendencia lineal (serie desestacionalizada)

X = periodos.reshape((-1, 1))

model = LinearRegression().fit(X, desestacionalizada)
r_sq = model.score(X, desestacionalizada)
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("T(t) = {0} + {1}t".format(a, b))

Tt = np.zeros(len(Xt)) # Tendencia lineal

for i in range(len(Xt)):
	Tt[i] = a + b*(desestacionalizada[i])
	
print(Tt)

# Medias moviles ASIMETRICAS de tamanho 7

media_movil = np.zeros(len(Xt))
offset = 7
for i in range(offset, len(media_movil)):
	media = 0
	for j in range(0, offset):
		media = media + desestacionalizada[i + j]
	
	media = media / 7
	
	media_movil[i] = media
	
print(media_movil)

# Grafique

#plot_lineas(periodos, [Xt, media_movil], "Produccion", "Año", "Grafico")

# Determinar tendencia con suavizamiento exponencial con alpha = 0.4

St1 = np.zeros(len(desestacionalizada) + 1)

suavizamiento(St1, 0.4, Xt)

print(St1)
#print(St2)

# NOTA: PARA TENER LOS PRONOSTICOS FINALES DE UNA SERIE DESESTACIONALIZADA, SE DEBE SUMAR SU E(T) CORRESPONDIENTE

t_prediccion = len(Xt)+1
