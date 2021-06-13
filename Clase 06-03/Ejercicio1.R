# R Commander -> Importar datos

library(readxl)
Old_Faithful <- read_excel("Documents/2021-1/EstadisticaII/Clase 06-03/23 - Old Faithful.xlsx")
View(Old_Faithful)

# Regresion seleccionando las 3 variables (R Commander)

regresion = lm(`INTERVALO POSTERIOR`~ALTURA+DURACION+`INTERVALO ANTERIOR`, data = Old_Faithful)
summary(regresion)

# Por la prueba t, vemos que la altura no aporta mucho al modelo, la sacamos.

regresion = lm(`INTERVALO POSTERIOR`~DURACION+`INTERVALO ANTERIOR`, data = Old_Faithful)
summary(regresion)

plot(regresion, 1)

# Pruebas de supuestos

# Normalidad
residuos = regresion$residuals
shapiro.test(residuos)

# Homocedasticidad
library(car) # (Se requiere esta libreria)
ncvTest(regresion)

# Independencia
library(car) # (Se requiere esta libreria)
durbinWatsonTest(regresion) # Halla independencia entre el error e_i y el error e_{i+1}
dwt(regresion) # Halla independencia entre el error e_i y el error e_{i+1}
