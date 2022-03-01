# Project Inititalized: 18/02/2022 
# 21:31 

# Beginning of the tictactoe.py project..

# FOR REFERENCE: Number Grid and Empty game board:

# - | - | -
# - | - | -       
# - | - | -

# 1 | 2 | 3 
# 4 | 5 | 6 
# 7 | 8 | 9

##############################################################################
# INTRO TO THE GAME
##############################################################################

import random

print("""\n
Let's play TicTacToe!\n
These are the game board and the corresponding number tiles.\n
- | - | -       1 | 2 | 3 
- | - | -       4 | 5 | 6 
- | - | -       7 | 8 | 9
\nRemember the numbers!\n""")

# EMPTY DICTIONARY
dict1 = {1:"-", 2:"-",3:"-",4:"-",5:"-",6:"-",7:"-",8:"-",9:"-"}

###########
# ROUND 1 #
###########

dict1[int(input("""
Player 1, choose a tile to place your first 'X' on.
Enter a valid number: """))] = "X"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")

dict1[int(input("""
Player 2, choose a tile to place your first 'O' on.
Enter a valid number: """))] = "O"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")

###########
# ROUND 2 #
###########

dict1[int(input("""
Player 1, choose a tile to place your second 'X' on.
Enter a valid number: """))] = "X"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")

dict1[int(input("""
Player 2, choose a tile to place your second 'O' on.
Enter a valid number: """))] = "O"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")

###########
# ROUND 3 #
###########

dict1[int(input("""
Player 1, choose a tile to place your third 'X' on.
Enter a valid number: """))] = "X"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")

dict1[int(input("""
Player 2, choose a tile to place your third 'O' on.
Enter a valid number: """))] = "O"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")

###########
# ROUND 4 #
###########

dict1[int(input("""
Player 1, choose a tile to place your fourth 'X' on.
Enter a valid number: """))] = "X"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")

dict1[int(input("""
Player 2, choose a tile to place your fourth 'O' on.
Enter a valid number: """))] = "O"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")

###########
# ROUND 4 #
###########

dict1[int(input("""
Player 1, place your 'X' on the last tile to end the game.
Enter the last available number: """))] = "X"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")