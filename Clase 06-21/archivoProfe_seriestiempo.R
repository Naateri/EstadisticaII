#### serie original
data("AirPassengers")
plot(AirPassengers, main='Cantidad mensual de pasajeros de vuelos internacionales', xlab='Mes/A?o', ylab='Miles de pasajeros')

###### Estabilizando la varianza
# Una forma de estabilizar la varianza es sacando logaritmo
logaritmo.AirPassengers<-log10(AirPassengers)
plot(logaritmo.AirPassengers, main='Cantidad mensual de pasajeros de vuelos internacionales', xlab='Mes/A?o', ylab='log(Miles de pasajeros)')

######## Medias m?viles

install.packages("vars")
library(vars)
plot(logaritmo.AirPassengers, main='Cantidad mensual de pasajeros de vuelos internacionales', xlab='Mes/A?o', ylab='log(Miles de pasajeros)')
lines(rollmean(logaritmo.AirPassengers, 7), col="red", lwd=2)
lines(rollmean(logaritmo.AirPassengers, 7, align="right"), col="blue", lwd=2)
legend("bottomright", c("serie Original", "Media m?vil centrada",
                       "Media m?vil no centrada"),
       lwd=c(1,2,2), col=c("black", "red", "blue"))

####  Suavizamiento exponencial

HoltWinters(logaritmo.AirPassengers,beta=FALSE,gamma=FALSE)
plot(logaritmo.AirPassengers, main='Cantidad mensual de pasajeros de vuelos internacionales', xlab='Mes/A?o', ylab='log(Miles de pasajeros)')
lines(HoltWinters(logaritmo.AirPassengers, 7), col="green", lwd=2)
legend("bottomright", c("serie Original", "Suavizamiento exponencial"), lwd=c(1,2,2), col=c("black", "green"))

###### Descomponiendo la serie

plot(logaritmo.AirPassengers, main='Cantidad mensual de pasajeros de vuelos internacionales', xlab='Mes/A?o', ylab='log(Miles de pasajeros)')
boxplot(logaritmo.AirPassengers~cycle(logaritmo.AirPassengers), xlab='Mes', ylab='log(Miles de pasajeros)')
decompose(logaritmo.AirPassengers)
plot(decompose(logaritmo.AirPassengers))

##### Eliminando la tendencia por diferenciaci?n

x<-diff(logaritmo.AirPassengers) # Xi = X(i+1) - Xi
plot(decompose(x))
y<-diff(x,lag=12) # Xi = X(i+12) - Xi
plot(decompose(y))

###### Verificando estacionariedad

install.packages("tseries")
library(tseries)
adf.test(y)

###    analizando autocorrelacipon

acf(AirPassengers) # Autocorrelacion
acf(logaritmo.AirPassengers)
acf(x) # Sin tendencia
acf(y)
pacf(y)
