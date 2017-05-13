#Function reverses word order in a sentence (string)


def revwF(Swrds):
	Srwrds = Swrds.split()
	Srwrds.reverse()
	Swyoda = ''.join(Srwrds)
	#print(Swyoda)
	return(Swyoda)

Swordin = str(input('write a sentence: '))
print(revwF(Swordin))


