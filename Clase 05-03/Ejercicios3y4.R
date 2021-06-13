# Ejercicio 3
library(readxl)
Movies <- read_excel("Documents/2021-1/EstadisticaII/Clase 05-03/11 - Alcohol and Tobacco in Movies.xlsx")
View(Movies)

# a) ¿Las duraciones de las películas producidas por los 
# estudios Disney, M&M, Warner Bross, Universal provienen de una distribución normal?

# c) Compare la duración de las películas infantiles producidas por los estudios Disney,
# M&M, Warner Bross, Universal. ¿Son iguales las duraciones de las películas? 

pairs = glht(AnovaModel1.1, linfct=mcp(STUDIO = "tukey")) 
print(summary(pairs))

# Ejercicio 4
library(readxl)
Datos_ingresos <- read_excel("Documents/2021-1/EstadisticaII/Clase 05-03/Datos-ingresos.xlsx")
View(Datos_ingresos)

# a) Al nivel de significación de 5%, aplique una prueba de hipótesis
# para determinar si las medias son significativamente iguales.

AnovaModel = aov(Ingresos~Ciudades, data= Datos_ingresos)
summary(AnovaModel)
