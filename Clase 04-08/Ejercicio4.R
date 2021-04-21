# Ejercicio 4

library(readxl)
Body <- read_excel("Documents/2021-1/EstadisticaII/Clase 04-08/01 - Body Data.xlsx")
#View(Body)

# Cambia 0 por mujer, 1 por hombre
Body$`GENDER (1=M)` = factor(Body$`GENDER (1=M)`, levels = c(0,1), labels=c("Mujer", "Hombre"))

# Verificamos normalidad

lapply(split(Body$PULSE, Body$`GENDER (1=M)`), shapiro.test)

# Verificamos igualdad de varianzas

var.test(PULSE~`GENDER (1=M)`, data=Body)

# Comparamos las medias
# var.equal = TRUE: estamos diciendo que asuma que las varianzas son iguales

t.test(PULSE~`GENDER (1=M)`, var.equal=TRUE, alternative="greater", data=Body)

