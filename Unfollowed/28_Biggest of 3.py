#Takes 3 numbers and defines the largest one without useing max function

fNum1 = input('give me a number')
fNum2 = input('Give another')
fNum3 = input('Give yet another')

fNumMax = fNum1

if fNum2 > fNumMax:
    fNumMax = fNum2

if fNum3 > fNumMax:
    fNumMax = fNum3

print (fNumMax)