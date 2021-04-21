import scipy.stats as stats
import numpy as np

# Calculos distribucion binomial
# F(a, n1, n2)

# Asumimos que tenemos los siguientes datos:

p = 0.31
n = 5

# Queremos calcular:
# P(X = 0)
# P(X = 1)
# P(X = 2)
# P(X = 3)
# P(X = 4)
# P(X = 5)

X = range(6)
values = np.zeros(6)

for x in X: # en este caso coinciden indices
	values[x] = stats.binom.pmf(x, n, p)
	# con stats.binom.cdf se calcula el acumulado
	# con stats.binom.pmf se calcula en el lugar

	print("P(X={0}) = {1}".format(x, values[x]))
