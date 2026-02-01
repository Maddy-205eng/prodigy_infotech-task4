

def show_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()

def check_winner(board, player):
    # Check rows, columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        show_board(board)
        print(f"Player {player}'s turn (Enter row and column 0-2):")

        try:
            row = int(input("Row (0-2): "))
            col = int(input("Col (0-2): "))
        except ValueError:
            print("Enter numbers only!")
            continue

        if row not in range(3) or col not in range(3):
            print("Row and column must be 0, 1, or 2.")
            continue
        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            show_board(board)
            print(f"Player {player} wins!")
            if input("Play again? (y/n): ").lower() == "y":
                board = [[" " for _ in range(3)] for _ in range(3)]
                player = "X"
                continue
            else:
                break

        if all(board[r][c] != " " for r in range(3) for c in range(3)):
            show_board(board)
            print("It's a draw!")
            if input("Play again? (y/n): ").lower() == "y":
                board = [[" " for _ in range(3)] for _ in range(3)]
                player = "X"
                continue
            else:
                break

        # Switch player
        player = "O" if player == "X" else "X"

play_game()

