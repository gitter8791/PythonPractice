

def f_take_tic(playerx, lGame):
    print('Turn, player', playerx)
    user_input = input('Coordinates: ')
    user_input = user_input.split(' ')
    iX = int(user_input[0])
    iY = int(user_input[1])

    if (iX < 0 or iY < 0) or (iX > 2 or iY > 2) or lGame[iX][iY] != '-':
        print ('values out of boundaries')
    if playerx == 1:
        lGame[iX][iY] = 'x'
        playerx = 2
    elif playerx == 2:
        lGame[iX][iY] = 'o'
        playerx = 1

    return (lGame)




def main():
    pass
      # Any code you like
    lGame = [['-','-','-'] for i in range(3)]
    playerx = 1

    print('Input coordinates. 0,0 is first slot. Please enter the indices separated by space')

    while f_take_tic(playerx, lGame) != 0:

        print(lGame)


if __name__ == '__main__':
    main()
