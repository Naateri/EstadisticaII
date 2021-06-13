# Practica 04-29
# Ejercicio 1

# Importar datos
library(readxl)
DATOS_LAB4 <- read_excel("Documents/2021-1/EstadisticaII/Clase 04-29/DATOS-LAB4.xlsx")
View(DATOS_LAB4)

library(nortest)
library(car)
library(Rcmdr)
# Prueba de normalidad

lapply(split(DATOS_LAB4$Tiempo, DATOS_LAB4$Máquinas), shapiro.test)

# Prueba de Levene para homogeneidad de varianzas

leveneTest(Tiempo~Máquinas, data=DATOS_LAB4, center='mean') # O algo asi
# La cosa es que si se cumple H0: 

# Con un nivel de significación de 5%, ¿es posible concluir que las máquinas utilizan la misma velocidad media por unidad de confección?

AnovaModel = aov(Tiempo~Máquinas, data= DATOS_LAB4)
summary(AnovaModel)

with(DATOS_LAB4, numSummary(Tiempo, GROUPS=Máquinas, statistics=c("mean", "sd"))) # Rcmdr
