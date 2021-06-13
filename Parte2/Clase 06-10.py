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

# Problema ejemplo 1	

data = pd.read_excel('Datos de consumo electrico EXCEL.xlsx', 
	engine='openpyxl')

year = np.array([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997])

Xt = np.array(data["Xt"])

periodos = np.arange(1, len(Xt)+1)
print(periodos)
print(Xt)

# Hallar media movil centrada de longitud 7

offset = 7//2

media_movil = np.zeros(len(Xt))

for i in range(offset, len(Xt) - offset):
	media = 0
	for j in range(-3, 4):
		media = media + Xt[i + j]
	
	media = media / 7
	
	media_movil[i] = media
	
print(media_movil)
	
tendencia_lineal = np.zeros(len(Xt)) # T(t)

	
residuos = np.zeros(len(Xt)) # X(t) - T(t)

for i in range(offset, len(residuos)-offset):
	residuos[i] = Xt[i] - media_movil[i]
	
print(residuos)

# Para estacionalidad, tomar en cuenta:
# El calculo va a ser el promedio de los residuos
# Pero no hay datos para los 3 primeros valores
# Ni para los 3 ultimos
estacionalidad = np.zeros(6)

acum_bimestres = np.zeros(6)
count_bimestres = np.zeros(6)
for i in range(len(Xt)):
	valor = residuos[i]
	if (valor != 0):
		acum_bimestres[i % 6] += valor
		count_bimestres[i % 6] += 1

for i in range(6):
	estacionalidad[i] = acum_bimestres[i] / count_bimestres[i]
	
print(estacionalidad)

# I(t) = R(t) - E(t)

irregular = np.zeros(len(Xt))

for i in range(len(Xt)):
	if (residuos[i] != 0):
		irregular[i] = residuos[i] - estacionalidad[i % 6]
		
print(irregular)

plot_lineas(periodos, [Xt, media_movil], "Bimestre", "Consumo", "Consumo electrico bimestral")

plot_lineas(periodos, residuos, "Bimestre", "Residuo", "Residuos")

plot_lineas(periodos, irregular, "periodo", "I(t)", "Componente irregular")

# Calculo para Ene-Feb 1998

t = 49
media_movil_t = 0

# Xt = (X_{t-1} + X_{t-2} + ... + X_{t-7}) / 7

for i in range(7):
	media_movil_t += Xt[t-i-2]

pronostico = media_movil_t/7 + estacionalidad[(t-1) % 6]
print("Pronostico: ", pronostico)
