from math import sqrt

def r(s1, s2, n1, n2):
	suma1 = (s1/n1) + (s2/n2)
	numerador = pow(suma1, 2)
	
	suma2 = (s1/n1)
	suma2 = pow(suma2, 2)
	suma2 = suma2 / (n1-1)

	suma3 = (s2/n2)
	suma3 = pow(suma3, 2)
	suma3 = suma3 / (n2-1)
	
	denominador = suma2 + suma3
	
	return numerador / denominador
	
def zc_prop(p1, p2, n1, n2, d0):
	num = (p1-p2) - d0
	suma1 = ( p1*(1-p1) ) / n1
	suma2 = ( p2*(1-p2) ) / n2
	den = sqrt(suma1 + suma2)
	return num/den
	
def bondad_ajuste(o, e, k):
	result = 0
	for i in range(k):
		num = pow( (o[i] - e[i]), 2)
		den = e[i]
		result += (num/den) 
	
	return result
	
def promedio_intervalos(X, F):
	mean = 0
	for i in range(len(X)):
		mean += (X[i] * F[i])
	return mean/len(X)
	
#print(r(4.09, 3.08, 11, 7))
#print(r(132.21, 958.29, 8, 7))
print(zc_prop(0.21, 0.4167, 300, 180, 0))

#o = [15,25,33,17,16,14]
#e = [20] * 6

o = [10, 41, 60, 29]
e = [21.9, 49.2, 44.2, 24.8]


print(e)
print(bondad_ajuste(o,e,len(o)))
