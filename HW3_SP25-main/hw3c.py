import math
#chatgpt
"""This program solves a system of linear equations
using either Cholesky’s or the Doolittle method dependent on its symmetry and
sign"""
def is_symmetric(A):
    #checking symmetry of Matrix
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] != A[j][i]:
                return False
    return True


def is_positive_definite(A):
    #checking if matrix A is >0
    try:
        for i in range(1, len(A) + 1):
            determinant = determinant_of_matrix([row[:i] for row in A[:i]])
            if determinant <= 0:
                return False
        return True
    except:
        return False


def determinant_of_matrix(A):
    #finding determinant of matrix using Laplace
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    determinant = 0
    for c in range(len(A)):
        sub_matrix = [row[:c] + row[c + 1:] for row in A[1:]]
        determinant += ((-1) ** c) * A[0][c] * determinant_of_matrix(sub_matrix)

    return determinant


def cholesky_decomposition(A):
    #performs cholesky decomp
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            sum_val = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(A[i][i] - sum_val)
            else:
                L[i][j] = (A[i][j] - sum_val) / L[j][j]
    return L


def forward_substitution(L, b):
    #Solves Ly = b using forward substitution
    n = len(L)
    y = [0] * n
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
    return y


def backward_substitution(U, y):
    #Solves Ux = y using backward substitution.
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x


def cholesky_solve(A, b):
    #Solve Ax = b using Cholesky decomposition.
    L = cholesky_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution([[L[j][i] for j in range(len(L))] for i in range(len(L))], y)
    return x


def doolittle_solve(A, b):
    #Solve Ax = b using Doolittle's LU decomposition.
    n = len(A)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x


def main():
    print("This program solves Ax = b using Cholesky or Doolittle method (math module only).")
#system of equations
    matrices = (([
      [1, -1, 3, 2],
      [-1, 5, -5, -2],
      [3, -5, 19, 3],
      [2, -2, 3, 21]],
                        [15, -35, 94, 1]),
    ([[4, 2, 4, 0],
      [2, 2, 3, 2],
      [4, 3, 6, 3],
      [0, 2, 3, 9]],
                        [20, 36, 60, 122]))

    for i, (A, b) in enumerate(matrices):
        print(f"\nSolving System {i + 1}:")

        if is_symmetric(A) and is_positive_definite(A):
            print("Using Cholesky decomposition...")
            x = cholesky_solve(A, b)
        else:
            print("Using Doolittle's method...")
            x = doolittle_solve(A, b)

        print(f"Solution vector x: {x}")


if __name__ == "__main__":
    main()
