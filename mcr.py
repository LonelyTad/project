def is_win(game):
    for row in game:
        if row[0] == row[1] == row[2] and (row[0] == 'X' or row[0] == 'O'):
            return True
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] and (game[0][col] == 'X' or game[0][col] == 'O'):
            return True
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        return True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        return True
    return False

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
                # user input
                i, j = map(int, input().split())
                i -= 1  # 转换为索引（0-2）
                j -= 1  # 转换为索引（0-2）

                # check
                if not (0 <= i < 3 and 0 <= j < 3):
                    print("Invalid input. Please enter numbers between 1 and 3 for both i and j.")
                    continue

                # check position
                if game[i][j] != ' ':
                    print("Invalid move. The cell is already taken. Try again.")
                    continue
                
                # if valid then break
                break
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        
      
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
            
        if is_win(game):
            print(f"Player {'1' if not turn else '2'} wins!")

        if n == 8:  
            print("It's a tie!")

    
        for row in game:
            print(" ".join(row))
    

    print("Final game board:")
    for row in game:
        print(" ".join(row))

if __name__ == "__main__":
    main()

