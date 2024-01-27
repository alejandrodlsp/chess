from enum import Enum
from pieces.bishop import get_legal_moves as get_bishop_legal_moves
from pieces.rook import get_legal_moves as get_rook_legal_moves

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

class Piece:
    def __init__(self, type = PieceType.PAWN, color = PieceColor.WHITE):
        self.type = type
        self.color = color

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
    
    def get_legal_moves(self, pos, board):
        if self.type == PieceType.BISHOP:
            return get_bishop_legal_moves(pos, self.color, board)
        if self.type == PieceType.ROOK:
            return get_rook_legal_moves(pos, self.color, board)
        else:
            return None

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
    return PieceType.EMPTY
    
def get_char_piece_color(char):
    return PieceColor.WHITE if char.isupper() else PieceColor.BLACK