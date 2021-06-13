def statistic(o, e):
	summ = 0
	num = 0
	den = 0
	
	for i in range(len(o)):
		num = (o[i]-e[i])
		num = pow(num, 2)
		den = e[i]
		res = num/den
		summ += res
	
	return summ
	
o = [35, 25, 13, 12]
e = [29.16, 31.20, 16.66, 7.99]

print(statistic(o,e))
