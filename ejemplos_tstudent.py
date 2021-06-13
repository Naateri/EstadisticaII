import scipy.stats as stats

# Calculo t de student con grados de libertad n
n = 28
alpha = 0.975
print(stats.t.ppf(alpha, n))
