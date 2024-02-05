from enum import Enum
from pieces.bishop import get_legal_moves as get_bishop_legal_moves
from pieces.rook import get_legal_moves as get_rook_legal_moves
from pieces.queen import get_legal_moves as get_queen_legal_moves
from pieces.knight import get_legal_moves as get_knight_legal_moves
from pieces.king import get_legal_moves as get_king_legal_moves
from pieces.pawn import get_legal_moves as get_pawn_legal_moves

class PieceType(Enum):
    KING = 1
    QUEEN = 2
    ROOK = 3
    BISHOP = 4
    KNIGHT = 5
    PAWN = 6
    EMPTY = 7

class PieceColor(Enum):
    WHITE = 1
    BLACK = 2

def opposite_color(color: PieceColor) -> PieceColor:
    return PieceColor.WHITE if color == PieceColor.BLACK else PieceColor.BLACK

class Piece:
    def __init__(self, pos, type = PieceType.PAWN, color = PieceColor.WHITE):
        self.pos = pos
        self.type = type
        self.color = color
        self.moved = False
        self.n_of_moves = 0
        
    def move(self, new_pos):
        self.n_of_moves += 1
        self.pos = new_pos

    def move_back(self, last_pos):
        self.n_of_moves -= 1
        self.pos = last_pos
    
    def has_moved(self):
        return self.n_of_moves > 0
    
    def char(self):
        if self.type == PieceType.KING:
            return "K" if self.color == PieceColor.WHITE else "k"
        if self.type == PieceType.QUEEN:
            return "Q" if self.color == PieceColor.WHITE else "q"
        if self.type == PieceType.ROOK:
            return "R" if self.color == PieceColor.WHITE else "r"
        if self.type == PieceType.BISHOP:
            return "B" if self.color == PieceColor.WHITE else "b"
        if self.type == PieceType.KNIGHT:
            return "N" if self.color == PieceColor.WHITE else "n"
        if self.type == PieceType.PAWN:
            return "P" if self.color == PieceColor.WHITE else "p"
        return "."

    def color(self):
        return self.color

    def get_legal_moves(self, board):
        if self.type == PieceType.BISHOP:
            return get_bishop_legal_moves(self, board)
        if self.type == PieceType.ROOK:
            return get_rook_legal_moves(self, board)
        if self.type == PieceType.QUEEN:
            return get_queen_legal_moves(self, board)
        if self.type == PieceType.KNIGHT:
            return get_knight_legal_moves(self, board)
        if self.type == PieceType.KING:
            return get_king_legal_moves(self, board)
        if self.type == PieceType.PAWN:
            return get_pawn_legal_moves(self, board)
        else:
            return None

    def is_legal_move(self, board, newpos):
        legal_moves = self.get_legal_moves(board)
        for move in legal_moves:
            if move.next_pos == newpos:
                return move
        return False

def get_piece_type_from_char(char):
    if char.lower() == 'k':
        return PieceType.KING
    if char.lower() == 'q':
        return PieceType.QUEEN
    if char.lower() == 'r':
        return PieceType.ROOK
    if char.lower() == 'b':
        return PieceType.BISHOP
    if char.lower() == 'n':
        return PieceType.KNIGHT
    if char.lower() == 'p':
        return PieceType.PAWN
    return None

def get_char_piece_color(char):
    if char == '.':
        return None
    return PieceColor.WHITE if char.isupper() else PieceColor.BLACK