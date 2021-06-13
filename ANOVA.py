import scipy.stats as stats
import numpy as np

# NOTA:
# Para hallar X(p, dfn, dfd): stats.f.ppf(q=p, dfn=dfn, dfd=dfd)

# Anova: disenho aleatorizado por bloques

def calculo_cuadrados(tabla):
	r = len(tabla)
	k = len(tabla[0])
	print("r: ", r, "k: ", k)
	
	E = np.zeros((r,k))
	
	result = 0
	expected = 0
	
	sum_filas = list()
	sum_columnas = list()
	for i in range(r):
		sum_filas.append(np.sum(tabla[i]))
		
	total = np.sum(sum_filas)
	
	for j in range(k):
		sum_actual = 0
		for i in  range(r):
			sum_actual += tabla[i][j]
		sum_columnas.append(sum_actual)
	
	print("sum filas: ",sum_filas)
	print("sum columnas: ", sum_columnas)
	print("total: ", total)
	
	C = (total*total)/(r*k)
	
	SCT = 0
	
	for i in range(r):
		for j in range(k):
			SCT += (pow(tabla[i][j], 2))
	
	SCT = SCT - C
	
	SCTR = 0
	for i in range(k):
		SCTR += (pow(sum_columnas[i], 2))
	SCTR = SCTR/r
	SCTR = SCTR - C
	
	SCB = 0
	for i in range(r):
		SCB += (pow(sum_filas[i], 2))
	
	SCB = SCB/k
	SCB = SCB - C
	
	SCE = SCT - (SCTR + SCB)
	
	print ("C: ", C)
	print("SCT: ", SCT)
	print("SCTR: ", SCTR)
	print("SCB: ", SCB)
	
	return SCE,SCB,SCTR
			
	
def anova_factores_bloques(tabla, alpha,/,tipo='TR'):
	r = len(tabla)
	k = len(tabla[0])
	
	# Tratamientos
	
	SCE,SCB,SCTR = calculo_cuadrados(tabla)
	
	CME = SCE/((k-1)*(r-1))
	
	#print("CME:", CME)
	
	if (tipo == 'TR'):
		dfn = (k-1)

		CMTR = SCTR/(k-1)	
		#print("CMTR:", CMTR)
		F = CMTR/CME
	else:
		dfn = (r-1)
		
		CMB = SCB/(r-1)
		F = CMB/CME
	
	dfd = (k-1)*(r-1)
	critical_region = stats.f.ppf(q=1-alpha, dfn=dfn, dfd=dfd)
#	print("dfn: ", dfn)
#	print("dfd: ", dfd)
	print("critical region: ", critical_region)

		
	print("F:",F)
	
	if F >= critical_region:
		return True
	else:
		return False
		
def interpretar_prueba(tab_contingencia, alpha):
	result = prueba_independencia(tab_contingencia, alpha)
	if result:
		print("Aceptamos H0. Las variables son independientes.")
	else:
		print("Rechazamos H0, aceptamos H1. Las variables son dependientes.")


datos = [ [12, 15, 11, 16, 13],
	[7, 12, 7, 12, 8],
	[8, 14, 7, 12, 8],
	[6, 10, 6, 13, 7]]

datos = [ [470, 191, 42],
	[445, 171, 28],
	[257, 129, 17] ]
	
#calculo_cuadrados(datos)
anova_factores_bloques(datos, 0.05)
