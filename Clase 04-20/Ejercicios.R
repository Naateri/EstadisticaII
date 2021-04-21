# 1- Remítase al conjunto de datos 04 – Births (disponible en el aula virtual
# , en la carpeta base de datos) y realice las pruebas necesarias para 
# responder a las preguntas:
# a) ¿Los pesos de los recién nacidos se distribuye normalmente?

library(readxl)
library(nortest)
Births <- read_excel("Documents/2021-1/EstadisticaII/Clase 04-20/04 - Births.xlsx")
View(Births)

lillie.test(Births$`BIRTH WEIGHT`)

# b)¿La proporción de bebes de sexo femenino es igual a 50%?

# Cambia 0 por mujer, 1 por hombre
Births$`GENDER (1=M)` = factor(Births$`GENDER (1=M)`, levels = c(0,1), labels=c("Mujer", "Hombre"))
total = length(Births$`GENDER (1=M)`)
print(Births$`GENDER (1=M)`)

# Hallamos la cantidad de mujeres en los nacimientos
fem = 0
for (val in Births$`GENDER (1=M)`){
  if (val == "Mujer"){
    fem = fem + 1
  }
}
print (fem)
prop.test(fem, total, p=0.50, alternative="two.sided", conf.level=0.95)

# c) ¿Los partos ocurren todos los días con la misma frecuencia?

# La frecuencia deberia ser la misma todos los dias
# Por tanto, la frecuencia relativa por dia es de 1/7
probs = c(1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7)
# Creamos una tabla con la relacion de frecuencias
# Para poder utilizar la funcion chisq.test
table = with(Births, table(ADMITTED))
print(table) # Relación de frecuencias
chisq.test(table, p=probs) # Prueba chi cuadrado de bondad de ajuste

# d) ¿El seguro y el día de admisión son variables independientes?

# Crear tabla de contingencia
tabla_contingencia = xtabs(~INSURANCE+ADMITTED, data=Births)
print(tabla_contingencia)
# Aplicar prueba chi cuadrado para la independencia de variables
test = chisq.test(tabla_contingencia, correct=FALSE)
print(test)
print("Expected counts: ")
print(test$expected)
