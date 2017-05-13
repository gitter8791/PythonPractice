#pick even numbers from the list

La = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 
"""
for i in La:
	if i % 2 == 0:
		print (i)
"""

Lb = [i for i in La if i % 2 == 0]
print (Lb)