import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def plot_dispersion(x, y):
	plt.scatter(x, y)
	plt.show()
	
def media(x):
	return np.average(x)

def varianza(x):
	return np.var(x, ddof=1)

def covarianza(x, y):
	suma = 0
	n = len(x)
	for i in range(n):
		suma += (x[i] * y[i])
		
	suma = suma - (n * media(x) * media(y))
	
	return suma / (n-1)
	
def correlacion(x, y):
	Sxy = covarianza(x, y)
	Sx = sqrt(varianza(x))
	Sy = sqrt(varianza(y))
	
	return Sxy/(Sx*Sy)
	
	
def coef_correlacion_poblacional(x, y, alpha, p, hyp):
	# hyp
	# 0: H0 p = p0
	# 1: H0 p < p0
	# 2: H0 p > p0
	r = correlacion(x, y)
	n = len(x)
	
	if (p == 0):
		t = r * sqrt( (n-2) / (1 - pow(r, 2))
		df = n - 2
		
		
	

x = [28, 25, 35, 40, 45, 50, 50, 35, 70, 80]
y = [25, 20, 32, 37, 40, 40, 45, 30, 55, 60]

#plot_dispersion(x, y)

print("X, media: ", media(x))
print("Y, media: ", media(y))
print("Covarianza: ", covarianza(x,y))
print("Correlacion: ", correlacion(x,y))
