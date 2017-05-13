#Primenumber

Inum = float(input('enter number to find out if it is prime number: '))
Vi = Inum
Vprm = 0

while (Vi > 2):
	Vi = Vi -1
	if (Inum % Vi == 0):
		Vprm = 1
#	print (Vi, Vprm)


if Vprm == 0:
	print('Your number can only be divided even, by itself and 1 and so is prime number')
else:
	print ('your number is not a prime number')
