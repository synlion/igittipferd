### tictactoe diary
Formatting and Syntax guide for GitHub Markdown [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

#### 18/02/22 - Len
Currently trying to get to work on a tictactoe game in python.

#### 19/02/22 - Len
David joins the effort to get the git fun going.
We couldn't work out why he couldn't push changes to my repository. VS Code wasn't helping with their unclear commit process. 

#### 20/2/2022 - Len
GitHub sharing and pull requests understood and trialed. The issue was that we were trying to have David access my repository by just pushing to it. We have now figured out that it takes pull requests to do that. He is sufficiently set up on VS Code to start work and collaboration on this project. Now I just need to catch up in terms of knowledge. I have no idea how to start. I don't even know what I need to know in order to get to work. First issue David proposed we solve was how to display the running status of the game, on screen, in the command line. Something like this is what we're currently thinking:
``` 
X|X|X O|O|O -|-|-
X|X|X O|O|O X|-|-
X|X|X O|O|O -|O|-
``` 
So the question to figure out is how we can have inputs map onto that graphical interface. 

#### 22/2/2022 - David
Test commits with new bot. 

#### 22/2/2022 - Len
###### 20:03 
Originally I made a new Discord server for this collaborative repsository, but we've moved that over to my "home server". 
This entry serves in part to test whether the update bot works on that server. 
David's commit didn't go through, likely because I hadn't change the content type of the webhook to application/JSON. 

###### 20:12 
We are also running into some issues with branches and VS code trying to merge or work with outdated files. 
It's quite confusing. When opening a file in GitHub from VS Code, it brings you to a branch that isn't supposed to exist and can't be viewed any other way. 
It doesn't show up even when I go looking for it in the branches section. 
I'm currently trying to reproduce the issue in my copy of VS Code to track down the problem source. Let's see how that goes.

###### 20:32
I also ran into some trouble with a branch called `pr/3` that I certainly didn't create on purpose. So far, I haven't been able to reproduce the VS Code GitHub issue. I have to set up full GitHub integration there first. I also have to fix the Webhook. It isn't sending updates to my home server.

###### 20:54
Found the issue... again. You have to add `/github` at the end of the URL. I had this issue with the last Webhook as well and just totally forgot the solution. Now dinner.

#### 01/03/2022 - Len
Today we took the first big step towards creating a working tictactoe game. David suggested we use a dictionary, so we numbered the tiles on the gameboard and created a corresponding dictionary with empty spaces that can be changed to either X's or O's. I took that setup as far as I could by writing round instructions that alternate between player 1 and player 2. This preliminary version of the game -- titled 1.0 -- gives you the option to put down squares until the board is full. Declaring a winner only works manually and players can put their own game pieces on their opponents tiles. We will try to solve that issue with a for loop that terminates once a winning condition is reached and by somehow locking tiles that have been changed once? We will see.