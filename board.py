from piece import *
from move import Move

initial_board_state =  [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], 
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

class Board:
    def __init__(self, on_move = None):
        self.move_count = 0
        self.move_history = []
        self.board_state = []
        self.current_turn = PieceColor.WHITE
        self.on_move = on_move

        self.initialize_board_state()
        print(self.string_state())

    def initialize_board_state(self):
        for i, row in enumerate(initial_board_state):
            new_row = []
            for j, col in enumerate(row):
                if col == '.':
                    new_row.append(None)
                else:
                    new_piece = Piece((j, i), get_piece_type_from_char(col), get_char_piece_color(col))
                    new_row.append(new_piece)
            self.board_state.append(new_row)

    def make_move(self, move: Move):
        piece = self.board_state[move.pos[0]][move.pos[1]]
        self.board_state[move.pos[0]][move.pos[1]] = None
        self.board_state[move.next_pos[1]][move.next_pos[0]] = piece
        piece.pos = move.next_pos
        self.current_turn = PieceColor.WHITE if self.current_turn == PieceColor.BLACK else PieceColor.BLACK
        self.on_move(move)

    def string_state(self):
        str = ""
        for row in self.board_state:
            for col in row:
                if col is None:
                    str += "., "
                else:
                    str += col.char() + ", "
            str += "\n"
        return str
    
    def get_at_position(self, pos):
        return self.board_state[pos[1]][pos[0]]
    
    def get_positions_for_piece_type(self, type : PieceType):
        pieces = []
        for i, row in enumerate(self.board_state):
            for j, col in enumerate(row):
                if col.type == type:
                    pieces += (i, j)
        return pieces
    
    def get_position_for_piece_type(self, type : PieceType):
        for i, row in enumerate(self.board_state):
            for j, col in enumerate(row):
                if col.type == type:
                    return (i, j)
        return None
    
    def check_for_move(self, selected_piece: Piece, new_square):
        legal_move = selected_piece.is_legal_move(self, new_square)
        if legal_move:
            self.make_move(legal_move)

    def all_pieces(self):
        pieces = []
        for row in self.board_state:
            for p in row:
                if p:
                    pieces.append(p)
        return pieces
    
    def white_pieces(self):
        pieces = []
        for p in self.all_pieces():
            if p.color == PieceColor.WHITE:
                pieces.append(p)
        return pieces 

    def black_pieces(self):
        pieces = []
        for p in self.all_pieces():
            if p.color == PieceColor.BLACK:
                pieces.append(p)
        return pieces 

    def all_moves(self):
        moves = []
        for piece in self.all_pieces():
            pmoves = piece.get_legal_moves(self)
            for move in pmoves:
                moves.append(move)
        return moves
    
    def attacked_pieces_white(self):
        attacked = []
        for move in self.all_moves():
            if move.capture_piece and move.capture_piece.color == PieceColor.WHITE:
                attacked.append(move.capture_piece)
        return attacked

    def attacked_pieces_black(self):
        attacked = []
        for move in self.all_moves():
            if move.capture_piece and move.capture_piece.color == PieceColor.BLACK:
                attacked.append(move.capture_piece)
        return attacked