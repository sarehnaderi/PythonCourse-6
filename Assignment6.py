from pyfiglet import Figlet

def show():
    for row in game_board: 
        for cel in row:
            print(cel,end=" ")
        print() 
        
def check_draw(): 
    if game_board[0][0]!="-" and game_board[0][1]!="-" and game_board[0][2]!="-" and game_board[1][0]!="-" and game_board[1][1]!="-" and game_board[1][2]!="-" and game_board[2][0]!="-" and game_board[2][1]!="-" and game_board[2][2]!="-": 
        print("Draw -> No Winner") 
        quit()
    
def check_game1():
# Possibilities for player 1 to score:
# Horizontally
    if game_board[0][0]=="X" and game_board[0][1]=="X" and game_board[0][2]=="X":
        print("Score for player1!!")
        return True
    elif game_board[1][0]=="X" and game_board[1][1]=="X" and game_board[1][2]=="X":
        print("Score for player1!!")
        return True
    elif game_board[2][0]=="X" and game_board[2][1]=="X" and game_board[2][2]=="X":
        print("Score for player1!!")
        return True
# Vertically
    elif game_board[0][0]=="X" and game_board[1][0]=="X" and game_board[2][0]=="X":
        print("Score for player1!!")
        return True
    elif game_board[0][1]=="X" and game_board[1][1]=="X" and game_board[2][1]=="X":
        print("Score for player1!!")
        return True
    elif game_board[0][2]=="X" and game_board[1][2]=="X" and game_board[2][2]=="X":
        print("Score for player1!!")
        return True
# Diagonally
    elif game_board[0][2]=="X" and game_board[1][1]=="X" and game_board[2][0]=="X":
        print("Score for player1!!")
        return True
    elif game_board[0][0]=="X" and game_board[1][1]=="X" and game_board[2][2]=="X":
        print("Score for player1!!")
        return True
    return False
# Possibilities for player 2 to score:
# Horizontally
def check_game2():
    if game_board[0][0]=="O" and game_board[0][1]=="O" and game_board[0][2]=="O":
        print("Score for player2!!")
        return True
    elif game_board[1][0]=="O" and game_board[1][1]=="O" and game_board[1][2]=="O":
        print("Score for player2!!")
        return True
    elif game_board[2][0]=="O" and game_board[2][1]=="O" and game_board[2][2]=="O":
        print("Score for player2!!")
        return True
# Vertically
    elif game_board[0][0]=="O" and game_board[1][0]=="O" and game_board[2][0]=="O":
        print("Score for player2!!")
        return True
    elif game_board[0][1]=="O" and game_board[1][1]=="O" and game_board[2][1]=="O":
        print("Score for player2!!")
        return True
    elif game_board[0][2]=="O" and game_board[1][2]=="O" and game_board[2][2]=="O":
        print("Score for player2!!")
        return True
# Diagonally
    elif game_board[0][2]=="O" and game_board[1][1]=="O" and game_board[2][0]=="O":
        print("Score for player2!!")
        return True
    elif game_board[0][0]=="O" and game_board[1][1]=="O" and game_board[2][2]=="O":
        print("Score for player2!!")
        return True
    return False

f = Figlet(font='slant')
print(f.renderText('tic tac toe'))

game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]

show()
while True:
    #player1
    print("player1")
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "-": 
                game_board[row][col] = "X" 
                show()
                check_game1()
                check_draw()
                break        
            else:
                print("Try another position!")
        else:
            print("Erroe! Enter a number from 0,1,2.")
    
    #player2
    print("player2")
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if 0<= row <=2 and 0 <= col <= 2: 
            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                show()
                check_game2()
                check_draw()
                break    
            else:
                print("Try another position!")
        else:
            print("Erroe! Enter a number from 0,1,2.")
