from move import Move

def get_legal_moves(piece, board):
    board_state = board.board_state
    out_squares = []
    x,y = piece.pos

    y1 = y-1
    x1 = x-1
    while (x1 > -1) and (y1 > -1):
        if board_state[y1][x1] == None:
            out_squares.append((x1,y1))
        elif board_state[y1][x1].color != piece.color:
            out_squares.append((x1,y1))
            y1 = -1
        else:
            y1 = -1
        y1 -= 1
        x1 -= 1

    y1 = y+1
    x1 = x+1
    while (x1 < 8) and (y1 < 8):
        if board_state[y1][x1] == None:
            out_squares.append((x1,y1)) 
        elif board_state[y1][x1].color != piece.color:
            out_squares.append((x1,y1))
            y1 = 8 
        else: 
            y1 = 8 
        y1 += 1 
        x1 += 1

    y1 = y + 1
    x1 = x - 1
    while (x1 > -1) and (y1 < 8):
        if board_state[y1][x1] == None:
            out_squares.append((x1,y1))
        elif board_state[y1][x1].color != piece.color:
            out_squares.append((x1,y1))
            y1 = 8
        else:
            y1 = 8
        y1 += 1
        x1 -= 1

    y1 = y - 1
    x1 = x + 1
    while (x1 < 8) and (y1 > -1):
        if board_state[y1][x1] == None:
            out_squares.append((x1,y1))
        elif board_state[y1][x1].color != piece.color:
            out_squares.append((x1,y1))
            y1 = -1
        else:
            y1 = -1
        y1 -= 1
        x1 += 1

    moves = []
    for m in out_squares:
        moves.append(Move((y,x), m, board))
    return moves