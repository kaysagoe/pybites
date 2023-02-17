from collections import defaultdict
from typing import List


class Matrix:
    def __init__(self, values):
        self.values = values

    def __matmul__(self, right):
        return Matrix(Matrix._multiply(self, right))

    def __rmatmul__(self, left):
        return Matrix(Matrix._multiply(self, left))

    def __imatmul__(self, right):
        self.values = Matrix._multiply(self, right)
        return self

    def __repr__(self) -> str:
        return f'<Matrix values="{repr(self.values)}">'

    @classmethod
    def _transpose_matrix(cls, matrix) -> List[List[int]]:
        result = defaultdict(list)
        for row in matrix.values:
            for index, col in enumerate(row):
                result[index].append(col)
        return list(result.values())

    @classmethod
    def _multiply(cls, left, right):
        result_values = list()
        right_t = cls._transpose_matrix(right)
        for row in left.values:
            row_result = list()
            for right_row in right_t:
                row_result.append(
                    sum([pair[0] * pair[1] for pair in zip(row, right_row)])
                )
            result_values.append(row_result)
        return result_values
