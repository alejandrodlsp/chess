class Move():
    def __init__(self, pos, next_pos, board):
        self.pos = pos
        self.next_pos = next_pos
        self.board = board
        self.capture_piece = self.capture_piece()
        self.is_check = self.is_check()
        self.is_mate = self.is_mate()
        self.piece = self.get_piece()

    def get_piece(self):
        return self.board.board_state[self.pos[1]][self.pos[0]]
    
    def capture_piece(self):
        return self.board.board_state[self.next_pos[1]][self.next_pos[0]]

    def is_check(self):
        return None
    
    def is_mate(self):
        return None

    def position_notation(self):
        return square_notation(self.pos)
    
    def notation(self):
        square_notation(self.pos)

def square_notation(pos):
    y,x = pos
    file_notations = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return file_notations[y] + (x + 1)