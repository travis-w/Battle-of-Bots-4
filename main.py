from random import randint


# Read board from standard in into 2d list
def read_board():
    board = []
    for i in range(10):
        board.append([int(x) for x in raw_input().split()])
    return board


# Print piece and reason for move
def print_move(piece, reason):
    print piece[0], piece[1]
    print reason


# Gets all posititions of pieces of certain player
def get_pieces(board, player):
    coordinates = []
    for i in range(10):
        for j in range(10):
            if board[i][j] == player:
                coordinates.append((i, j))

    return coordinates


# Check if move will win the game
def winning_move(board, piece, player):
    # Check vertical
    totalAbove = 0
    totalBelow = 0

    # Check Up
    for x in range(1, 10):
        if in_bounds((piece[0]-x, piece[1])) and board[piece[0]-x][piece[1]] == player:
            totalAbove += 1
        else:
            break

    # Check Below
    for x in range(1, 10):
        if in_bounds((piece[0]+x, piece[1])) and board[piece[0]+x][piece[1]] == player:
            totalBelow += 1
        else:
            break

    # If possible to win vertically
    if player == 1:
        if totalBelow + totalAbove == 4:
            return True
    else:
        if totalBelow + totalAbove >= 4:
            return True


    # Check Horizontal
    totalLeft = 0
    totalRight = 0

    # Check Left
    for x in range(1, 10):
        if in_bounds((piece[0], piece[1]-x)) and board[piece[0]][piece[1]-x] == player:
            totalLeft += 1
        else:
            break

    # Check Right
    for x in range(1, 10):
        if in_bounds((piece[0], piece[1]+x)) and board[piece[0]][piece[1]+x] == player:
            totalRight += 1
        else:
            break

    # If possible to win horizontally
    if player == 1:
        if totalRight + totalLeft == 4:
            return True
    else:
        if totalRight + totalLeft >= 4:
            return True

    # Check top left -> bottom right
    totalAbove = 0
    totalBelow = 0

    # Check Up
    for x in range(1, 10):
        if in_bounds((piece[0]-x, piece[1]-x)) and board[piece[0]-x][piece[1]-x] == player:
            totalAbove += 1
        else:
            break

    # Check Below
    for x in range(1, 10):
        if in_bounds((piece[0]+x, piece[1]+x)) and board[piece[0]+x][piece[1]+x] == player:
            totalBelow += 1
        else:
            break

    # If possible to win topLeft -> bottomRight
    if player == 1:
        if totalBelow + totalAbove == 4:
            return True
    else:
        if totalBelow + totalAbove >= 4:
            return True

    # Check topRight -> bottomLeft
    totalAbove = 0
    totalBelow = 0

    # Check Up
    for x in range(1, 10):
        if in_bounds((piece[0]-x, piece[1]+x)) and board[piece[0]-x][piece[1]+x] == player:
            totalAbove += 1
        else:
            break

    # Check Below
    for x in range(1, 10):
        if in_bounds((piece[0]+x, piece[1]-x)) and board[piece[0]+x][piece[1]-x] == player:
            totalBelow += 1
        else:
            break

    # If possible to win topLeft -> bottomRight
    if player == 1:
        if totalBelow + totalAbove == 4:
            return True
    else:
        if totalBelow + totalAbove >= 4:
            return True

    return False


