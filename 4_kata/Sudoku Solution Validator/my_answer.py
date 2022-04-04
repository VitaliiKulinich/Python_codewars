def valid_solution(board):
    result_sum = 45

    for row in board:
        if sum(row) != result_sum:
            return False

    for i in range(9):
        column_sum = 0
        for row in board:
            column_sum += row[i]
        if column_sum != result_sum:
            return False

        for a in range(3):
            for b in range(3):

                square_sum = 0
                for i in range(0 + 3 * a, 3 + 3 * a):
                    for k in range(0 + 3 * b, 3 + 3 * b):
                        square_sum += board[i][k]
                if square_sum != result_sum:
                    return False

    return True

print(valid_solution([ [5, 3, 4, 6, 7, 8, 9, 1, 2],
                       [6, 7, 2, 1, 9, 5, 3, 4, 8],
                       [1, 9, 8, 3, 4, 2, 5, 6, 7],
                       [8, 5, 9, 7, 6, 1, 4, 2, 3],
                       [4, 2, 6, 8, 5, 3, 7, 9, 1],
                       [7, 1, 3, 9, 2, 4, 8, 5, 6],
                       [9, 6, 1, 5, 3, 7, 2, 8, 4],
                       [2, 8, 7, 4, 1, 9, 6, 3, 5],
                       [3, 4, 5, 2, 8, 6, 1, 7, 9]]))