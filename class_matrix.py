from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, rows):
        self.rows = copy.deepcopy(rows)

    def __str__(self):
        b = []
        for i in self.rows:
            b.append('\t'.join(map(str, i)))
        return '\n'.join(b)

    def size(self):
        return (len(self.rows), len(self.rows[0]))

    def __add__(self, other):
        if self.size() == other.size():
            x, y = len(self.rows), len(self.rows[0])
            a = []
            for i in range(x):
                a.append([])
                for j in range(y):
                    a[i].append(self.rows[i][j] + other.rows[i][j])
            return Matrix(a)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x, y = len(self.rows), len(self.rows[0])
            a = []
            for i in range(x):
                a.append([])
                for j in range(y):
                    a[i].append(self.rows[i][j] * num)
            return Matrix(a)
        elif isinstance(other, Matrix):
            matr1 = self.rows
            matr2 = other.rows
            if len(matr1[0]) == len(matr2):
                a = []
                row = []
                for i in range(len(matr1)):
                    for j in range(len(matr2[0])):
                        elem = 0
                        for k in range(len(matr2)):
                            elem = elem + matr1[i][k] * matr2[k][j]
                        row.append(elem)
                    a.append(row)
                    row = []
                return Matrix(a)
            else:
                raise MatrixError(self, other)

    def __rmul__(self, num):
        x, y = len(self.rows), len(self.rows[0])
        a = []
        for i in range(x):
            a.append([])
            for j in range(y):
                a[i].append(self.rows[i][j] * num)
        return Matrix(a)

    def transpose(self):
        x, y = len(self.rows), len(self.rows[0])
        self.rows = [[self.rows[j][i] for j in range(x)] for i in range(y)]
        return self

    def transposed(self):
        x, y = len(self.rows), len(self.rows[0])
        a = [[self.rows[i][j] for i in range(x)] for j in range(y)]
        return Matrix(a)


class SquareMatrix(Matrix):
    def __pow__(self, num):
        x = len(self.rows)
        a = []
        for i in range(x):
            row = []
            for j in range(x):
                if j == i:
                    row.append(1)
                else:
                    row.append(0)
            a.append(row)
            row = []
        base = self
        result = Matrix(a)
        while num:
            if num % 2 == 1:
                result = result * base
            base = base * base
            num = num // 2
        return result


exec(stdin.read())