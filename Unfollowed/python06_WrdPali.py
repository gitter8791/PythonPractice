#Palindome. Printing extra letter with space??

"""
Spali = input('Try palindrome: ')
Salip = Spali[::-1]

if Spali == Salip: print (Salip,'This word is a palindrome')
else: print (Spali, 'is not a palindrome')
"""

def revWord(Sword):
	xWord = ''
	for i in range(len(Sword)):
		xWord += Sword[len(Sword)-1-i]
		return xWord
		
Sword = input('Give word:\n')
xWord = revWord(Sword)

print (Sword,xWord)