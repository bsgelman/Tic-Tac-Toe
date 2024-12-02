"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)
    
    if X_count <= O_count:
        return X
    else:
        return O
    
        


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    if action not in actions(board) or action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise ValueError("Action is invalid.")
    
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = current_player
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    moves = actions(board)
    if len(moves) == 0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    if result == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    current_player = 'X' if player(board) == X else 'O'

    def max_value(board):
        if terminal(board):
            return utility(board), None
        max_utility = float('-inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            utility_val, _ = min_value(new_board)
            if utility_val > max_utility:
                max_utility = utility_val
                best_action = action
        return max_utility, best_action

    def min_value(board):
        if terminal(board):
            return utility(board), None
        min_utility = float('inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            utility_val, _ = max_value(new_board)
            if utility_val < min_utility:
                min_utility = utility_val
                best_action = action
        return min_utility, best_action

    _, action = max_value(board) if current_player == 'X' else min_value(board)
    return action