
def moves_left(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                return True
    return False

def check_win(board):
    for row in range(3) :     
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :        
            if (board[row][0] == player) :
                return 10
            elif (board[row][0] == opponent) :
                return -10
  
    # Checking for Columns for X or O victory. 
    for col in range(3) :
       
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
          
            if (board[0][col] == player) : 
                return 10
            elif (board[0][col] == opponent) :
                return -10
  
    # Checking for Diagonals for X or O victory. 
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
      
        if (board[0][0] == player) :
            return 10
        elif (board[0][0] == opponent) :
            return -10
  
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
      
        if (board[0][2] == player) :
            return 10
        elif (board[0][2] == opponent) :
            return -10
  
    # Else if none of them have won then return 0 
    return 0









def minimax(board, depth,isMax):
    score = check_win(board)
    if (score == 10):
        return score
    if (score == -10):
        return score
    if moves_left is False:
        return 0
    
    if (isMax):
        best = -1000
        for row in range(3):
            for col in range(3):
                if (board[row][col] == None):
                    board[row][col] = player
                    best = max(best, minimax(board,depth +1, not isMax) )
                    board[row][col] = None
        return best
    else:
        best = 1000
        for row in range(3):
            for col in range(3):
                if (board[row][col] == None):
                    board[row][col] = opponent
                    best = min(best, minimax(board,depth +1, not isMax) )
                    board[row][col] = None
        return best
def best_move(board):
    bestVal = -1000
    bestMove = (-1,-1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                board[row][col] = player
                moveVal = minimax(board, 0, False) 
                board[row][col] = None
                if (moveVal > bestVal) :                
                    bestMove = (row,col)
                    bestVal = moveVal
                    print(bestVal)
                    return bestMove


def idk_yet(board, player_fun, opponent_fun):# 1/0
    global player, opponent
    player = player_fun
    opponent = opponent_fun
    move = best_move(board)

    row = move[0]
    col = move[1]
    match row:
        case 0:
            match col:
                case 0:
                    return 1 
                case 1:
                    return 2
                case 2:
                    return 3
        case 1:
            match col:
                case 0:
                    return 4 
                case 1:
                    return 5
                case 2:
                    return 6
        case 2:
            match col:
                case 0:
                    return 7 
                case 1:
                    return 8
                case 2:
                    return 9