# Check if move will set up player for win
def setup_move(board, piece, player):
    totalSetup = 0

    # Put piece board and check if winning move
    # Check vertical
    totalAbove = 0
    totalBelow = 0

    # Check Up
    hasZero = False
    zeroPos = -1

    for x in range(1, 6):
        if in_bounds((piece[0]-x, piece[1])) and board[piece[0]-x][piece[1]] == player:
            totalAbove += 1
        elif in_bounds((piece[0]-x, piece[1])) and board[piece[0]-x][piece[1]] == 0:
            if hasZero:
                if x - 1 - zeroPos == 0:
                    hasZero = False
                break
            else:
                hasZero = True
                zeroPos = x
        else:
            if x - 1 - zeroPos == 0:
                hasZero = False
            break

    # Check Below
    for x in range(1, 6):
        if in_bounds((piece[0]+x, piece[1])) and board[piece[0]+x][piece[1]] == player:
            totalBelow += 1
        elif in_bounds((piece[0]+x, piece[1])) and board[piece[0]+x][piece[1]] == 0:
            if hasZero:
                if x - 1 - zeroPos == 0:
                    hasZero = False
                break
            else:
                hasZero = True
                zeroPos = x
        else:
            if x - 1 - zeroPos == 0:
                hasZero = False
            break

    # If possible to win vertically
    if totalBelow + totalAbove == 3:
        if hasZero:
            totalSetup += 1
        else:
            if in_bounds((piece[0]-(totalAbove+1), piece[1])) and board[piece[0]-(totalAbove+1)][piece[1]] == 0:
                totalSetup += 1
            if in_bounds((piece[0]+(totalBelow+1), piece[1])) and board[piece[0]+(totalBelow+1)][piece[1]] == 0:
                totalSetup += 1

    # Check Horizontal
    totalLeft = 0
    totalRight = 0
    hasZero = False
    zeroPos = -1

    # Check Left
    for x in range(1, 6):
        if in_bounds((piece[0], piece[1]-x)) and board[piece[0]][piece[1]-x] == player:
            totalLeft += 1
        elif in_bounds((piece[0], piece[1]-x)) and board[piece[0]][piece[1]-x] == 0:
            if hasZero:
                if x - 1 - zeroPos == 0:
                    hasZero = False
                break
            else:
                hasZero = True
                zeroPos = x
        else:
            if x - 1 - zeroPos == 0:
                hasZero = False
            break

    # Check Right
    for x in range(1, 6):
        if in_bounds((piece[0], piece[1]+x)) and board[piece[0]][piece[1]+x] == player:
            totalRight += 1
        elif in_bounds((piece[0], piece[1]+x)) and board[piece[0]][piece[1]+x] == 0:
            if hasZero:
                if x - 1 - zeroPos == 0:
                    hasZero = False
                break
            else:
                hasZero = True
                zeroPos = x
        else:
            if x - 1 - zeroPos == 0:
                hasZero = False
            break

    # If possible to win horizontally
    if totalRight + totalLeft == 3:
        if hasZero:
            totalSetup += 1
        else:
            if in_bounds((piece[0], piece[1]-(totalLeft+1))) and board[piece[0]][piece[1]-(totalLeft+1)] == 0:
                totalSetup += 1
            if in_bounds((piece[0], piece[1]+(totalRight+1))) and board[piece[0]][piece[1]+(totalRight+1)] == 0:
                totalSetup += 1

    # Check top left -> bottom right
    totalAbove = 0
    totalBelow = 0
    hasZero = False
    zeroPos = -1

    # Check Up
    for x in range(1, 6):
        if in_bounds((piece[0]-x, piece[1]-x)) and board[piece[0]-x][piece[1]-x] == player:
            totalAbove += 1
        elif in_bounds((piece[0]-x, piece[1]-x)) and board[piece[0]-x][piece[1]-x] == 0:
            if hasZero:
                if x - 1 - zeroPos == 0:
                    hasZero = False
                break
            else:
                hasZero = True
                zeroPos = x
        else:
            if x - 1 - zeroPos == 0:
                hasZero = False
            break

    # Check Below
    for x in range(1, 6):
        if in_bounds((piece[0]+x, piece[1]+x)) and board[piece[0]+x][piece[1]+x] == player:
            totalBelow += 1
        elif in_bounds((piece[0]+x, piece[1]+x)) and board[piece[0]+x][piece[1]+x] == 0:
            if hasZero:
                if x - 1 - zeroPos == 0:
                    hasZero = False
                break
            else:
                hasZero = True
                zeroPos = x
        else:
            if x - 1 - zeroPos == 0:
                hasZero = False
            break

    # If possible to win topLeft -> bottomRight
    if totalBelow + totalAbove == 3:
        if hasZero:
            totalSetup += 1
        else:
            if in_bounds((piece[0]-(totalAbove+1), piece[1]-(totalAbove+1))) and board[piece[0]-(totalAbove+1)][piece[1]-(totalAbove+1)] == 0:
                totalSetup += 1
            if in_bounds((piece[0]+(totalBelow+1), piece[1]+(totalBelow+1))) and board[piece[0]+(totalBelow+1)][piece[1]+(totalBelow+1)] == 0:
                totalSetup += 1

    # Check topRight -> bottomLeft
    totalAbove = 0
    totalBelow = 0
    hasZero = False
    zeroPos = -1

    # Check Up
    for x in range(1, 6):
        if in_bounds((piece[0]-x, piece[1]+x)) and board[piece[0]-x][piece[1]+x] == player:
            totalAbove += 1
        elif in_bounds((piece[0]-x, piece[1]+x)) and board[piece[0]-x][piece[1]+x] == 0:
            if hasZero:
                if x - 1 - zeroPos == 0:
                    hasZero = False
                break
            else:
                hasZero = True
                zeroPos = x
        else:
            if x - 1 - zeroPos == 0:
                hasZero = False
            break

    # Check Below
    for x in range(1, 6):
        if in_bounds((piece[0]+x, piece[1]-x)) and board[piece[0]+x][piece[1]-x] == player:
            totalBelow += 1
        elif in_bounds((piece[0]+x, piece[1]-x)) and board[piece[0]+x][piece[1]-x] == 0:
            if hasZero:
                if x - 1 - zeroPos == 0:
                    hasZero = False
                break
            else:
                hasZero = True
                zeroPos = x
        else:
            if x - 1 - zeroPos == 0:
                hasZero = False
            break

    # If possible to win topLeft -> bottomRight
    if totalBelow + totalAbove == 3:
        if hasZero:
            totalSetup += 1
        else:
            if in_bounds((piece[0]-(totalAbove+1), piece[1]+(totalAbove+1))) and board[piece[0]-(totalAbove+1)][piece[1]+(totalAbove+1)] == 0:
                totalSetup += 1
            if in_bounds((piece[0]+(totalBelow+1), piece[1]-(totalBelow+1))) and board[piece[0]+(totalBelow+1)][piece[1]-(totalBelow+1)] == 0:
                totalSetup += 1

    return totalSetup


