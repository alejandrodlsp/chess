import pygame
import math

from board import Board
from piece import Piece, PieceType, PieceColor

PIECE_SIZE = 60
BOARD_BORDER = 26
PIECE_SPACING = 56

board_bg_img = pygame.image.load("assets/board/wooden.png")

white_king_img = pygame.transform.scale(pygame.image.load("assets/pieces/white/King.png"), (PIECE_SIZE, PIECE_SIZE))
white_queen_img = pygame.transform.scale(pygame.image.load("assets/pieces/white/Queen.png"), (PIECE_SIZE, PIECE_SIZE))
white_rook_img = pygame.transform.scale(pygame.image.load("assets/pieces/white/Rook.png"), (PIECE_SIZE, PIECE_SIZE))
white_knight_img = pygame.transform.scale(pygame.image.load("assets/pieces/white/Knight.png"), (PIECE_SIZE, PIECE_SIZE))
white_bishop_img = pygame.transform.scale(pygame.image.load("assets/pieces/white/Bishop.png"), (PIECE_SIZE, PIECE_SIZE))
white_pawn_img = pygame.transform.scale(pygame.image.load("assets/pieces/white/Pawn.png"), (PIECE_SIZE, PIECE_SIZE))

black_king_img = pygame.transform.scale(pygame.image.load("assets/pieces/black/King.png"), (PIECE_SIZE, PIECE_SIZE))
black_queen_img = pygame.transform.scale(pygame.image.load("assets/pieces/black/Queen.png"), (PIECE_SIZE, PIECE_SIZE))
black_rook_img = pygame.transform.scale(pygame.image.load("assets/pieces/black/Rook.png"), (PIECE_SIZE, PIECE_SIZE))
black_knight_img = pygame.transform.scale(pygame.image.load("assets/pieces/black/Knight.png"), (PIECE_SIZE, PIECE_SIZE))
black_bishop_img = pygame.transform.scale(pygame.image.load("assets/pieces/black/Bishop.png"), (PIECE_SIZE, PIECE_SIZE))
black_pawn_img = pygame.transform.scale(pygame.image.load("assets/pieces/black/Pawn.png"), (PIECE_SIZE, PIECE_SIZE))

def draw_board(screen, board):
    screen.blit(pygame.transform.scale(board_bg_img, (500, 500)), (0, 0))
    
    for i, row in enumerate(board.board_state):
        for j, piece in enumerate(row):
            piece_asset = get_piece_image(piece)
            if piece_asset != None:
                screen.blit(piece_asset, get_square_screen_pos(j, i))

def get_piece_image(piece : Piece):
    if piece == None:
        return None
    if piece.type == PieceType.KING:
        return white_king_img if piece.color == PieceColor.WHITE else black_king_img
    if piece.type == PieceType.QUEEN:
        return white_queen_img if piece.color == PieceColor.WHITE else black_queen_img
    if piece.type == PieceType.ROOK:
        return white_rook_img if piece.color == PieceColor.WHITE else black_rook_img
    if piece.type == PieceType.KNIGHT:
        return white_knight_img if piece.color == PieceColor.WHITE else black_knight_img
    if piece.type == PieceType.BISHOP:
        return white_bishop_img if piece.color == PieceColor.WHITE else black_bishop_img
    if piece.type == PieceType.PAWN:
        return white_pawn_img if piece.color == PieceColor.WHITE else black_pawn_img
    return None

def get_square_screen_pos(x, y):
    spacing_x = x * PIECE_SPACING + BOARD_BORDER
    spacing_y = y * PIECE_SPACING + BOARD_BORDER
    return (spacing_x, spacing_y)


def get_square_at_pos(pos):
    if pos[0] < BOARD_BORDER or pos[0] > 500 - BOARD_BORDER or pos[1] < BOARD_BORDER or pos[1] > 500 - BOARD_BORDER:
        return
    pos_x = math.floor( (pos[0] - BOARD_BORDER) / PIECE_SPACING )
    pos_y = math.floor( (pos[1] - BOARD_BORDER) / PIECE_SPACING )
    
    return (pos_x, pos_y)

def handle_click_event(event, board : Board):
    square = get_square_at_pos(event.pos)
    piece = board.get_at_position(square)
    print(piece.get_legal_moves(square, board))