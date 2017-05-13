#Function eats a list and return another one without dublicates

Lin = [1,1,2,3,3,4,5,5]
Lout = []


def gasF (Lin, Lout):
	for i in Lin:
		if i not in Lout:
			Lout.append (i)
	return Lout

print (gasF (Lin, Lout))
