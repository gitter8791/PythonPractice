#asks user for dimensions and draws a game board


def f_draw_board(lGame):
    print (' ---'*3)
    for x in range(3):
        for y in range(3):
            print('| %s  \b'%lGame[x][y],end = "")
        print('|')
    print(' ---' * 3)


def main():
    pass
# Any code you like
    #random payed game with number indicators 0,1,2 for player tick
    import random
    lGame = []
    for cX in range(3):
        lMakeRow = []
        for cY in range(3):
            lMakeRow.append(random.randint(0,2))
        #print(lMakeRow)
        lGame.append(lMakeRow)

    f_draw_board(lGame)

if __name__ == '__main__':
    main()




