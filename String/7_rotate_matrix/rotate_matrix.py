import unittest

def rotate(matrix):
    print_matrix(matrix)
    n = len(matrix[0])
    for layer in range(int(n/2)):
        first = layer
        last = n - 1 - first
        for i in range(first, last):
            offset = i - first
            # Temporary save first of the 4 values
            top = matrix[first][i]
            # Save left to top
            matrix[first][i] = matrix[last-offset][first]
            # save bottom to left
            matrix[last-offset][first] = matrix[last][last-offset]
            # save right to bottom
            matrix[last][last-offset] = matrix[first+offset][last]
            # save top to right
            matrix[first+offset][last] = top
    print()
    print_matrix(matrix)
    return matrix


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
    rotate(data)
