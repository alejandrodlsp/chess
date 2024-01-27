def get_legal_moves(pos, color, board):
    board = board.board_state
    out_squares = []
    x,y = pos

    y1 = y-1
    while (y1 > -1): # edge of the board
        if board[y1][x] == None:
            out_squares.append((y1,x)) # square is legal
        elif board[y1][x].color != color:
            out_squares.append((y1,x)) # square is legal
            y1 = -1 # look no further in this direction
        else: # if same color
            y1 = -1 # look no further in this direction
        y1 -= 1 # check next square

    # check all other directions
    y1 = y+1
    while (y1 < 8):
        if board[y1][x] == None:
            out_squares.append((y1,x)) # square is legal
        elif board[y1][x].color != color:
            out_squares.append((y1,x)) # square is legal
            y1 = 8 # look no further in this direction
        else: # if same color
            y1 = 8 # look no further in this direction
        y1 += 1 # check next square

    x1 = x - 1
    while (x1 > -1):
        if board[y][x1] == None:
            out_squares.append((y,x1)) # square is legal
        elif board[y][x1].color != color:
            out_squares.append((y,x1)) # square is legal
            x1 = -1 # look no further in this direction
        else: # if same color
            x1 = -1 # look no further in this direction
        x1 -= 1

    x1 = x + 1
    while (x1 < 8):
        if board[y][x1] == None:
            out_squares.append((y,x1)) # square is legal
        elif board[y][x1].color != color:
            out_squares.append((y,x1)) # square is legal
            x1 = 8 # look no further in this direction
        else: # if same color
            x1 = 8 # look no further in this direction
        x1 += 1

    return out_squares