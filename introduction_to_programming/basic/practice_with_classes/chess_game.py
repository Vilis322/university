from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_possible_moves(self):
        pass


class Pawn(ChessPiece):
    def get_possible_moves(self):
        if self.color == "white":
            return [(0, 1), (0, 2), (1, 1), (-1, 1)]
        elif self.color == "black":
            return [(0, -1), (0, -2), (1, -1), (-1, -1)]
        else:
            return None


class Rook(ChessPiece):
    def get_possible_moves(self):
        if self.color == "white" or self.color == "black":
            return [(0, 1), (0, -1), (1, 0), (-1, 0)]
        else:
            return None


class Bishop(ChessPiece):
    def get_possible_moves(self):
        if self.color == "white" or self.color == "black":
            return [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        else:
            return None


class ChessBoard:
    def __init__(self):
        self.board = {}

    def place_piece(self, piece, position):
        self.board[position] = piece

    def move_piece(self, from_position, to_position):
        if from_position in self.board:
            piece = self.board.pop(from_position)
            self.board[to_position] = piece

    def display_board(self):
        board_strings = []
        for row in range(8):
            row_string = ""
            for col in range(8):
                position = (col, row)
                if position in self.board:
                    piece = self.board[position]
                    if piece.color == "white":
                        row_string += f"{piece.__class__.__name__[0]}W "
                    else:
                        row_string += f"{piece.__class__.__name__[0]}B "
                else:
                    row_string += ". "
            board_strings.append(row_string)
        return board_strings


if __name__ == "__main__":
    chess_board = ChessBoard()
    white_pawn = Pawn("white")
    black_rook = Rook("black")
    white_bishop = Bishop("white")

    print(f"Possible moves for White Pawn: {white_pawn.get_possible_moves()}")
    print(f"Possible moves for Black Rook: {black_rook.get_possible_moves()}")
    print(f"Possible moves for White Bishop: {white_bishop.get_possible_moves()}")

    chess_board.place_piece(white_pawn, (4, 1))
    chess_board.place_piece(black_rook, (0, 0))
    chess_board.place_piece(white_bishop, (2, 2))

    board_strings = chess_board.display_board()
    for row_string in board_strings:
        print(row_string)

    chess_board.move_piece((4, 1), (4, 3))
    print("\nAfter moving White Pawn:")
    board_strings = chess_board.display_board()
    for row_string in board_strings:
        print(row_string)
