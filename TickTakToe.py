import os
os.system('cls')
# GAME DATA
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chosenNumberTmp = 0
roundsPlayed = 0

# DEUBG
DEBUG = False

# TEXT COLORS
greenText = '\033[32m'
whiteText = '\033[00m'
redText = '\033[31m'
cyanText = '\033[96m'
yellowText = '\033[93m'

# PLAYER NAMES
if DEBUG == True:
    print(redText +  'Debug Mode active, player names skipped')
    playerOneName = 'DEBUG PLAYER 1'
    playerTwoName = 'DEBUG PLAYER 2'
else:
    playerOneName = input('' + greenText + "What is Player 1's name?: " + whiteText)
    print('' + 'Hello ' + playerOneName)
    playerTwoName = input('' + greenText + "What is Player 2's name?: " + whiteText)
    print('' + 'Hello ' + playerTwoName)

# ASK LOCATION FUNCTION
def askPlayerWhereToGo(roundsPlayed, board):
    if roundsPlayed % 2 == 0:
        chosenNumberTmp  = 0 
        print('')
        print(' ' + greenText + playerOneName +"'s turn" + whiteText)
        print('')
        isValidChoice = False
        while not isValidChoice:
            chosenNumberTmp = int(input('Choose a number to fill with an X: '))
            if 'X' in str(board[chosenNumberTmp -1]) or 'O' in str(board[chosenNumberTmp -1]):
                print('That spots taken.. please retry')
                input('Press enter to try again...')
                continue
            else:
                isValidChoice = True
        board[chosenNumberTmp - 1] =  greenText + 'X' + whiteText
        return roundsPlayed, board
    else: 
        chosenNumberTmp  = 0 
        print('')
        print(' ' + yellowText + playerTwoName +"'s turn" + whiteText)
        print('')
        isValidChoice = False
        while not isValidChoice:
            chosenNumberTmp = int(input('Choose a number to fill with an O: '))
            if 'X' in str(board[chosenNumberTmp -1]) or 'O' in str(board[chosenNumberTmp -1]):
                print('')
                print('That spots taken.. please retry')
                input('Press enter to try again...')
                print('')
                continue
            else:
                isValidChoice = True
        board[chosenNumberTmp - 1] =  yellowText + 'O' + whiteText
        return roundsPlayed, board
    

roundsPlayed += 0

while roundsPlayed <= 9:

    # PRINT BOARD
    os.system('cls')
    if DEBUG == True:
        print(redText + '==================')
        print(redText + 'DEBUG MODE ACTIVE')
        print(redText + '==================')
    print('')
    print(' ' + redText + str(board[0]) + whiteText  + '' + ' | '  + '' + redText + str(board[1]) + whiteText  + '' + ' | '  + '' + redText + str(board[2]) + whiteText + '')
    print(' ----------')
    print(' ' + redText + str(board[3]) + whiteText  + '' + ' | '  + '' + redText + str(board[4]) + whiteText  + '' + ' | '  + '' + redText + str(board[5]) + whiteText + '')
    print(' ----------')
    print(' ' + redText + str(board[6]) + whiteText  + '' + ' | '  + '' + redText + str(board[7]) + whiteText  + '' + ' | '  + '' + redText + str(board[8]) + whiteText + '')
    # CHECK WIN CONDITION
    if(board[0] == board[1] == board[2] or #TypeWin -- 1
       board[0] == board[3] == board[6] or #TypeWin -- 2
       board[0] == board[4] == board[8] or #TypeWin -- 3
       board[1] == board[4] == board[7] or #TypeWin -- 4
       board[3] == board[4] == board[5] or #TypeWin -- 5
       board[6] == board[7] == board[8] or #TypeWin -- 6
       board[2] == board[5] == board[8] or #TypeWin -- 7
       board[2] == board[4] == board[6]):  #TypeWin -- 8
        if roundsPlayed % 2 == 0:
            if DEBUG == True:
                print('')
                print( redText + 'DEBUG MODE ACTIVE: PlayerWinCondition -- ONE')
                if board[0] == board[1] == board[2]:
                    print('')
                    print(redText +  'DEBUG MODE ACTIVE: TypeWin -- 1')
                elif board[0] == board[3] == board[6]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 2')      
                elif board[0] == board[4] == board[8]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 3')   
                elif board[0] == board[4] == board[8]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 4')   
                elif board[3] == board[4] == board[5]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 5')   
                elif board[6] == board[7] == board[8]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 6')   
                elif board[2] == board[5] == board[8]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 7')   
                elif board[2] == board[4] == board[6]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 8')    
            print('')
            print(yellowText + playerTwoName + cyanText + ' Wins!' + whiteText)
            print('')
            quit()
        else:
            if DEBUG == True:
                print('')
                print( redText + 'DEBUG MODE ACTIVE: PlayerWinCondition -- Two')
                if board[0] == board[1] == board[2]:
                    print('')
                    print(redText +  'DEBUG MODE ACTIVE: TypeWin -- 1')
                elif board[0] == board[3] == board[6]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 2')      
                elif board[0] == board[4] == board[8]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 3')   
                elif board[0] == board[4] == board[8]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 4')   
                elif board[3] == board[4] == board[5]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 5')   
                elif board[6] == board[7] == board[8]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 6')   
                elif board[2] == board[5] == board[8]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 7')   
                elif board[2] == board[4] == board[6]:
                    print('')
                    print(redText + 'DEBUG MODE ACTIVE: TypeWin -- 8')  
            if DEBUG == True:
                print('DEBUG MODE ACTIVE: PlayerWinCondition -- TWO')
            print('')
            print(greenText + playerOneName + cyanText +  ' Wins!' + whiteText)
            print('')
            quit()
    askPlayerWhereToGo(roundsPlayed, board)

    roundsPlayed += 1

print('')
print(cyanText + 'Tie Game' + whiteText)
print('')
quit() 