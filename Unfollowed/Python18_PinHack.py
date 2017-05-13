#Program asks user for 4 digit pin and tells how many is right until all of them are
import random
import string

#random pin to be guessed
vPin_hard = list(''.join(random.SystemRandom().choice(string.digits) for _ in range (4)))
#print ('[%s]' % ''.join(map(str, vPin_hard)))

#ask for pin
vPin = list(input('guess 4 digit pin, until you get it right: '))
#print('[%s]' % ''.join(map(str, vPin)))

#compare pins
def fCompPins(vPin, vPin_hard):
    cRightGuess = 0
    if len(vPin) == 4:
        if cRightGuess != 4:
            for i in range(4):
                if vPin[i] == vPin_hard[i]:
                    cRightGuess += 1
                    if cRightGuess == 4:
                        return (True)
            print('you got',cRightGuess,'digits right',)

    else:
        print('You must enter 4 digit pin')
        return(False)

while fCompPins(vPin, vPin_hard) != True:
    vPin = input('guess again: ')

print('game over!')
