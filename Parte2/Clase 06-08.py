import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import sqrt
import pandas as pd

def plot_dispersion(x, y):
	plt.scatter(x, y)
	plt.show()
	
def plot_lineas(x, y):
	plt.plot(x, y)
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

X = periodos.reshape((-1, 1))

model = LinearRegression().fit(X, Xt)
r_sq = model.score(X, Xt)
print("Coefficient (r2): ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("T(t) = {0} + {1}t".format(a, b))

tendencia_lineal = np.zeros(len(Xt)) # T(t)

for i in range(0,len(tendencia_lineal)):
	tendencia_lineal[i] = a + b*periodos[i]
	
residuos = np.zeros(len(Xt)) # X(t) - T(t)

for i in range(0, len(residuos)):
	residuos[i] = Xt[i] - tendencia_lineal[i]


#print (Xt)	
#print (tendencia_lineal)
#print (residuos)	

plot_reg(periodos, Xt, a, b, 'Periodo (ener-feb 1990=1)', 'Consumo electrico (Kwh)', 'Consumo electrico de la empresa 1990-1997')

# Regresion lineal con los residuos

#model = LinearRegression().fit(X, residuos)
#r_sq = model.score(X, residuos)
#print("Coefficient (r2): ", r_sq)

#a = model.intercept_
#b = model.coef_

#print("a: ", a)
#print("b: ", b)
#print("T(t) = {0} + {1}t".format(a, b))

#plot_reg(periodos, residuos, a, b, 'Periodo', 'X(t) - T(t)', 'Serie sin tendencia')

plot_lineas(periodos, residuos)

# Para la estacionalidad, hallamos promedios por periodo de los residuos
# Ener-Feb, Mar-Abril, May-Jun, Jul-Agos, Set-Oct, Nov-Dic

print()
por_periodo = np.zeros(6)
count_periodos = np.zeros(6)
for i in range(len(Xt)):
	index = i % 6
	por_periodo[index] += residuos[i] 
	count_periodos[index] += 1
	

estacionalidad = np.zeros(6)

for i in range(6):
	estacionalidad[i] = (por_periodo[i] / count_periodos[i])

print(estacionalidad)
# [754, -545, -260, 439.25, 5.7, -393]

# Como es periodo estacional, lo que ocurre en un anho (en este caso) ocurre en todos los demas, por eso solo se calcula para un anho

E = np.zeros(len(periodos))

for i in range(len(periodos)):
	E[i] = estacionalidad[i % 6]
	
plot_lineas(periodos, E)

# Para la componente irregular:
# I(t) = X(t) - T(t) - E(t)

irregular = np.zeros(len(Xt))

for i in range(len(Xt)):
	irregular[i] = Xt[i] - tendencia_lineal[i] - E[i]

print(irregular)
plot_lineas(periodos, irregular)

# Pronosticar para el periodo Julio-Agosto del 2010

# X(t) = T(t) + E(t) + I(t)
# X(t) = a + bt + E(t) + I(t)

bimestres = (2010 - 1990) * 6 + 4

resultado = a + b*bimestres + E[(bimestres-1) % 6]
print("Xt = {0} + {1}*{2} + {3}".format(a, b, bimestres, E[bimestres % 6]))
print(resultado)
