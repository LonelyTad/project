def is_win(game):
    # 检查行
    for row in game:
        if row[0] == row[1] == row[2] and (row[0] == 'X' or row[0] == 'O'):
            return True
    # 检查列
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] and (game[0][col] == 'X' or game[0][col] == 'O'):
            return True
    # 检查对角线
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
                # 获取用户输入
                i, j = map(int, input().split())
                i -= 1  # 转换为索引（0-2）
                j -= 1  # 转换为索引（0-2）

                # 检查坐标是否在有效范围内（1到3之间）
                if not (0 <= i < 3 and 0 <= j < 3):
                    print("Invalid input. Please enter numbers between 1 and 3 for both i and j.")
                    continue

                # 检查位置是否已经被占用
                if game[i][j] != ' ':
                    print("Invalid move. The cell is already taken. Try again.")
                    continue
                
                # 如果输入有效，跳出循环
                break
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        
        # 根据玩家的回合选择 'X' 或 'O'
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'

        # 检查是否有玩家获胜
        if is_win(game):
            print(f"Player {'1' if not turn else '2'} wins!")
            break

        # 检查是否平局
        if n == 8:  # 所有格子已经填满
            print("It's a tie!")

        # 显示游戏板
        for row in game:
            print(" ".join(row))
    
    # 最终棋盘显示
    print("Final game board:")
    for row in game:
        print(" ".join(row))

if __name__ == "__main__":
    main()

