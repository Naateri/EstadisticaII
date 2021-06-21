library(readxl)
data_respuestas <- read_excel("Documents/2021-1/EstadisticaII/TrabajoFinal/segunda vuelta (respuestas).xlsx")
View(data_respuestas)

summary(data_respuestas)

pedro = 0
keiko = 0
viciado = 0
pedro_M = 0
pedro_F = 0
keiko_M = 0
keiko_F = 0

candidatos = data_respuestas$`¿Cuál fue su elección en la segunda vuelta electoral?`
sexo = data_respuestas$SEXO

index = 1
for (val in candidatos){
  if (val == "Keiko Fujimori"){
    keiko = keiko + 1
    if (sexo[index] == "Masculino"){
      keiko_M = keiko_M + 1
    } else {
      keiko_F = keiko_F + 1
    }
  } else {
    if (val == "Pedro Castillo"){
      pedro = pedro + 1
      if (sexo[index] == "Masculino"){
        pedro_M = pedro_M + 1
      } else {
        pedro_F = pedro_F + 1
      }
    } else { # Viciado
      viciado = viciado + 1
    }
  }
  index = index + 1
}

total = keiko + pedro + viciado
prop_keiko = keiko / total
prop_pedro = pedro / total
prop_viciados = pedro / viciado
prop_keikoM = keiko_M / keiko
prop_keikoF = keiko_F / keiko
prop_pedroM = pedro_M / pedro
prop_pedroF = pedro_F / pedro

# Pruebas de la votacion en general

prop.test(keiko, total, p=0.67, alternative='greater') # H1: p (Electores de Keiko) > 67%
prop.test(pedro, total, p=0.21, alternative='less') # H1: p (Electores de Pedro) < 21%
prop.test(viciado, total, p=0.11, alternative='less') # H1: p (Viciados/Blanco) < 11%

prop.test(keiko_M, total, p=0.39, alternative="two.sided") # H1: p (Electores de Keiko masculinos) != 39% (del total)
prop.test(keiko_F, total, p=0.44, alternative="two.sided") # H1: p (Electoras de Keiko femeninas) != 44% (del total)
prop.test(pedro_M, total, p=0.45, alternative="two.sided") # H1: p (Electores de Pedro masculinos) != 45% (del total)
prop.test(pedro_F, total, p=0.37, alternative="two.sided") # H1: p (electoras de Pedro femeninas) != 37% (del total)

# Hay independencia entre candidato y sexo?

tabla_contingencia1 = xtabs(~`¿Cuál fue su elección en la segunda vuelta electoral?`+SEXO, data=data_respuestas)
print(tabla_contingencia1)

test1 = chisq.test(tabla_contingencia1, correct=FALSE)
print(test1)

# Hay independencia entre candidato y edad?

tabla_contingencia2 = xtabs(~`¿Cuál fue su elección en la segunda vuelta electoral?`+`Ingrese su edad`, data=data_respuestas)
print(tabla_contingencia2)

test2 = chisq.test(tabla_contingencia2, correct=FALSE)
print(test2)
