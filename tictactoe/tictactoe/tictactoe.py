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
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    # If X has made more moves than O, it's O's turn, otherwise, it's X's turn
    return O if count_X > count_O else X

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))

    return possible_moves
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if board[action[0]][action[1]] != EMPTY:
        raise Exception("action is invalid")
    # Create a deep copy of the original board
    new_board = copy.deepcopy(board)

    # Let the current player make their move
    current_player = player(board)
    new_board[i][j] = current_player

    return new_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O

        # Check for vertical win
    for col in range(len(board[0])):
        if all(row[col] == X for row in board):
            return X
        elif all(row[col] == O for row in board):
            return O

        # Check for diagonal win
    if all(board[i][i] == X for i in range(len(board))) or all(
            board[i][len(board) - 1 - i] == X for i in range(len(board))):
        return X
    elif all(board[i][i] == O for i in range(len(board))) or all(
            board[i][len(board) - 1 - i] == O for i in range(len(board))):
        return O

    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if all cells are filled
    for row in board:
        if EMPTY in row:
            return False

    # All cells are filled without a winner, it's a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        # It's X's turn
        best_score = float('-inf')
        best_move = None

        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)

            if score > best_score:
                best_score = score
                best_move = action

    else:
        # It's O's turn
        best_score = float('inf')
        best_move = None

        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)

            if score < best_score:
                best_score = score
                best_move = action

    return best_move

def minimax_score(board):
    if terminal(board):
        return utility(board)

    if player(board) == X:
        return max(minimax_score(result(board, action)) for action in actions(board))
    else:
        return min(minimax_score(result(board, action)) for action in actions(board))
