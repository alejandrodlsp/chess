from move import Move

def get_legal_moves(piece, board):
    out_squares = []
    x,y = piece.pos
    ymov = -1 if piece.color.value == 1 else 1

    # check single move
    fpos = (x, y + ymov)
    fsquare = board.get_at_position(fpos)
    if fsquare == None:
        out_squares.append(fpos)
        # Check double move
        starting_sqr = 1 if piece.color.value == 2 else 6
        if y == starting_sqr:
            fpos = (x, y + ymov + ymov)
            fsquare = board.get_at_position(fpos)
            if fsquare == None:
                out_squares.append(fpos)

    # check for capture left
    if x > 0:
        fpos = (x - 1, y + ymov)
        fsquare = board.get_at_position(fpos)
        if fsquare != None and fsquare.color != piece.color:
            out_squares.append(fpos)

    # check for capture right
    if x < 7:
        fpos = (x + 1, y + ymov)
        fsquare = board.get_at_position(fpos)
        if fsquare != None and fsquare.color != piece.color:
            out_squares.append(fpos)

    # TODO: En Passant

    moves = []
    for m in out_squares:
        moves.append(Move((y,x), m, board))
    return moves