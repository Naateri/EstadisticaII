# Importando data

library(readxl)
Old_Faithful <- read_excel("Documents/2021-1/EstadisticaII/Clase 05-25/23 - Old Faithful.xlsx")
View(Old_Faithful)

# a) Construya diagramas de dispersión entre las variables independientes 
# “INTERVALO ANTERIOR”, “DURACIÓN”, “ALTURA” y la variable dependiente
# “INTERVALO POSTERIOR”. ¿Cuáles son sus conclusiones?
# R Commander -> Matriz de diagramas de dispersión -> Altura/Duracion/Intervalo Anterior/Intervalo Posterior

# b)
# R Commander - Estadístico -> Matriz de correlaciones -> Coeficiente de pearson, observaciones completas, p-valor

# c)
# R Commander - Regresión Lineal
# Variable explicada: Intervalo posterior
# Variable explicativa: Duracion

regresion1 = lm(`INTERVALO POSTERIOR`~DURACION, data=Old_Faithful)
summary(regresion1)
anova(regresion1) # Parte f pregunta c)

# Supuestos
residuos = rstandard(regresion1)
# Independencia
# Linealidad 
# Homocedasticidad
# Linealidad

#Normalidad

residuos = regresion1$residuals
shapiro.test(residuos)

qqnorm(regresion1$residuals)
qqline(regresion1$residuals)

# Homocedasticidad

plot(regresion1$fitted.values, residuos, xlab="Valores ajustados", ylab="Residuos")


# library(car) (Se requiere esta libreria)
ncvTest(regresion1)

# linealidad
plot(regresion1,1)

# independencia
library(lmtest)
durbinWatsonTest(regresion1)
dwtest(regresion1)

# Durbib watson busca corrleación entre un valor y el siguiente