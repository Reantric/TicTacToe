def tictactoe():
    board = ''; counter = 1; endi = 'st'; countX = 1; countY = 1; xVar = 0; yVar = 0; gameWon = False
    for x in range(-1,6):
            if x % 2 == 0:
                board += '|      ' *4
                board += '\n|      |      |      |'
            else:
                board += ' _____ ' * 3
            board += '\n'
    print(board)
    posDict = {3:216,2:209,1:202,6:142,5:135,4:128,9:68,8:61,7:54}
    listCheck = []
    while not gameWon and len(listCheck) < 9:
        if countX == 1 or countY == 1:
            pass
        elif countX == 2 or countY == 2:
            endi = 'nd'
        elif countX == 3 or countY == 3:
            endi = 'rd'
        else:
            endi = 'th'
        if counter % 2 == 1:
            xVar = int(input(f'Where would you like to place your {countX}{endi} X? '))
            countX += 1
        else:
            yVar = int(input(f'Where would you like to place your {countY}{endi} O? '))
            countY += 1
        board = list(board)
        listCheck = list(listCheck)
        try:
            if posDict[xVar] in listCheck and counter % 2 == 1:
                countX -= 1; counter -= 2
                print(''.join(board))
                continue
        except KeyError:
            pass
        try:
            if posDict[yVar] in listCheck and counter % 2 == 0:
                countY -= 1; counter -= 2
                print(''.join(board))
                continue
        except KeyError:
            pass
        for foonum in range(1,10):
            if xVar > 9:
                print('Please enter an X value in the correct range!')
                countX -= 1; counter -= 1
                break
            elif yVar > 9:
                print('Please enter a Y value in the correct range!')
                countY -= 1; counter -= 1
                break
            numbare = posDict[foonum]
            if xVar == foonum or yVar == foonum:
                if xVar == yVar:
                    print('Illegal!')
                    if counter % 2 == 0:
                        countY -= 1; counter -= 1
                    else:
                        countX -= 1; counter -= 1
                    continue
                elif xVar == foonum:
                    board[numbare] = 'X'
                    listCheck = list(listCheck)
                    listCheck.append(posDict[xVar])
                    listCheck = set(listCheck)
                elif yVar == foonum:
                    board[numbare] = 'O'
                    listCheck = list(listCheck)
                    listCheck.append(posDict[yVar])
                    listCheck = set(listCheck)
            else:
                pass
        board = ''.join(board)
        print(board)
        counter += 1
        def winCheck(mark):
            return ((board[7] ==  board[8] ==  board[9] == mark) or
            (board[posDict[4]] == board[posDict[5]] == board[posDict[6]] == mark) or
            (board[posDict[1]] == board[posDict[2]] == board[posDict[3]] == mark) or
            (board[posDict[7]] == board[posDict[4]] == board[posDict[1]] == mark) or
            (board[posDict[8]] == board[posDict[5]] == board[posDict[2]] == mark) or
            (board[posDict[9]] == board[posDict[6]] == board[posDict[3]] == mark) or
            (board[posDict[7]] == board[posDict[5]] == board[posDict[3]] == mark) or
            (board[posDict[9]] == board[posDict[5]] == board[posDict[1]] == mark))
        if winCheck('X') or winCheck('O'):
            break
    if len(listCheck) == 9:
        print('Good game, it was a tie!')
    elif counter % 2 == 0:
        print('Good game, X won!')
    else:
        print('Good game, O won!')
    replay = input('Want to play again? Yes if you do, No if you do not! (Note, anything other than yes will be regarded as no) ')
    if ''.join(replay).lower().startswith('y'):
        tictactoe()
tictactoe()
