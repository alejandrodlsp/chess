from piece import *

initial_board_state =  [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], 
            ['.', '.', 'p', '.', 'p', 'p', 'p', 'p'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

class Board:
    def __init__(self):
        self.move_count = 0
        self.move_history = []
        self.board_state = []
        self.current_turn = PieceColor.WHITE
           
        self.initialize_board_state()
        print(self.string_state())

    def initialize_board_state(self):
        for row in initial_board_state:
            new_row = []
            for col in row:
                if col == '.':
                    new_row.append(None)
                else:
                    new_piece = Piece(get_piece_type_from_char(col), get_char_piece_color(col))
                    new_row.append(new_piece)
            self.board_state.append(new_row)

    def string_state(self):
        str = ""
        for row in self.board_state:
            for col in row:
                if col is None:
                    str += "., "
                else:
                    print(col)
                    str += col.char() + ", "
            str += "\n"
        return str
    
    def get_at_position(self, pos):
        return self.board_state[pos[1]][pos[0]]
    
    def get_positions_for_piece(self, piece):
        pieces = []
        for i, row in enumerate(self.board_state):
            for j, col in enumerate(row):
                if col == piece:
                    pieces += (i, j)
        return pieces
    
    def get_position_for_piece(self, piece):
        for i, row in enumerate(self.board_state):
            for j, col in enumerate(row):
                if col == piece:
                    return (i, j)
        return None
    
    def white_pieces():
        pass

    def black_pieces():
        pass

    def attacked_pieces_white():
        pass

    def attacked_pieces_black():
        pass