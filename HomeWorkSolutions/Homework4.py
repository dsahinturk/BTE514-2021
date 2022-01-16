def read_vectors():
    v1 = input("Input vector 1 as a whole line: ")
    v2 = input("Input vector 2 as a whole line: ")

    v_1 = [int(i) for i in v1.split()]
    v_2 = [int(i) for i in v2.split()]

    #for i in zip(v1.split(), v2.split()):
    #    v_1.append(int(i[0]))
    #    v_2.append(int(i[1]))

    return v_1, v_2


def dot_product(v_1, v_2):
    sum = 0
    if len(v_1) != len(v_2):
        raise Exception("VectorSizeError")

    for tup in zip(v_1, v_2):
        sum += tup[0]*tup[1]

    return sum

def read_matrix():
    print("Input matrix rows line by line, input a single q to stop")

    rows = []

    while True:
        rows.append(input())
        if rows[-1][0] == "q":
            break
    del rows[-1]

    matrix = []
    for line in rows:
        matrix.append([int(i) for i in line.split()])

    return matrix


def is_symmetric(matrix, skew = False):
    if len(matrix) != len(matrix[0]):
        return False

    factor = -1 if skew else 1

    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != factor*matrix[j][i]:
                return False

    return True


def print_transpose(matrix):
    transpose = []
    for i in range(len(matrix[0])):
        transpose.append(len(matrix)*[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[j][i] = matrix[i][j]

    print(transpose)


def trace(matrix):
    if len(matrix) != len(matrix[0]):
        raise Exception("VectorSizeError")

    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]

    return sum


def test_q1():
    print("******************* Soru 1 cozum ******************")
    var = read_vectors()
    print(dot_product(var[0], var[1]))
    print("******************* Soru 1 cozum ******************\n")


def test_q2():
    print("******************* Soru 2 cozum ******************")
    print(is_symmetric([[1, 2, 3], [-2, 5, -6], [-3, 6, 9]], True))
    print_transpose([[1, 2, 3], [-2, 5, -6]])
    print(trace([[1, 2, 3], [-2, 5, -6], [-3, 6, 9]]))
    print("******************* Soru 2 cozum ******************\n")
