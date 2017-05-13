#tictactoe matrix will generate a played game and determine the winner
import random

#rows

def f_winner(lGame, vWin1, vWin2):
    vWinner = 'none'
    lDiag1 = []
    lDiag2 = []

    for iX in range(3):
        lRow = []
        lCol = []
        for iY in range(3):
            lRow.append(lGame[iX][iY])
            lCol.append(lGame[iY][iX])
            if (iX == iY):
                lDiag1.append(lGame[iX][iY])
            if (iX == iY == 1) or (iX == 0 and 2 == iY) or (2 == iX and iY == 0):
                lDiag2.append(lGame[iX][iY])
        if lRow[0] == lRow [1] == lRow[2] == 'x':
            vWin1 = 1
        if lRow[0] == lRow[1] == lRow[2] == 'o':
            vWin2 = 1
        if lCol[0] == lCol [1] == lCol[2] == 'x':
            vWin1 = 1
        if lCol[0] == lCol[1] == lCol[2] == 'o':
            vWin2 = 1
    if lDiag1[0] == lDiag1 [1] == lDiag1[2] == 'x':
        vWin1 = 1
    if lDiag1[0] == lDiag1[1] == lDiag1[2] == 'o':
        vWin2 = 1
    if lDiag2[0] == lDiag2 [1] == lDiag2[2] == 'x':
        vWin1 = 1
    if lDiag2[0] == lDiag2[1] == lDiag2[2] == 'o':
        vWin2 = 1



    if vWin1 == vWin2:
        print('Game On!')
        vWinner = 0
    elif vWin1 == 1:
        vWinner = 1
        print('Player one wins')
    elif vWin2 == 1:
        vWinner = 2
        print('Player two wins')
    else:
        print('you both suck')
        vWinner = 0

    return (vWinner)

#Main function. not executed when above function called from another segment
def main():
    pass
    lGame = []
    vWin1 = 0
    vWin2 = 0

    #random exes and circles
    for cI in range(3):
        lMakeRow = []
        for cII in range(3):
            lMakeRow.append(random.choice('xo'))
        print(lMakeRow)
        lGame.append(lMakeRow)

    f_winner(lGame, vWin1, vWin2)
    print(lGame)

if __name__ == '__main__':
    main()
