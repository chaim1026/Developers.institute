import re

board = {
    "A1": "","B1": "0","C1": "","D1": "0","E1": "","F1": "0","G1": "","H1": "0",
    "A2": "0","B2": "","C2": "0","D2": "","E2": "0","F2": "","G2": "0","H2": "",
    "A3": "","B3": "0","C3": "","D3": "0","E3": "","F3": "0","G3": "","H3": "0",
    "A4": " ","B4": "","C4": " ","D4": "","E4": " ","F4": "","G4": " ","H4": "",
    "A5": "","B5": " ","C5": "","D5": " ","E5": "","F5": " ","G5": "","H5": " ",
    "A6": "x","B6": "","C6": "x","D6": "","E6": "x","F6": "","G6": "x","H6": "",
    "A7": "","B7": "x","C7": "","D7": "x","E7": "","F7": "x","G7": "","H7": "x",
    "A8": "x","B8": "","C8": "x","D8": "","E8": "x","F8": "","G8": "x","H8": "",
}

board_keys = []

for key in board:
    board_keys.append(key)

def display_board(board):
    print("  A B C D E F G H")
    print("  -----------------")
    print("1 |" + " " + "|" + board["B1"] + "|" + " " + "|" + board["D1"] + "|" + " " + "|" + board["F1"] + "|" + " " + "|" + board["H1"] + "|")
    print("  -----------------")
    print("2 |" + board["A2"] + "|" + " " + "|" + board["C2"] + "|" + " " + "|" + board["E2"] + "|" + " " + "|" + board["G2"] + "|" + " " + "|")
    print("  -----------------")
    print("3 |" + " " + "|" + board["B3"] + "|" + " " + "|" + board["D3"] + "|" + " " + "|" + board["F3"] + "|" + " " + "|" + board["H3"] + "|")
    print("  -----------------")
    print("4 |" + board["A4"] + "|" + " " + "|" + board["C4"] + "|" + " " + "|" + board["E4"] + "|" + " " + "|" + board["G4"] + "|" + " " + "|")
    print("  -----------------")
    print("5 |" + " " + "|" + board["B5"] + "|" + " " + "|" + board["D5"] + "|" + " " + "|" + board["F5"] + "|" + " " + "|" + board["H5"] + "|")
    print("  -----------------")
    print("6 |" + board["A6"] + "|" + " " + "|" + board["C6"] + "|" + " " + "|" + board["E6"] + "|" + " " + "|" + board["G6"] + "|" + " " + "|")
    print("  -----------------")
    print("7 |" + " " + "|" + board["B7"] + "|" + " " + "|" + board["D7"] + "|" + " " + "|" + board["F7"] + "|" + " " + "|" + board["H7"] + "|")
    print("  -----------------")
    print("8 |" + board["A8"] + "|" + " " + "|" + board["C8"] + "|" + " " + "|" + board["E8"] + "|" + " " + "|" + board["G8"] + "|" + " " + "|")
    print("  -----------------")
    
def player_input():

    turn = "0"
    player_0 = 12
    player_x = 12

    while player_0 != 0 or player_x != 0:
        display_board(board)
        position = input("It's your turn " + turn + " choose the position of the piece you would like to move:\n").upper()

        while board[position] != turn:
            position = input("You dont have a piece there please choose again:\n").upper()
        
        board[position] = " "

        move = input("Where would you like that piece to move:\n").upper()

        if turn != "x" and int(re.findall("[12345678]",position)[0]) - int(re.findall("[12345678]",move)[0]) > 0 or turn != "0" and int(re.findall("[12345678]",position)[0]) - int(re.findall("[12345678]",move)[0]) < 0:
            move = input("you are not allowed to move backwords unless you are a king please choose again:\n").upper()

        if turn == "0" and int(re.findall("[12345678]",position)[0]) - int(re.findall("[12345678]",move)[0]) == -2:
            if ord(re.findall("[A-H]", position)[0]) - ord(re.findall("[A-H]", move)[0]) == 2:
                if board[chr(ord(re.findall("[A-H]", move)[0]) + 1) + (str(int(re.findall("[12345678]",position)[0]) + 1))] == "x":
                    board[chr(ord(re.findall("[A-H]", move)[0]) + 1) + (str(int(re.findall("[12345678]",position)[0]) + 1))] = " "
                    player_x -= 1
                else:
                    move = input("You can only move 2 spaces to jump other players piece chose another move:\n")
            elif ord(re.findall("[A-H]", position)[0]) - ord(re.findall("[A-H]", move)[0]) == -2:
                if board[chr(ord(re.findall("[A-H]", move)[0]) - 1) + (str(int(re.findall("[12345678]",position)[0]) + 1))] == "x":
                    board[chr(ord(re.findall("[A-H]", move)[0]) - 1) + (str(int(re.findall("[12345678]",position)[0]) + 1))] = " "
                    player_x -= 1
                else:
                    move = input("You can only move 2 spaces to jump other players piece chose another move:\n")
        elif turn == "x" and int(re.findall("[12345678]",position)[0]) - int(re.findall("[12345678]",move)[0]) == 2:
            if ord(re.findall("[A-H]", position)[0]) - ord(re.findall("[A-H]", move)[0]) == 2:
                if board[chr(ord(re.findall("[A-H]", move)[0]) + 1) + (str(int(re.findall("[12345678]",position)[0]) - 1))] == "0":
                    board[chr(ord(re.findall("[A-H]", move)[0]) + 1) + (str(int(re.findall("[12345678]",position)[0]) - 1))] = " "
                    player_0 -= 1
                else:
                    move = input("You can only move 2 spaces to jump other players piece chose another move:\n")
            elif ord(re.findall("[A-H]", position)[0]) - ord(re.findall("[A-H]", move)[0]) == -2:
                if board[chr(ord(re.findall("[A-H]", move)[0]) - 1) + (str(int(re.findall("[12345678]",position)[0]) - 1))] == "0":
                    board[chr(ord(re.findall("[A-H]", move)[0]) - 1) + (str(int(re.findall("[12345678]",position)[0]) - 1))] = " "
                    player_0 -= 1
                else:
                    move = input("You can only move 2 spaces to jump other players piece chose another move:\n")


        while board[move] != " ":
            move = input("That place is already chosen or place is not a valid move please chose again:\n").upper()
            
        board[move] = turn

        if turn == "x":
            turn = "0"
        else:
            turn = "x" 