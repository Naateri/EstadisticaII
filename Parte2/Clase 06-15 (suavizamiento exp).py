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
		
def error_cuadratico(St, Xt):
	errores = np.zeros(len(Xt))
	for i in range(len(errores)):
		errores[i] = pow(St[i] - Xt[i], 2)
	
	return errores

# Problema ejemplo 1	

data = pd.read_excel('Datos de consumo electrico EXCEL.xlsx', 
	engine='openpyxl')

year = np.array([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997])

Xt = np.array(data["Xt"])

St1 = np.zeros(len(Xt) + 1)
St2 = np.zeros(len(Xt) + 1)

periodos = np.arange(1, len(Xt)+1)
print(periodos)
print(Xt)

suavizamiento(St1, 0.2, Xt)
suavizamiento(St2, 0.3, Xt)

#print(St1)
#print(St2)

errores1 = error_cuadratico(St1, Xt)
errores2 = error_cuadratico(St2, Xt)

#print(errores1)
#print(errores2)

# El profesor dejo la casilla correspondiente a S(0) vacia en ambos casos, por eso para el promedio no lo estoy tomando en cuenta

print("Error ST1 (a=0.2): ", np.average(errores1[1:]))
print("Error ST2 (a=0.3): ", np.average(errores2[1:]))

print("Mejor pronostico para el periodo que sigue: ", St1[-1])

plot_lineas(periodos, [Xt, St1[:-1], St2[:-1]], "Periodos", "Tendencia", "Grafico")
