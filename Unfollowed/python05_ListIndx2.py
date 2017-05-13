#List

La = [1, 1, 2, 3, 5, 8, 9]
Lb = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
Vcomp1 = -1
Vcomp2 = -1


for i in La:
	if i != Vcomp1:
		Vcomp1 = i
		for j in Lb:
			if j != Vcomp2 and i == j:
				Vcomp2 = j
				print (i)
			else: 
				Vcomp2 = -1
	else:
		Vcomp1 = -1