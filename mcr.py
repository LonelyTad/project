def is_win(game):
    win = False
    # Check rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # Check columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    
    for n in range(9):
        turn = not turn  # Switch turns
        if not turn:
            print("Player 1's turn.")
        else:
            print("Player 2's turn.")
        
        while True:
            print("Which cell to mark? i:[1..3], j:[1..3]: ")
            try:
                # Get user input
                i, j = map(int, input().split())
                i -= 1  # Convert to index (0-2)
                j -= 1  # Convert to index (0-2)

                # Check if the coordinates are within valid range (1 to 3)
                if not (0 <= i < 3 and 0 <= j < 3):
                    print("Invalid input. Please enter numbers between 1 and 3 for both i and j.")
                    continue

                # Check if the position is already taken
                if game[i][j] != ' ':
                    print("Invalid move. The cell is already taken. Try again.")
                    continue
                
                # If input is valid, break the loop
                break
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        
        # Mark the cell with 'X' or 'O' based on the player's turn
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'

        # Check if any player has won
        if is_win(game):
            print(f"Player {'1' if not turn else '2'} wins!")
            break

        # Check if it's a tie
        if n == 8:  # All cells are filled
            print("It's a tie!")

        # Display the game board
        for row in game:
            print(" ".join(row))
    
    # Final game board display
    print("Final game board:")
    for row in game:
        print(" ".join(row))

if __name__ == "__main__":
    main()
