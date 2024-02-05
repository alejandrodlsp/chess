class Move():
    def __init__(self, pos, next_pos, board):
        self.pos = pos # TODO: Use pos from piece
        self.next_pos = next_pos
        self.board = board
        self.piece = self.get_piece()
        self.capture_piece = self.capture_piece()
        self.is_capture = self.capture_piece != None
        
    def get_piece(self):
        return self.board.board_state[self.pos[0]][self.pos[1]]
    
    def capture_piece(self):
        return self.board.board_state[self.next_pos[1]][self.next_pos[0]]

    def position_notation(self):
        return square_notation(self.next_pos)
    
    def notation(self):
        square_notation(self.pos)

def square_notation(pos):
    y,x = pos
    file_notations = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return file_notations[y] + str(9 - (x + 1))