from matrix_manager import MatrixManager
import unittest
import numpy as np

class TestMatrixManager(unittest.TestCase):
    """Tests for matrix manager"""
    
    def test_filter_data_for_matrix_cells(self):
        "Tests if the matrix manager returns data only for relevant cells"
        manager = MatrixManager()
        cells = manager.filter_data_for_matrix_cells(
            "A",
            [('rows_a', '3'), ('cols_a', '3'), ('rows_b', '3'), 
            ('cols_b', '3'), ('Ar0c0', '0'), ('Ar0c1', '3'), 
            ('Ar0c2', '5')]
        )
        assert cells == [('Ar0c0', '0'), ('Ar0c1', '3'), ('Ar0c2', '5')]

    def test_create_zero_matrix(self):
        """Checks if the new created zero matrix with defined number of rows and columns is a correct zero matrix"""
        manager = MatrixManager()
        matrix = manager.create_zero_matrix(4,8)
        np.testing.assert_array_equal(matrix,np.zeros([4,8]))

    def test_assign_values(self):
        """Tests assignment of values to the matrix"""
        
        manager = MatrixManager()
        zeros = np.zeros([2,2])

        changed = manager.assign_values(zeros,
                              [('Ar0c0', '1'),('Ar0c1', '2'), ('Ar1c0', '3'), ('Ar1c1', '4')])
        
        np.testing.assert_array_equal(changed,np.reshape(np.arange(1,5),[2,2]))

    def test_possible_operations(self):
        """Test for possible operations between two matrices
        for 2x2 and 2x1 it should accept only multiplication"""

        manager = MatrixManager()

        matrix_a = np.array([[3,5],[2,3]])
        matrix_b = np.array([[3],[2]])

        assert manager.possible_operations(matrix_a,matrix_b) == ["multiply"]