import random

##############################################################################

print("""\n
Let's play TicTacToe!\n
Game board     Number Tiles\n
- | - | -       1 | 2 | 3 
- | - | -       4 | 5 | 6 
- | - | -       7 | 8 | 9
\nRemember the numbers!\n""")

def play():
    player = 0
    x = 0
    starting_board = {1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}
    active_board = {}
    
    while x == 0:
        if player % 2 == 0:
            print("Player X, its your turn: ")
            active_board[int(input('Enter valid number to put your sign on: '))] = "X"
        else:
            print("Player O, its your turn: ")
            active_board[int(input('Enter valid number to put your sign on: '))] = "O"
        for i in active_board:
            starting_board[i] = active_board[i]
        player += 1

        print(f"""
        {starting_board[1]} | {starting_board[2]} | {starting_board[3]}
        {starting_board[4]} | {starting_board[5]} | {starting_board[6]}
        {starting_board[7]} | {starting_board[8]} | {starting_board[9]}
            """)

play()



# how do stop one player from removing the opponents input? 
# can you limit dictionary entries to one?


# how do you set up a win condition?
# win_condition_met = False