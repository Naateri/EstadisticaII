# Body
# prueba t de estudent para la media del pulso, H1: mu > 60

#t.test(Body$PULSE,mu=60) # Con dolar accedemos solo a una columna, en este caso PULSE
# Poniendo mu=60, nos hara una prueba bilateral
t.test(Body$PULSE,mu=60, alternative='greater') #con eso le estamos indicando que haga
# una prueba lateral derecha

# Recordatorio: para que funcione la prueba t de estudent, la muestra debe ser normal
# Sin embargo, como este conjunto de datos es grande, no es necesario probarlo

# OJO: si la muestra es grande, usar Z o t es similar, deberian dar la misma respuesta

################################################################################

# Recordatorio: p < alfa, se rechaza H0, se acepta H1
# Resultado de ejecución:

# One Sample t-test

# data:  Body$PULSE (datos analizados)
# t = 16.804, df = 299, p-value < 2.2e-16 (valor del estadistico t, df=g.l. (n-1), p-valor)
# alternative hypothesis: true mean is greater than 60 (hipotesis alternativa H1)
# 95 percent confidence interval: (valor de alfa, por defecto: 0.05)
#   70.61134      Inf   (intervalo de confianza, en este caso [70.6, +INF[)
# sample estimates:
#   mean of x   (media de la muestra)
# 71.76667   (en este caso, 71.76667)