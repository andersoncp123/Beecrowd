cont = 0
a = -0.2

while(cont <= 10):
	a += 0.2
	print("I={:g} J={:g}".format(a, a+1))
	print("I={:g} J={:g}".format(a, a+2))
	print("I={:g} J={:g}".format(a, a+3))
	cont += 1