# Score position on board
def score_position(board, piece, player):
    opp = 1 if player == 2 else 2

    # Strenth of score going up [numEmpty, numPieces]
    # Check up
    upScore = [[], []]
    step = (piece[0]-1, piece[1])
    while in_bounds(step) and board[step[0]][step[1]] != opp:
        if board[step[0]][step[1]] == player:
            upScore[1].append(len(upScore[0]) + len(upScore[1]) + 1)
        else:
            upScore[0].append(len(upScore[0]) + len(upScore[1]) + 1)

        step = (step[0]-1, step[1])

    # Check down
    downScore = [[], []]
    step = (piece[0]+1, piece[1])
    while in_bounds(step) and board[step[0]][step[1]] != opp:
        if board[step[0]][step[1]] == player:
            downScore[1].append(len(downScore[0]) + len(downScore[1]) + 1)
        else:
            downScore[0].append(len(downScore[0]) + len(downScore[1]) + 1)
        step = (step[0]+1, step[1])

    # Check Left
    leftScore = [[], []]
    step = (piece[0], piece[1]-1)
    while in_bounds(step) and board[step[0]][step[1]] != opp:
        if board[step[0]][step[1]] == player:
            leftScore[1].append(len(leftScore[0]) + len(leftScore[1]) + 1)
        else:
            leftScore[0].append(len(leftScore[0]) + len(leftScore[1]) + 1)
        step = (step[0], step[1]-1)

    # Check Right
    rightScore = [[], []]
    step = (piece[0], piece[1]+1)
    while in_bounds(step) and board[step[0]][step[1]] != opp:
        if board[step[0]][step[1]] == player:
            rightScore[1].append(len(rightScore[0]) + len(rightScore[1]) + 1)
        else:
            rightScore[0].append(len(rightScore[0]) + len(rightScore[1]) + 1)
        step = (step[0], step[1]+1)

    # Check topLeft Score
    topLeftScore = [[], []]
    step = (piece[0]-1, piece[1]-1)
    while in_bounds(step) and board[step[0]][step[1]] != opp:
        if board[step[0]][step[1]] == player:
            topLeftScore[1].append(len(topLeftScore[0]) + len(topLeftScore[1]) + 1)
        else:
            topLeftScore[0].append(len(topLeftScore[0]) + len(topLeftScore[1]) + 1)
        step = (step[0]-1, step[1]-1)

    # Check bottomRight Score
    botRightScore = [[], []]
    step = (piece[0]+1, piece[1]+1)
    while in_bounds(step) and board[step[0]][step[1]] != opp:
        if board[step[0]][step[1]] == player:
            botRightScore[1].append(len(botRightScore[0]) + len(botRightScore[1]) + 1)
        else:
            botRightScore[0].append(len(botRightScore[0]) + len(botRightScore[1]) + 1)
        step = (step[0]+1, step[1]+1)

    # Check topRight Score
    topRightScore = [[], []]
    step = (piece[0]-1, piece[1]+1)
    while in_bounds(step) and board[step[0]][step[1]] != opp:
        if board[step[0]][step[1]] == player:
            topRightScore[1].append(len(topRightScore[0]) + len(topRightScore[1]) + 1)
        else:
            topRightScore[0].append(len(topRightScore[0]) + len(topRightScore[1]) + 1)
        step = (step[0]-1, step[1]+1)

    # Check topRight Score
    botLeftScore = [[], []]
    step = (piece[0]+1, piece[1]-1)
    while in_bounds(step) and board[step[0]][step[1]] != opp:
        if board[step[0]][step[1]] == player:
            botLeftScore[1].append(len(botLeftScore[0]) + len(botLeftScore[1]) + 1)
        else:
            botLeftScore[0].append(len(botLeftScore[0]) + len(botLeftScore[1]) + 1)
        step = (step[0]+1, step[1]-1)

    # Sum total Score
    score = 0

    # Check if possible to win in up down
    if sum([len(upScore[0]), len(upScore[1]), len(downScore[0]), len(downScore[1])]) >= 4 and len(upScore[1]) + len(downScore[1]) >= 1:
        for x in range(len(upScore[0])):
            score += 1.0 / upScore[0][x]

        for x in range(len(upScore[1])):
            if upScore[1][x] - x == 1:
                score += (2.0 * (x + 1)) / upScore[1][x]
            else:
                score += 2.0 / upScore[1][x]

        for x in range(len(downScore[0])):
            score += 1.0 / downScore[0][x]

        for x in range(len(downScore[1])):
            if downScore[1][x] - x == 1:
                score += (2.0 * (x + 1)) / downScore[1][x]
            else:
                score += 2.0 / downScore[1][x]

    # Check if possible to win left right
    if sum([len(leftScore[0]), len(leftScore[1]), len(rightScore[0]), len(rightScore[1])]) >= 4 and len(leftScore[1]) + len(rightScore[1]) >= 1:
        for x in range(len(leftScore[0])):
            score += 1.0 / leftScore[0][x]

        for x in range(len(leftScore[1])):
            if leftScore[1][x] - x == 1:
                score += (2.0 * (x + 1)) / leftScore[1][x]
            else:
                score += 2.0 / leftScore[1][x]

        for x in range(len(rightScore[0])):
            score += 1.0 / rightScore[0][x]

        for x in range(len(rightScore[1])):
            if rightScore[1][x] - x == 1:
                score += (2.0 * (x + 1)) / rightScore[1][x]
            else:
                score += 2.0 / rightScore[1][x]

    # Check if possible win topLeft->botRight
    if sum([len(topLeftScore[0]), len(topLeftScore[1]), len(botRightScore[0]), len(botRightScore[1])]) >= 4 and len(topLeftScore[1]) + len(botRightScore[1]) >= 1:
        for x in range(len(topLeftScore[0])):
            score += 1.0 / topLeftScore[0][x]

        for x in range(len(topLeftScore[1])):
            if topLeftScore[1][x] - x == 1:
                score += (2.0 * (x + 1)) / topLeftScore[1][x]
            else:
                score += 2.0 / topLeftScore[1][x]

        for x in range(len(botRightScore[0])):
            score += 1.0 / botRightScore[0][x]

        for x in range(len(botRightScore[1])):
            if botRightScore[1][x] - x == 1:
                score += (2.0 * (x + 1)) / botRightScore[1][x]
            else:
                score += 2.0 / botRightScore[1][x]

    # Check if possible to win botLeft->topRight
    if sum([len(botLeftScore[0]), len(botLeftScore[1]), len(topRightScore[0]), len(topRightScore[1])]) >= 4 and len(botLeftScore[1]) + len(topRightScore[1]) >= 1:
        for x in range(len(botLeftScore[0])):
            score += 1.0 / botLeftScore[0][x]

        for x in range(len(botLeftScore[1])):
            if botLeftScore[1][x] - x == 1:
                score += (2.0 * (x + 1)) / botLeftScore[1][x]
            else:
                score += 2.0 / botLeftScore[1][x]

        for x in range(len(topRightScore[0])):
            score += 1.0 / topRightScore[0][x]

        for x in range(len(topRightScore[1])):
            if topRightScore[1][x] - x == 1:
                score += (2.0 * (x + 1)) / topRightScore[1][x]
            else:
                score += 2.0 / topRightScore[1][x]

    return score


