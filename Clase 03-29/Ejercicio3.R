# Coin Weights
# H0: mu = 5.670

objective_mean=5.670 
estadistico1<-t.test(Coin$`POST-1964 QUARTERS`, mu=objective_mean)
estadistico2<-t.test(Coin$`POST-1964 QUARTERS`, mu=objective_mean,conf.level=0.05,alternative='two.sided')
# Lo mismo que arriba, pero con todos los parametros, varia nivel de significancia
#estadistico1
estadistico2