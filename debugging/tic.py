#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the tic-tac-toe board.

    Parameters:
    board (list): A 3x3 list representing the tic-tac-toe board.

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """
    Check if there is a winner on the tic-tac-toe board.

    Parameters:
    board (list): A 3x3 list representing the tic-tac-toe board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_full(board):
    """
    Check if the tic-tac-toe board is full (no more moves possible).

    Parameters:
    board (list): A 3x3 list representing the tic-tac-toe board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play a game of tic-tac-toe.

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter a number between 0 and 2.")
                continue
            
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[row][col] = player

            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break

            if check_full(board):
                print_board(board)
                print("It's a draw!")
                break

            player = "O" if player == "X" else "X"
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    tic_tac_toe()