# Find top scoring poition
def find_highest_score(board, player):
    highest = (None, 0)

    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                tmp_score = score_position(board, (i, j), player)

                if  tmp_score > highest[1]:
                    highest = ((i, j), tmp_score)

    return highest


# Find first available winning move for player
def find_winning(board, player):
    winning_moves = []

    for i in range(10):
        for j in range(10):
            if board[i][j] == 0 and winning_move(board, (i, j), player):
                winning_moves.append((i, j))

    return winning_moves


# Find first available setup move for player
def find_setup(board, player):
    setup_moves = []

    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                setup = setup_move(board, (i, j), player)

                if setup != 0:
                    setup_moves.append(((i, j), setup))

    return setup_moves



def find_double(board, piece, player):
    board[piece[0]][piece[1]] = player

    setups = find_setup(board, player)

    board[piece[0]][piece[1]] = 0

    return len(setups)


def find_doubles(board, player):
    doubles = []

    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                double = find_double(board, (i, j), player)

                if double != 0:
                    doubles.append(((i, j), double))

    return doubles



# Check if piece is in bounds
def in_bounds(piece):
    if piece[0] < 0 or piece[0] > 9:
        return False
    if piece[1] < 0 or piece[1] > 9:
        return False
    return True


# Make a random move
def random_move(board):
    # Collect spaces that contain zero
    pieces = []

    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                pieces.append((i, j))

    x = randint(0, len(pieces)-1)

    print_move(pieces[x], "Random Move")


