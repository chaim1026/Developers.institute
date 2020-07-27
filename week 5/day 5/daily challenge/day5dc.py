import re

class Checkers():
    def __init__(self):
        self.board = {
            "A1": "","B1": "0","C1": "","D1": "0","E1": "","F1": "0","G1": "","H1": "0",
            "A2": "0","B2": "","C2": "0","D2": "","E2": "0","F2": "","G2": "0","H2": "",
            "A3": "","B3": "0","C3": "","D3": "0","E3": "","F3": "0","G3": "","H3": "0",
            "A4": " ","B4": "","C4": " ","D4": "","E4": " ","F4": "","G4": " ","H4": "",
            "A5": "","B5": " ","C5": "","D5": " ","E5": "","F5": " ","G5": "","H5": " ",
            "A6": "x","B6": "","C6": "x","D6": "","E6": "x","F6": "","G6": "x","H6": "",
            "A7": "","B7": "x","C7": "","D7": "x","E7": "","F7": "x","G7": "","H7": "x",
            "A8": "x","B8": "","C8": "x","D8": "","E8": "x","F8": "","G8": "x","H8": "",
        }
        self.board_keys = []
        for key in self.board:
            self.board_keys.append(key)

    def display_board(self,board):
        print("  A B C D E F G H")
        print("  -----------------")
        print("1 |" + " " + "|" + self.board["B1"] + "|" + " " + "|" + self.board["D1"] + "|" + " " + "|" + self.board["F1"] + "|" + " " + "|" + self.board["H1"] + "|")
        print("  -----------------")
        print("2 |" + self.board["A2"] + "|" + " " + "|" + self.board["C2"] + "|" + " " + "|" + self.board["E2"] + "|" + " " + "|" + self.board["G2"] + "|" + " " + "|")
        print("  -----------------")
        print("3 |" + " " + "|" + self.board["B3"] + "|" + " " + "|" + self.board["D3"] + "|" + " " + "|" + self.board["F3"] + "|" + " " + "|" + self.board["H3"] + "|")
        print("  -----------------")
        print("4 |" + self.board["A4"] + "|" + " " + "|" + self.board["C4"] + "|" + " " + "|" + self.board["E4"] + "|" + " " + "|" + self.board["G4"] + "|" + " " + "|")
        print("  -----------------")
        print("5 |" + " " + "|" + self.board["B5"] + "|" + " " + "|" + self.board["D5"] + "|" + " " + "|" + self.board["F5"] + "|" + " " + "|" + self.board["H5"] + "|")
        print("  -----------------")
        print("6 |" + self.board["A6"] + "|" + " " + "|" + self.board["C6"] + "|" + " " + "|" + self.board["E6"] + "|" + " " + "|" + self.board["G6"] + "|" + " " + "|")
        print("  -----------------")
        print("7 |" + " " + "|" + self.board["B7"] + "|" + " " + "|" + self.board["D7"] + "|" + " " + "|" + self.board["F7"] + "|" + " " + "|" + self.board["H7"] + "|")
        print("  -----------------")
        print("8 |" + self.board["A8"] + "|" + " " + "|" + self.board["C8"] + "|" + " " + "|" + self.board["E8"] + "|" + " " + "|" + self.board["G8"] + "|" + " " + "|")
        print("  -----------------")
        
    def player_input(self):

        turn = "0"
        player_0 = 12
        player_x = 12

        while player_0 != 0 or player_x != 0:
            self.display_board(self.board)
            position = input("It's your turn " + turn + " choose the position of the piece you would like to move:\n").upper()

            while self.board[position] != turn and self.board[position] != "K" and self.board[position] != "R" :
                position = input("You dont have a piece there please choose again:\n").upper()
            
            self.board[position] = " "

            move = input("Where would you like that piece to move:\n").upper()
            
            # go back and make sure king can go backwards
            if self.board[position] == "R" or self.board[position] == "K":
                break
            elif turn != "x" and int(re.findall("[12345678]",position)[0]) - int(re.findall("[12345678]",move)[0]) > 0 or turn != "0" and int(re.findall("[12345678]",position)[0]) - int(re.findall("[12345678]",move)[0]) < 0:
                move = input("you are not allowed to move backwords unless you are a king please choose again:\n").upper()
                  
            if turn == "0" and int(re.findall("[12345678]",position)[0]) - int(re.findall("[12345678]",move)[0]) == -2:
                if ord(re.findall("[A-H]", position)[0]) - ord(re.findall("[A-H]", move)[0]) == 2:
                    if self.board[chr(ord(re.findall("[A-H]", move)[0]) + 1) + (str(int(re.findall("[12345678]",position)[0]) + 1))] == "x":
                        self.board[chr(ord(re.findall("[A-H]", move)[0]) + 1) + (str(int(re.findall("[12345678]",position)[0]) + 1))] = " "
                        player_x -= 1
                    else:
                        move = input("You can only move 2 spaces to jump other players piece chose another move:\n")
                elif ord(re.findall("[A-H]", position)[0]) - ord(re.findall("[A-H]", move)[0]) == -2:
                    if self.board[chr(ord(re.findall("[A-H]", move)[0]) - 1) + (str(int(re.findall("[12345678]",position)[0]) + 1))] == "x":
                        self.board[chr(ord(re.findall("[A-H]", move)[0]) - 1) + (str(int(re.findall("[12345678]",position)[0]) + 1))] = " "
                        player_x -= 1
                    else:
                        move = input("You can only move 2 spaces to jump other players piece chose another move:\n")
            elif turn == "x" and int(re.findall("[12345678]",position)[0]) - int(re.findall("[12345678]",move)[0]) == 2:
                if ord(re.findall("[A-H]", position)[0]) - ord(re.findall("[A-H]", move)[0]) == 2:
                    if self.board[chr(ord(re.findall("[A-H]", move)[0]) + 1) + (str(int(re.findall("[12345678]",position)[0]) - 1))] == "0":
                        self.board[chr(ord(re.findall("[A-H]", move)[0]) + 1) + (str(int(re.findall("[12345678]",position)[0]) - 1))] = " "
                        player_0 -= 1
                    else:
                        move = input("You can only move 2 spaces to jump other players piece chose another move:\n")
                elif ord(re.findall("[A-H]", position)[0]) - ord(re.findall("[A-H]", move)[0]) == -2:
                    if self.board[chr(ord(re.findall("[A-H]", move)[0]) - 1) + (str(int(re.findall("[12345678]",position)[0]) - 1))] == "0":
                        self.board[chr(ord(re.findall("[A-H]", move)[0]) - 1) + (str(int(re.findall("[12345678]",position)[0]) - 1))] = " "
                        player_0 -= 1
                    else:
                        move = input("You can only move 2 spaces to jump other players piece chose another move:\n")

            while self.board[move] != " ":
                move = input("That place is already chosen or place is not a valid move please chose again:\n").upper()

            if turn == "0" and move in ["A8", "C8", "E8", "G8"]:
                print("You are now a king")
                self.board[move] = "K"
            elif turn == "x" and move in ["B1", "D1", "F1", "H1"]:
                print("You are now a king")
                self.board[move] = "R"
            elif self.board[position] == "K":
                self.board[move] = "K"           
            elif self.board[position] == "R":
                self.board[move] = "R"            
            else:
                self.board[move] = turn


            if turn == "x":
                turn = "0"
            else:
                turn = "x" 