def max_coins(rows, cols, coins, curr_row, curr_col):
    if curr_row == rows - 1:
        if curr_col == cols - 1:
            return coins[curr_row][curr_col]
        elif curr_col < cols - 1:
            return coins[curr_row][curr_col] + max_coins(
                rows, cols, coins, curr_row, curr_col + 1
                )

    elif curr_row < rows - 1:
        if curr_col == cols - 1:
            return coins[curr_row][curr_col] + max_coins(
                rows, cols, coins, curr_row + 1, curr_col
            )
        elif curr_col < cols - 1:
            return coins[curr_row][curr_col] + max(
                max_coins(rows, cols, coins, curr_row + 1, curr_col),
                max_coins(rows, cols, coins, curr_row, curr_col + 1)
            )
if __name__ == "__main__":
    coins = []
    with open("123.txt", "r", encoding="utf-8") as fin:
        for line in fin:
            row_str = line.strip()
            if line:
                row = list(map(int, row_str.split()))
                coins.append(row)
    rows = len(coins)
    cols = len(coins[0])
    for row in coins[1:]:
        assert len(row) == cols
        
    max_value = max_coins(rows, cols, coins, 0, 0)
    new_coins = []
    for row in coins:
        new_coins.append([-value for value in row])
    a = -1
    print(a)
    min_value = a * max_coins(rows, cols, new_coins, 0, 0)

    print(max_value, min_value)
