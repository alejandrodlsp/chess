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
    def __init__(self, on_move = None, on_check = None):
        self.move_count = 0
        self.move_history = []
        self.board_state = []
        self.current_turn = PieceColor.WHITE
        self.on_move = on_move
        self.on_check = on_check
        self.in_check = False

        self.black_kingside_castle_available = False
        self.black_queenside_castle_available = False
        self.white_kingside_castle_available = False
        self.white_queenside_castle_available = False

        self.initialize_board_state()
        print(self.string_state())
        self.search_for_check()
        self.check_castle_availability()

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
        piece.move(move.next_pos)
        self.current_turn = PieceColor.WHITE if self.current_turn == PieceColor.BLACK else PieceColor.BLACK
        self.on_move(move)
        self.move_history.append(move)
        self.search_for_check()
        self.check_castle_availability()

        print(self.black_queenside_castle_available)

    def pop_last_move(self):
        if len(self.move_history) < 1:
            return
        
        move = self.move_history.pop()
        
        self.board_state[move.pos[0]][move.pos[1]] = move.piece
        move.piece.move_back(move.pos)

        captured = move.capture_piece
        if captured:
            self.board_state[move.next_pos[1]][move.next_pos[0]] = captured
        else:
            self.board_state[move.next_pos[1]][move.next_pos[0]] = None

        self.current_turn = PieceColor.WHITE if self.current_turn == PieceColor.BLACK else PieceColor.BLACK
        self.on_move(move)
        self.search_for_check()
        self.check_castle_availability()

    def search_for_check(self):
        moves = self.all_moves()
        for move in moves:
            if move.capture_piece:
                if move.capture_piece.type == PieceType.KING:
                    self.in_check = True
                    if self.on_check:
                        self.on_check(move)
                    return

    def is_attacked_by_color(self, pos, color : PieceColor):
        for piece in self.attacked_squares_by_color(color):
            if piece == pos:
                return True
        return False

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

    def get_positions_for_piece_type(self, type : PieceType, color : PieceColor):
        pieces = []
        for row in self.board_state:
            for piece in row:
                if piece:
                    if piece.type == type and piece.color == color:
                        pieces.append(piece)
        return pieces

    def get_piece_position(self, type : PieceType, color : PieceColor):
        for row in self.board_state:
            for piece in row:
                if piece:
                    if piece.type == type and piece.color == color:
                        return piece
        return None

    def make_move_if_legal(self, selected_piece: Piece, new_square):
        legal_move = selected_piece.is_legal_move(self, new_square)
        if legal_move:
            self.make_move(legal_move)

    def check_castle_availability(self):
        kingside_rook_black = self.board_state[0][7]
        queenside_rook_black = self.board_state[0][0]
        black_king = self.get_piece_position(PieceType.KING, PieceColor.BLACK)

        self.black_kingside_castle_available = self.check_castle_in_file(black_king, kingside_rook_black)
        self.black_queenside_castle_available = self.check_castle_in_file(black_king, queenside_rook_black)

        kingside_rook_white = self.board_state[7][7]
        queenside_rook_white = self.board_state[7][0]
        white_king = self.get_piece_position(PieceType.KING, PieceColor.WHITE)

        self.white_kingside_castle_available = self.check_castle_in_file(white_king, kingside_rook_white)
        self.white_queenside_castle_available = self.check_castle_in_file(white_king, queenside_rook_white)

    def check_castle_in_file(self, king : Piece, rook : Piece) -> bool:
        if not king or king.has_moved(): # Check king has not moved
            return False
        if self.is_attacked_by_color(king.pos, opposite_color(king.color)): # If in check
            return False
        if not rook or rook.color == opposite_color(king.color) or rook.has_moved(): # Check rook has not moved
            return False
        
        for i in range(min(king.pos[0], rook.pos[0]) + 1, max(king.pos[0], rook.pos[0])):
            if self.get_at_position((i, king.pos[1])): # Check no square in between is occupied
                return False
            if self.is_attacked_by_color((i, king.pos[1]), opposite_color(king.color)): # Check no square in between is attacked
                return False
        return True

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

    def all_moves_for_color(self, color: PieceColor):
        moves = []
        pieces = self.white_pieces() if color == PieceColor.WHITE else self.black_pieces()
        for piece in pieces:
            pmoves = piece.get_legal_moves(self)
            for move in pmoves:
                moves.append(move)
        return moves

    def attacked_squares_by_color(self, color: PieceColor):
        attacked = []
        for move in self.all_moves_for_color(color):
            attacked.append(move.next_pos)
        return attacked

    def attacked_squares(self):
        attacked = []
        for move in self.all_moves():
            attacked.append(move.next_pos)
        return attacked
    
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