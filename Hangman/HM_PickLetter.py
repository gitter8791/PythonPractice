
def f_take_guess(sWordUK):
    lWordPrint = ['_' for i in range(len(sWordUK))]
    sWordUK = sWordUK.upper()
    lLettersMissed =[]

    while '_' in lWordPrint:
        sLetter = input('Input letter: ').upper()

        for iX in range(len(lWordPrint)):
            if sLetter == sWordUK[iX]:
                lWordPrint[iX] = sLetter

        if sLetter not in (lLettersMissed and lWordPrint):
            lLettersMissed.append(sLetter)

        print('\n'*100)
        for iX in range(len(lWordPrint)):
            print(' ', lWordPrint[iX], end='')
        print('\n')
        print('tried: ', lLettersMissed)


def main():
   pass
   #sWordUK = ['D', 'e', 'm', 'o', 'W', 'o', 'r', 'd']
   sWordUK = 'DemoWord'
   f_take_guess(sWordUK)

if __name__ == '__main__':
   main()