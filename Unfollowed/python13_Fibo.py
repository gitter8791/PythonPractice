#Fibonacci generator

def fibF():
	Lfib = []
	Iamnt = int(input ('Give amount of Fibonacci numbers you wish to list. '))
	VnumF = 0
	VnumI = 1
	while (Iamnt > 0):
		VnumO = VnumF
		VnumF = VnumF + VnumI
		VnumI = VnumO
		Iamnt -= 1
		Lfib.append (VnumF)
	print (Lfib)
	
fibF()