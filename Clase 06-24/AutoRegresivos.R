data("JohnsonJohnson")
x<-JohnsonJohnson
# 1. Graficar la serie
plot(x)
# 2. Estabilizar varianza (es necesario)
y<-log10(x)
plot(y)
# 3. Datos no estacionarios, diferenciar la serie para eliminar estacionalidad
z<-diff(y)
plot(z)

# Corroborar que la serie es estacionaria con una prueba adf
#library(tseries)
#adf.test(z)

# Examinar ACF y PACF
par(mfrow = c(1, 1))
acf(z) # q = 1
# Ojo: empieza en 0, por lo que no se cuenta el primero
pacf(z) # p = 2
# Ojo: en este caso, no se esta incluyendo al 0 en el grafico
# No se estan considerando los 2 ultimos porque son parte de la estacionalidad
# Tip: ver de manera decreciente (asi solo quedarian 2)
# Sugerencias a partir de esto:
# AR(2), MA(1), ARIMA(2,1,1)

#install.packages("forecast")
#library(forecast)
#auto.arima(y) # Halla el ARIMA ideal para la serie y

# Modelo propuesto: ARIMA (2,0,0) (1,1,0) [4]
## Modelo arima con estacionalidad (cada 4 hay estacionalidad)
## Aic = -287

# Nuestro arima
arima(y, order=c(2,1,1)) # Aic = -178.8, el aic de autoarima es menor