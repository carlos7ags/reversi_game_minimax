from copy import deepcopy
from random import shuffle


class Ai:
    @staticmethod
    def result(board, action):
        """Returns the board that results from making a move on the board"""
        new_board = deepcopy(board)
        x, y = action
        new_board.move(x, y)
        return new_board

    @classmethod
    def min_value(cls, board, depth):
        """Finds the move that minimize utility"""
        if depth > 0:
            board.det_winner()
            if board.gameover:
                return board.utility
            v = float("inf")
            valid_moves = board.valid_moves.keys()
            shuffle(valid_moves)
            for action in valid_moves:
                v = min(v, cls.max_value(cls.result(board, action), depth-1))
                if v == -1:
                    return v
            return v
        else:
            board.gameover = True
            board.det_winner()
            return board.utility

    @classmethod
    def max_value(cls, board, depth):
        """Finds the move that maximize utility"""
        if depth > 0:
            board.det_winner()
            if board.gameover:
                return board.utility
            v = float("-inf")
            valid_moves = board.valid_moves.keys()
            shuffle(valid_moves)
            for action in valid_moves:
                v = max(v, cls.min_value(cls.result(board, action), depth-1))
                if v == 1:
                    return v
            return v
        else:
            board.gameover = True
            board.det_winner()
            return board.utility

    @classmethod
    def minimax(cls, board, depth):
        """Returns the optimal action for the current player on the board"""
        if board.gameover:
            return None

        best_move = None
        current_player = board.player

        if current_player == 2:
            v = float("inf")
            valid_moves = board.valid_moves.keys()
            shuffle(valid_moves)
            for action in valid_moves:
                k = cls.max_value(cls.result(board, action), depth)
                if k < v:
                    v = k
                    best_move = action
                if v == -1:
                    break
        else:
            v = float("-inf")
            valid_moves = board.valid_moves.keys()
            shuffle(valid_moves)
            for action in valid_moves:
                k = cls.min_value(cls.result(board, action), depth)
                if k > v:
                    v = k
                    best_move = action
                if v == -1:
                    break
        return best_move
