library(readxl)
Monedas <- read_excel("Documents/2021-1/EstadisticaII/Clase 04-08/29 - Coin Weights.xlsx")
## View(Monedas)

# Prueba para normalidad de poblaciones
lillie.test(Monedas$`PRE-1964 QUARTERS`)
shapiro.test(Monedas$`PRE-1964 QUARTERS`)
shapiro.test(Monedas$`POST-1964 QUARTERS`)

# Prueba para ver varianzas iguales (homocesdasticidad)
var.test(Monedas$`PRE-1964 QUARTERS`, Monedas$`POST-1964 QUARTERS`)

# Prueba para ver si las medias son iguales
#t.test(Monedas$`PRE-1964 QUARTERS`)
t.test(Monedas$`PRE-1964 QUARTERS`, Monedas$`POST-1964 QUARTERS`, alternative="two.sided", mu=0, var.equal=FALSE, conf.level=0.95)
