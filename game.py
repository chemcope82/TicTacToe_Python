player1 = ""
player2 = ""

def startGame():
        chooseMarker()
        gameBoard = [" "]*9
        printBoard(gameBoard)

def printInstructions():
        numPad = list(range(1,10))
        gameBoard = [str(item) for item in numPad]
        print("Instructions:\n")
        print("This is a simple game of Tic, Tac, Toe following the standard rules")
        print("To make a move at your turn, enter the number that corresponds to the box you wish to fill")
        print("(The box numbering is laid out according the the numberpad on a standard computer keyboard)\n")
        printBoard(gameBoard)
        print("\n")

        confirm = ""
        
        while confirm != "Y":
            confirm = input("Enter 'Y' to play: ").upper()
        
        if confirm == 'Y':
                startGame()

def printBoard(gameBoard):

        print(gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])
        print("--|---|--")
        print(gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
        print("--|---|--")
        print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])


def chooseMarker():
        marker = ""

        while marker != "X" and marker != "O":
                print("\n")
                marker = input("Player 1 choose X or O: ").upper()
        
        player1 = marker

        if player1 == "X":
                player2 = "O"
        else:
                player2 = "X"
        
        print("\n\n Player 1 is {}\n\n Player 2 is {}\n".format(player1, player2))

        return [player1, player2]


printInstructions()