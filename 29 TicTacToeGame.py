#Combine 3 functions to complete the game

from TTT_UserInput import f_take_tic
from TTT_SeekWinner import f_winner
from TTT_DrawGame import f_draw_board


def main():
    pass
    lGame = [['-','-','-'] for i in range(3)]
    playerx = 1
    vWin1 = 0
    vWin2 = 0

    while f_take_tic(playerx, lGame) != 0 and f_winner(lGame, vWin1, vWin2) == 0:
        if playerx == 1:
            playerx = 2
        else:
            playerx = 1
        f_draw_board(lGame)


    f_draw_board(lGame)

if __name__ == '__main__':
    main()