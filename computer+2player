from colorama import Fore, Style
from random import choice
from time import sleep

posDict = {1: 202, 2: 209, 3: 216, 4: 128, 5: 135, 6: 142, 7: 54, 8: 61, 9: 68}
players = ['X', 'O']
print(Fore.RED + "Copyright © 2018 The Schram Foundation. All rights reserved." + Style.RESET_ALL)

def display_board():
    global board
    board = ''
    for x in range(-1, 6):
        if x % 2 == 0:
            board += '|      ' * 4 + '\n|      |      |      |'
        else:
            board += ' _____ ' * 3
        board += '\n'
    return board

def demo():
    demoBoard = list(display_board())
    for i, k in enumerate(posDict.keys()):
        demoBoard[posDict[k]] = Fore.CYAN + f'{i + 1}' + Style.RESET_ALL
    return ''.join(demoBoard)

def errorHandle(i):
    while True:
        try:
            x = int(input(Fore.YELLOW + f'Where would you like to place your {players[i]}? ' + Style.RESET_ALL))
            if x > 9:
                print(Fore.LIGHTRED_EX + 'Please input an number between 1 and 9! ' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.LIGHTRED_EX + "Please input a number between 1 and 9! " + Style.RESET_ALL)
            continue
        break
    return x

def chooseEnemy():
    cPlay = input(
        Fore.BLUE + 'Would you like to play the computer (c) or another person (p)? ' + Style.RESET_ALL)
    return 'j' if cPlay.upper().startswith('J') else cPlay.upper().startswith('C')

def winCheck(board, mark):
    return (board[posDict[7]] == board[posDict[8]] == board[posDict[9]] == mark or
            (board[posDict[4]] == board[posDict[5]] == board[posDict[6]] == mark) or
            (board[posDict[1]] == board[posDict[2]] == board[posDict[3]] == mark) or
            (board[posDict[7]] == board[posDict[4]] == board[posDict[1]] == mark) or
            (board[posDict[8]] == board[posDict[5]] == board[posDict[2]] == mark) or
            (board[posDict[9]] == board[posDict[6]] == board[posDict[3]] == mark) or
            (board[posDict[7]] == board[posDict[5]] == board[posDict[3]] == mark) or
            (board[posDict[9]] == board[posDict[5]] == board[posDict[1]] == mark))

def isSpaceEmpty(board,pos):
    return board[posDict[pos]] == ' '

def computerMove(board,firstMove):
    simBoard = list(board)
    print(Fore.YELLOW + "Computer is thinking..." + Style.RESET_ALL)
    sleep(1)
    for j in range(1, 10):
        if isSpaceEmpty(board,j):
            simBoard[posDict[j]] = '{}'.format(Fore.GREEN + 'O' + Style.RESET_ALL if firstMove else Fore.RED + 'X' + Style.RESET_ALL)
            if winCheck(simBoard, '{}'.format(Fore.GREEN + 'O' + Style.RESET_ALL if firstMove else Fore.RED + 'X' + Style.RESET_ALL)):
                return j  # as mark
            simBoard[posDict[j]] = ' '

    for j in range(1, 10):
        if isSpaceEmpty(board,j):
            simBoard[posDict[j]] = '{}'.format(Fore.RED + 'X' + Style.RESET_ALL if firstMove else Fore.GREEN + 'O' + Style.RESET_ALL)
            if winCheck(simBoard, '{}'.format(Fore.RED + 'X' + Style.RESET_ALL if firstMove else Fore.GREEN + 'O' + Style.RESET_ALL)):
                return j
            simBoard[posDict[j]] = ' '
    if isSpaceEmpty(board,5): return 5

    for j in 1,3,7,9:
        if isSpaceEmpty(board,j):
            return j

    for j in 2,4,6,8:
        if isSpaceEmpty(board,j):
            return j

def displayPrompt(i=0):
    return errorHandle(i)

def midGame(cPlay, board, autoplay, mF=choice((0,1))):
    gameWon = False
    def move(j=0):
        if not j:
            if not winCheck(board, Fore.GREEN + 'O' + Style.RESET_ALL):
                mark = displayPrompt(False)
                while mark in listCheck:
                    mark = displayPrompt(False)
                listCheck.append(mark)
                board[posDict[mark]] = Fore.RED + 'X' + Style.RESET_ALL
                print(''.join(board))
                return False
            return True
        if not winCheck(board, Fore.RED + 'X' + Style.RESET_ALL) and not winCheck(board,
                                                                                  Fore.GREEN + 'O' + Style.RESET_ALL):
            mark = displayPrompt(1)
            while mark in listCheck:
                mark = displayPrompt(1)
            listCheck.append(mark)
            board[posDict[mark]] = Fore.GREEN + 'O' + Style.RESET_ALL
            print(''.join(board))
            return False
        print(
            Fore.MAGENTA + "gg my dude ez win for {}".format('O' if len(listCheck) % 2 == 0 else 'X') + Style.RESET_ALL)
        return True

    board = list(board)
    listCheck = []

    if cPlay:
        print(Fore.LIGHTRED_EX + "Choosing who goes first..." + Style.RESET_ALL)
        sleep(1.5)
        print(''.join(board))
        while not winCheck(board,Fore.GREEN + 'O' + Style.RESET_ALL):
            if cPlay == 'j':
                mark = computerMove(board, False)
            elif mF:
                mark = computerMove(board, False)
            else:
                mark = displayPrompt(0)
            while mark in listCheck:
              mark = displayPrompt(0)
            board[posDict[mark]] = Fore.RED + 'X' + Style.RESET_ALL
            listCheck.append(mark)
            print(''.join(board))
            if winCheck(board,'{}'.format(Fore.GREEN + 'O' + Style.RESET_ALL if mF else Fore.RED + 'X' + Style.RESET_ALL)):
                print(Fore.LIGHTRED_EX + "Congratulations, you won!" + Style.RESET_ALL)
                break
            if winCheck(board,'{}'.format(Fore.GREEN + 'X' + Style.RESET_ALL if mF else Fore.RED + 'O' + Style.RESET_ALL)):
                print(Fore.LIGHTMAGENTA_EX + "Looks like the computer won!" + Style.RESET_ALL)
                break
            if len(listCheck) == 9: print(Fore.BLUE + "Tie!" + Style.RESET_ALL); break
            if cPlay == 'j':
                mark = computerMove(board, False)
            elif mF:
                mark = displayPrompt(1)
            else:
                mark = computerMove(board, False)
            while mark in listCheck:
              mark = displayPrompt(1)
            board[posDict[mark]] = Fore.GREEN + 'O' + Style.RESET_ALL
            listCheck.append(mark)
            print(''.join(board))

    else:
        print(''.join(board))
        while not gameWon:
            move(False)
            if len(listCheck) == 9:
                if winCheck(board, Fore.RED + 'X' + Style.RESET_ALL): print("Nice last move win!")
                break
            gameWon = move(1)
    while not autoplay:
        replay = input(Fore.CYAN + "Would you like to play again my dude? (a) for autoplay! " + Style.RESET_ALL)
        return 'a' if replay.upper().startswith('A') else replay.upper().startswith('Y')
    return True
def highlightWin(wM):
    if wM:
        pass
    return None

def renew(replay=True):
    while replay:
        print(demo())
        cPlay = chooseEnemy()
        x = True if replay == 'a' else False
        replay = midGame(cPlay, board,x)
    else:
        print(Fore.YELLOW + "Well that's gg")

renew()
