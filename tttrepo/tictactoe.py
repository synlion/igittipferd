# Project Inititalized: 18/02/2022 
# 21:31 

# Beginning of the tictactoe.py project..

import random

print("Let's play TicTacToe!")

# a possible game board 
print("""\n
-|-|-
-|-|-
-|-|-
    \n""")

1 | 2 | 3 
4 | 5 | 6 
7 | 8 | 9

print("""\n
X|-|-
-|-|-
-|-|-
    \n""")

dict1 = {1:"-", 2:"-",3:"-",4:"-",5:"-",6:"-",7:"-",8:"-",9:"-"}

print("""
1 | 2 | 3 
4 | 5 | 6 
7 | 8 | 9""")
dict1[int(input("do it"))] = "X"

print(f"""\n
{dict1[1]}|{dict1[2]}|{dict1[3]}
{dict1[4]}|{dict1[5]}|{dict1[6]}
{dict1[7]}|{dict1[8]}|{dict1[9]}
    \n""")