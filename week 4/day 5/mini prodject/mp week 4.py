board = {
    "1":" ",
    "2":" ",
    "3":" ",
    "4":" ",
    "5":" ",
    "6":" ",
    "7":" ",
    "8":" ",
    "9":" "
}

board_keys = []

for key in board:
        board_keys.append(key)

def display_board(board):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])


def player_input():

    turn = "x"
    count = 0

    for i in range(10):
        display_board(board)
        print("It's your turn" + turn + "choose your move")

        move = input()

        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("That place is already chosen. \nchoose your move")
            continue


        if count >= 5:
            if board["1"] == board["2"] == board["3"] != " ":
                display_board(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif board["4"] == board["5"] == board["6"] != " ":
                display_board(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board["7"] == board["8"] == board["9"] != " ":
                display_board(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board["7"] == board["4"] == board["1"] != " ":
                display_board(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board["8"] == board["5"] == board["2"] != " ": 
                display_board(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board["9"] == board["6"] == board["3"] != " ":
                display_board(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif board["3"] == board["5"] == board["7"] != " ":
                display_board(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board["9"] == board["5"] == board["1"] != " ":
                display_board(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn == "x":
            turn = "0"
        else:
            turn = "x"


    
    
    restart = input("Do want to play Again?(y/n)")

    if restart == "y" or restart == "Y":  
        for key in board_keys:
            board[key] = " "

        player_input()    

if __name__ == "__main__":
    player_input()