# Simulate the next turn
def simulate_turn(board, piece, player):
    board[piece[0]][piece[1]] = player

    winning_moves = find_winning(board, player)

    board[piece[0]][piece[1]] = 0

    return winning_moves


# Sim every move for piece and see if there are two setups
def simulate_all_moves(board, player):
    sim_moves = []

    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                sim = simulate_turn(board, (i, j), player)
                if len(sim) >= 1:
                    sim_moves.append(((i, j), len(sim)))

    return sim_moves


# Find highest score avergaged between both players
def find_best_avg(board, player):
    opp = 1 if player == 2 else 2

    highest = (None, 0)

    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                tmpAttack = score_position(board, (i, j), player)
                tmpDefend = score_position(board, (i, j), opp)

                tmp_score = (tmpAttack + tmpDefend) / 2

                if  tmp_score > highest[1]:
                    highest = ((i, j), tmp_score)

    return highest


# Main program
def make_move(board, player):
    # Get Opponent id
    opp = 1 if player == 2 else 2

    # Win game if possible
    playerWin = find_winning(board, player)

    if len(playerWin) != 0:
        print_move(playerWin[0], "Win Game")
        return

    # Prevent opponent win
    oppWin = find_winning(board, opp)

    if len(oppWin) != 0:
        print_move(oppWin[0], "Prevent Win")
        return

    # Find setup for playerWin
    playerSet = find_setup(board, player)
    oppSet = find_setup(board, opp)
    highestPSet = (None, 0)
    highestOSet = (None, 0)

    if len(playerSet) != 0:
        highestPSet = playerSet[0]

        for x in range(1, len(playerSet)):
            if playerSet[x][1] > highestPSet[1]:
                highestPSet = playerSet[x]
            elif playerSet[x][1] == highestPSet[1]:
                hScore = (score_position(board, highestPSet[0], player) + score_position(board, highestPSet[0], opp)) / 2
                oScore = (score_position(board, playerSet[x][0], player) + score_position(board, playerSet[x][0], player)) / 2

                if oScore > hScore:
                    highestPSet = playerSet[x]

    # Find setup for opponent
    if len(oppSet) != 0:
        highestOSet = oppSet[0]

        for x in range(1, len(oppSet)):
            if oppSet[x][1] > highestOSet[1]:
                highestOSet = oppSet[x]
            elif oppSet[x][1] == highestOSet[1]:
                hScore = (score_position(board, highestOSet[0], player) + score_position(board, highestOSet[0], opp)) / 2
                oScore = (score_position(board, oppSet[x][0], player) + score_position(board, oppSet[x][0], opp)) / 2

                if oScore > hScore:
                    highestOSet = oppSet[x]

    if highestOSet[1] <= 1:
        highestOSet = (None, 0)

    if highestOSet[0] is not None or highestPSet[0] is not None:
        if highestOSet[1] > highestPSet[1]:
            print_move(highestOSet[0], "Prevent Setup")
            return
        else:
            print_move(highestPSet[0], "Setup")
            return

    # Get all player pieces on board
    pieces = get_pieces(board, player)
    opp_pieces = get_pieces(board, opp)

    # Random Move for First Move (Player one)
    if len(pieces) == 0 and player == 1:
        print_move((4, 4), "Start Game")
        return

    # Opening move for player two
    if len(pieces) == 0 and player == 2:
        madeMove = False

        while not madeMove:
            i = randint(-1, 1)
            j = randint(-1, 1)
            point = (opp_pieces[0][0]+i, opp_pieces[0][1]+j)

            if in_bounds(point) and point != opp_pieces[0]:
                print_move(point, "White Opening")
                madeMove = True

        return

    # Double Setups
    playerDoubles = find_doubles(board, player)
    oppDoubles = find_doubles(board, opp)

    highestPDouble = (None, 0)
    highestODouble = (None, 0)

    # Find top playe rand opp double
    for x in range(len(playerDoubles)):
        if playerDoubles[x][1] > highestPDouble[1]:
            highestPDouble = playerDoubles[x]
        elif playerDoubles[x][1] == highestPDouble[1]:
            hScore = (score_position(board, highestPDouble[0], player) + score_position(board, highestPDouble[0], opp)) / 2
            oScore = (score_position(board, playerDoubles[x][0], player) + score_position(board, playerDoubles[x][0], opp)) / 2

            if oScore > hScore:
                highestPDouble = playerDoubles[x]

    for x in range(len(oppDoubles)):
        if oppDoubles[x][1] > highestODouble[1]:
            highestODouble = oppDoubles[x]
        elif oppDoubles[x][1] == highestODouble[1]:
            hScore = (score_position(board, highestODouble[0], player) + score_position(board, highestODouble[0], opp)) / 2
            oScore = (score_position(board, oppDoubles[x][0], player) + score_position(board, oppDoubles[x][0], opp)) / 2

            if oScore > hScore:
                highestODouble = oppDoubles[x]

    if highestODouble[0] is not None or highestPDouble[0] is not None:
        if highestPDouble[1] >= highestODouble[1]:
            print_move(highestPDouble[0], "Attack?")
        else:
            print_move(highestODouble[0], "Defend?")
        return


    # Look to future! (for player)
    future = simulate_all_moves(board, player)

    if len(future) != 0:
        print_move(future[0], "Future looks good")
        return

    futureOpp = simulate_all_moves(board, opp)

    if len(futureOpp) != 0:
        highest = (futureOpp[0][0], score_position(board, futureOpp[0][0], opp))
        for x in range(1, len(futureOpp)):
            tmpScore = score_position(board, futureOpp[x][0], opp)

            if tmpScore > highest[1]:
                highest = (futureOpp[x][0], tmpScore)

        print_move(highest[0], "Prevent the future")
        return

    # Find highest average move
    bestAvg = find_best_avg(board, player)

    #if bestAvg[0] is not None:
    #    print_move(bestAvg[0], "Make move")
    #    return

    # Get highest Scoring move for player and opponent
    highestPlayer = find_highest_score(board, player)
    highestOpp = find_highest_score(board, opp)

    if highestPlayer[0] is None and highestOpp[0] is None:
        random_move(board)
        return

    # Attack if highest player score better or equal, defend otherwise
    if highestPlayer[1] >= highestOpp[1]:
        print_move(highestPlayer[0], "Attack: " + str(highestPlayer[1]))
        return
    else:
        print_move(highestOpp[0], "Defend: " + str(highestOpp[1]))
        return


if __name__ == "__main__":
    # Get board and player
    board = read_board()
    player = int(input())

    # Run program
    make_move(board, player)
