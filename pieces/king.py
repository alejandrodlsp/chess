from move import Move

def get_legal_moves(piece, board):
    out_squares = []
    x,y = piece.pos

    king_moves = [
        (1, 1), (1, -1), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)
    ]

    for move in king_moves:
        x1 = x + move[0];
        y1 = y + move[1];

        if x1 > -1 and y1 > -1 and x1 < 8 and y1 < 8:
            square = board.get_at_position((x1, y1))
            if square == None or square.color != piece.color:
                out_squares.append((x1, y1))

    moves = []
    for m in out_squares:
        moves.append(Move((y,x), m, board))
    return moves