
def set_zero(matrix):
    row_flag = [0 for i in range(len(matrix))]
    col_flag = [0 for i in range(len(matrix[0]))]
    # Scan matrix for zero
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_flag[i] = 1
                col_flag[j] = 1
    # nullify rows
    for i in range(len(row_flag)):
        if row_flag[i] == 1:
            nullify_row(matrix, i)
    # nullify columns
    for i in range(len(col_flag)):
        if col_flag[i] == 1:
            nullify_col(matrix, i)

    print()
    print_matrix(matrix)

def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0
def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def print_matrix(matrix):
    for i in range(len(matrix)):
        buffer = []
        for j in range(len(matrix[0])):
            buffer.append(matrix[i][j])
        print(buffer)

if __name__ == "__main__":
    n = 5
    ix = 11
    data = [list(range(i, i+n)) for i in range(ix, ix+n*n, n)]
    zero_positions = [(0, 0), (2, 2), [4, 4]]
    for pos in zero_positions:
        data[pos[0]][pos[1]] = 0
    print_matrix(data)
    set_zero(data)
