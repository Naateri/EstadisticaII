import scipy.stats as stats

# Calculo de F de Fischer
# F(a, n1, n2)

# Ej: F(0.975, 7, 6)
f = stats.f.ppf(q=0.975, dfn=7, dfd=6)
# dfn: degrees of freedom numerator
# dfd: degrees of freedmon denominator
print("f = ", f)

# Ej: F(1-0.975, 7, 6)
f = stats.f.ppf(q=1-0.975, dfn=7, dfd=6)
print("f = ", f)

# Corroborando usando 1/F(1-a, n2, n1)
f = stats.f.ppf(q=0.975, dfn=6, dfd=7)
print("f = ", 1/f)

# Hallar varianzas: np.var(array, ddof=1)
# stats.f.cdf(x=valor, dfn, dfd): halla lo opuesto a ppf (es decir, el alfa o el q)
