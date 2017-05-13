#random integer

import random

Irand = random.randint(0,9)
print (Irand)
Iput = int(input('Guess one digit number until you get it right:\n'))
Iround = 1

while Irand != Iput: 
	Iput = int (input ('NO! Guess again.\n'))
	Iround = Iround + 1
#	print (type(Iput))
else: 
	print ('You guessed it! Number is',Iput,'. You got it on',Iround,'. try')

