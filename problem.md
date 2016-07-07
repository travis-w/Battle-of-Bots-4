**Gomoku** is a two-player board game which is played on a 10 X 10 grid of cells. Each player has an allocated color, Black ( First Player ) or White ( Second Player ) being conventional. Players take turns placing a stone of their color on a single cell within the overall playing board. The goal is to get an **unbroken row of five or more stones horizontally, vertically, or diagonally.**

Now here is a twist. We modified some of the rules of Gomoku to make the game little more fair and interesting.
- First Player must get an unbroken row of **exactly five** stones horizontally, vertically, or diagonally to win. This rule is applied to first player only. Second player can win by making an unbroken row of five or more stones.

<div style="text-align:center"><img src ="https://raw.githubusercontent.com/travis-w/Battle-of-Bots-4/master/gomoku.png" /></div>

We will play it on an 10 X 10 grid simulated as rhombus. The top left of the grid is [0, 0] and the bottom right is [9, 9]. The coordinate of a cell is represented by [row, column] where row increases from top to bottom and column increases from left to right.

__Input__

The input will be a 10 X 10 matrix consisting only of 0, 1 or 2. Then another line will follow which will contain a number - 1 or 2 which is your player id.

The cell having value 0 means it doesn't contain any stones. The cell having value 1 means it contains first player's stone which is Black in color. The cell having value 2 means it contains second player's stone which is white in color.

__Output__

Print the coordinates of the cell separated by space, where you want to put your stone. You must take care that you don't print invalid coordinates. For example, [1, 1] might be a valid coordinate in the game play, but [9, 10] will never be. Also if you play an invalid move or your code exceeds the time/memory limit while determining the move, you lose the game.

__Starting state__

The starting state of the game is the state of the board before the game starts.

0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

__First Input__

This is the input given to the first player at the start of the game.

0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1

__Scoring__

The scores are calculated by running tournament of all submissions. The tournament will run everyday at 1:00 PM IST (7:30 AM UTC). Your latest submission will be taken into tournament. Scores are assigned according to the Glicko-2 rating system. For more information and questions, see Bot problem judge.
