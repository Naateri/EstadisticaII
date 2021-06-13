import scipy.stats as stats
import numpy as np

# NOTA:
# Para hallar Chi(p, df): stats.chi2.ppf(p, df)

def estadistico_chi(tab_contingencia):
	k = len(tab_contingencia)
	c = len(tab_contingencia[0])
	
	E = np.zeros((k, c))
	
	result = 0
	expected = 0
	
	sum_filas = list()
	sum_columnas = list()
	for i in range(k):
		sum_filas.append(np.sum(tab_contingencia[i]))
		
	total = np.sum(sum_filas)
	
	for j in range(c):
		sum_actual = 0
		for i in  range(k):
			sum_actual += tab_contingencia[i][j]
		sum_columnas.append(sum_actual)
	
	print("sum filas: ",sum_filas)
	print("sum columnas: ", sum_columnas)
	print("total: ", total)
	
	for i in range(k):
		for j in range(c):
			expected = (sum_filas[i] * sum_columnas[j])/total
			E[i][j] = expected
			o = tab_contingencia[i][j]
			
			result += (pow(o - expected, 2) / expected)
			
	print ("e11: ", (sum_filas[0] * sum_columnas[0])/total)
	#print(E)
	
	return result
	
def prueba_independencia(tab_contingencia, alpha):
	k = len(tab_contingencia)
	c = len(tab_contingencia[0])
	df = (k-1) * (c-1)
	critical_region = stats.chi2.ppf(alpha, df)
	estadistico = estadistico_chi(tab_contingencia)
	if estadistico <= critical_region:
		return True
	else:
		return False
		
def interpretar_prueba(tab_contingencia, alpha):
	result = prueba_independencia(tab_contingencia, alpha)
	if result:
		print("Aceptamos H0. Las variables son independientes.")
	else:
		print("Rechazamos H0, aceptamos H1. Las variables son dependientes.")


tab = [ [12, 14, 30], [18, 16, 24], [12, 8, 4]]

# Resultado = 10.35

#print(estadistico_chi(tab))

tab = [ [10, 13, 29], [19, 80, 19], [81, 57, 22]]
#print(estadistico_chi(tab))

#interpretar_prueba(tab, 0.01)

tab = [ [70, 64, 66], [63, 68, 69] ]
print(estadistico_chi(tab))
