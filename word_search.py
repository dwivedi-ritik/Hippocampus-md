grid = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

# Word Search Problem
def find_word(grid, i, j, point, word):
    if i <= 0 or j <= 0:
        return
    if i > len(grid) or j > len(grid[0]):
        return

    if point == len(word) - 1:
        return True

    if grid[i][j] == word[point]:
        point += 1
        find_word(grid, i + 1, j, point, word)
        find_word(grid, i, j + 1, point, word)
        find_word(grid, i - 1, j, point, word)
        find_word(grid, i, j - 1, point, word)


# Climbing stairs problem
def stair(n, map_table={}):
    if n in map_table:
        return map_table[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    val = stair(n - 1, map_table) + stair(n - 2, map_table)
    map_table[n] = val
    return val
