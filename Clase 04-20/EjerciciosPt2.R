# (Continuacion de Ejercicios.R)
# Clase 04-22
# 1- Remítase al conjunto de datos 04 – Births (disponible en el aula virtual
# , en la carpeta base de datos) y realice las pruebas necesarias para 
# responder a las preguntas:
library(readxl)
library(nortest)
Births <- read_excel("Documents/2021-1/EstadisticaII/Clase 04-20/04 - Births.xlsx")
View(Births)
# e) ¿El día de admisión y el día de salida son variables independientes?

tab_contingencia = xtabs(~ADMITTED+DISCHARGED, data=Births) # Creando tabla de contingencia
print(tab_contingencia)
prueba_ind = chisq.test(tab_contingencia, correct=FALSE) # Prueba de independencia chi2
print(prueba_ind)
print("Expected values: ")
print(prueba_ind$expected)

# f) ¿Podemos concluir que la distribución de frecuencias para las seguradoras es:
# Blue Cross 25%, Champus 5%, Insurance Company 50%, Medicaid 15%, Self Pay 5%?

# Creamos una tabla con la relacion de frecuencias
# Para poder utilizar la funcion chisq.test
table_seguros = with(Births, table(INSURANCE))
print(table_seguros) # Relación de frecuencias

# Ponemos la frecuencia de las aseguradoras 
# Segun como estan guardadas en table_seguros
probs = c(0.25, 0.05, 0.50, 0.15, 0.05)
prueba_bondad = chisq.test(table_seguros, p=probs) # Prueba chi cuadrado de bondad de ajuste

print(prueba_bondad)
print("Frecuencias observadas")
print(table_seguros)
print("Frecuencias esperadas")
print(prueba_bondad$expected)

# g) ¿El hospital y el seguro son independientes?

# Creando tabla de contingencia
tab_contingencia = xtabs(~FACILITY+INSURANCE, data=Births) 
print(tab_contingencia)
prueba_ind = chisq.test(tab_contingencia, correct=FALSE) # Prueba de independencia chi2
print(prueba_ind)
print("Expected values: ")
print(prueba_ind$expected)

# h) ¿Es verdad que los bebes nacen con un peso aproximado de 3400 gramos?

# Población normal: prueba t para media
# Población no normal: prueba de wilcoxon para medianas

normal = lillie.test(Births$`BIRTH WEIGHT`)
print(normal)
if (normal$p.value <= 0.05){
  print("Variable no tiene distribución normal.")
} else {
  print("Variable tiene distribucion normal.")
}

# Prueba de wilcoxon: H0: Me = 3400
prueba = wilcox.test(Births$`BIRTH WEIGHT`, mu=3400, alternative="two.sided")
print(prueba)

# i) ¿Es verdad que los niños nacen con pesos mayores que las niñas?

# Cambiar numeros por categoria para que R no lo tome como variable numerica
Births$`GENDER (1=M)` = factor(Births$`GENDER (1=M)`, levels = c(0,1), labels=c("Mujer", "Hombre"))
males = 0
females = 0

# Arreglo para guardar 0 si es mujer, 1 si es hombre
values = numeric(length(Births$`GENDER (1=M)`))
index = 0 +1

# Bucle que llena values
for (val in Births$`GENDER (1=M)`){
  if (val == "Mujer"){
    females = females + 1
    values[index] = 0
  } else {
    males = males + 1
    values[index] = 1
  }
  index = index + 1
}

#print(values[1])
total = males + females
male_weights = numeric(males)  # Arreglo de 0's de tamanho males
female_weights = numeric(females)

male_index = 0 +1
female_index = 0 +1
index = 0 +1
# Llenando arreglo de pesos segun sexo

for (val in Births$`BIRTH WEIGHT`){
  if (values[index] == 0){
    female_weights[female_index] = val
    female_index = female_index + 1
  } else {
    male_weights[male_index] = val
    male_index = male_index + 1
  }
  index = index + 1
}

print(male_weights)
print(female_weights)

# Me1: Femenino. Me2: Masculino.

# Prueba U de Mann-Whitney
wilcox.test(female_weights, male_weights, alternative="less")
#wilcox.test(y,x)

#wilcox.test(male_weights, female_weights, alternative="greater")
