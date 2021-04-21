# Ejercicio 5, M&MS
# Probar que el 24% de dulces son azules

summary(MM) # Da un resumen estadistico

num_blues = length(MM$BLUE)
total = length(MM$RED)+length(MM$ORANGE)+length(MM$YELLOW)+length(MM$BROWN)+length(MM$BLUE)+length(MM$GREEN)
prop_blues <- num_blues/total

prop.test(num_blues, total, p=0.24, alternative='two.sided') 
# primer parametro: x, cantidad de la proporcion
# segundo parametro: n, cantidad total
# p=: cantidad que se busca en la hipotesis
# alternative: cual es H1 (en este caso, H1 > 0.24)