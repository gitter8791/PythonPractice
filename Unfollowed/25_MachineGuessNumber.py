'''
You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, 
will say whether it is too high, too low, or your number.
'''

print('Think of a number 1-100. Machine will try to guess it and you tell it, low or high. ')
vGuess = 50
vMax = 101
vMin = 1
sAlt = ""
iCount = 0

while sAlt != 'r':
    print('my guess is : ', vGuess)
    iCount += 1
    sAlt = input('is it high, low or right? ')
    if sAlt == 'h':
        vMax = vGuess
        vGuess = int((vMax+vMin)/2)
    elif sAlt == 'l':
        vMin = vGuess
        vGuess = int(vGuess + (vMax-vMin)/2)
    elif sAlt == 'r':
        print('YOU GOT IT!')
    else:
        print('enter valid choicee')

print (iCount)