class GameState:
 
    def __init__(self):
        """
            8x8 board. All element has 2 characters.
            First elements are black piece (b) and last elements are
            white piece (b). "--" represent empty space
        """
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.selected = None
        self.move_log = []


    def update_board(self, piece, position):
        x, y = position
        print("before", self.board[y][x])
        board = self.board
        print("after", self.board[y][x])
         