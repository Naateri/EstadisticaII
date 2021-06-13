import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import sqrt
import scipy

# Importando data

data = pd.read_excel('23 - Old Faithful.xlsx', 
	engine='openpyxl')
#print(data["INTERVALO ANTERIOR"])

# a) Construya diagramas de dispersión entre las variables independientes “INTERVALO ANTERIOR”, “DURACIÓN”, “ALTURA” y la variable dependiente “INTERVALO POSTERIOR”. ¿Cuáles son sus conclusiones?

inter_posterior = np.array(data["INTERVALO POSTERIOR"])
inter_anterior = np.array(data["INTERVALO ANTERIOR"])
duracion = np.array(data["DURACION"])
altura = np.array(data["ALTURA"])

"""

plt.scatter(inter_anterior, inter_posterior)
#plt.savefig("inter_anterior_posterior.png")
plt.show()
# Relacion lineal negativa

plt.scatter(duracion, inter_posterior)
#plt.savefig("duracion_posterior.png")
plt.show()
# Relacion lineal positiva

plt.scatter(altura, inter_posterior)
#plt.savefig("altura_posterior.png")
plt.show()
# No hay relacion lineal
"""

# b) Encuentre una matriz de correlación entre esas variables. ¿cuáles de ellas están significativamente correlacionadas? Explique.

corr_mat = data.corr()
print(corr_mat)

corr_post = corr_mat["INTERVALO POSTERIOR"]
corr_ant = corr_mat["INTERVALO ANTERIOR"]
corr_duracion = corr_mat["DURACION"]
corr_altura = corr_mat["ALTURA"]

print("\nAltura: ")
print(corr_altura)


print("\nDuracion: ")
print(corr_duracion)


print("\nIntervalo anterior: ")
print(corr_ant)


print("\nIntervalo posterior: ")
print(corr_post)

# c) Realice un análisis de regresión entre la “DURACIÓN” y el “INTERVALO POSTERIOR”.
# a. Escriba la ecuación

x = duracion[:len(duracion)-1]
y = inter_posterior[:len(inter_posterior)-1]

X = x.reshape((-1, 1))

print("\nSklearn:")
model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print("Coefficient (r): ", sqrt(r_sq))
print("r2: ", r_sq)

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("y = {0} + {1}x".format(a, b))

print("\nScipy:")

scipy_model = scipy.stats.linregress(x, y)

a = scipy_model.intercept
b = scipy_model.slope
p_value = scipy_model.pvalue
r_sq = scipy_model.rvalue

print("Coefficient (r): ", r_sq)
print("r2: ", r_sq**2)
print("a: ", a)
print("b: ", b)
print("y = {0} + {1}x".format(a, b))
print("P-value: ", p_value)
