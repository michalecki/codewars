def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    # loops until no fields are unsolved
    while True:
        count = 0
        # loops trough 3x3 squares on the board
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                square = set()
                # collects the digits used inside 3x3 square
                for k in [i - 1, i, i + 1]:
                    for l in [j - 1, j, j + 1]:
                        square.add(puzzle[k][l])
                # goes through 3x3 square and check if there is an unique solution to unsolved field
                for m in [i - 1, i, i + 1]:
                    for n in [j - 1, j, j + 1]:

                        if puzzle[m][n] == 0:
                            field = square.union(set(puzzle[m][:]), set([row[n] for row in puzzle]))
                            count += 1

                            if len(field) == 9:
                                puzzle[m][n] = list(numbers.difference(field))[0]

        if count == 0:
            break

    return puzzle


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# assert solution == sudoku(puzzle)

# sudoku(puzzle)

answer = sudoku(puzzle)

print(answer)
print(solution)
