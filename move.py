class Move():
    def __init__(self, pos, next_pos, board):
        self.pos = pos # TODO: Use pos from piece
        self.next_pos = next_pos
        self.board = board
        self.piece = self.get_piece()
        self.is_mate = self.is_mate()

    def get_piece(self):
        return self.board.board_state[self.pos[0]][self.pos[1]]
    
    def capture_piece(self):
        return self.board.board_state[self.next_pos[1]][self.next_pos[0]]

    def is_check(self):
        attacked_pieces = self.board.attacked_pieces_white() if self.piece.color == 2 else self.board.attacked_pieces_black()
        for piece in attacked_pieces:
            if piece.type == 1: # King
                return True
        return False
    
    def is_mate(self):
        return None

    def position_notation(self):
        return square_notation(self.next_pos)
    
    def notation(self):
        square_notation(self.pos)

def square_notation(pos):
    y,x = pos
    file_notations = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return file_notations[y] + str(9 - (x + 1))