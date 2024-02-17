import numpy as np
import re

class MatrixManager():
    """Class responsible for operations on matrices"""

    def filter_data_for_matrix_cells(self, matrix_name: str, data: list) -> list:
        """Filters data to select only relevant matrix cells 
        It checks, if the beginning of the name of each of the list elements
        matches the name of the matrix, like A... or B...
        """

        return [d for d in data if re.match(matrix_name, d[0])]

    def create_zero_matrix(self, rows: int, cols: int) -> np.array:
        """Creates a zero matrix for the size set"""

        return np.zeros([rows, cols])
    
    def assign_values(self, base_matrix: np.array, data: list) -> np.array:
        """Assigns values to the matrix in format ([row_number, col_number], value) """

        matrix_vals = [(re.findall(r'\d+',r[0]),r[1]) for r in data] #checks for numeric values in rNUMBERcNUMBER format

        new_matrix = np.copy(base_matrix)

        for m in matrix_vals:
            new_matrix[int(m[0][0]), int(m[0][1])]= int(m[1])

        return new_matrix
    
    def possible_operations(self, matrix_a: np.array, matrix_b: np.array):
        operations = []
        if matrix_a.shape == matrix_b.shape:
            operations.append("add")
            operations.append("substract")
            
        if matrix_a.shape[1] == matrix_b.shape[0]:
            operations.append("multiply")

        return operations