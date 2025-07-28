import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[9.555555555555555, 0.6666666666666666, 10.666666666666666], [3.5555555555555554, 10.666666666666666, 6.222222222222221], 6.987654320987654],
            'standard deviation': [[3.091206165165235, 0.816496580927726, 3.265986323710904], [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        for key in expected:
            self.assertAlmostEqual(actual[key][2], expected[key][2], msg=f"{key} - flattened")
            for i in range(3):
                self.assertAlmostEqual(actual[key][0][i], expected[key][0][i], msg=f"{key} - axis 0 - index {i}")
                self.assertAlmostEqual(actual[key][1][i], expected[key][1][i], msg=f"{key} - axis 1 - index {i}")
    
    def test_calculate_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            calculate([1, 2, 3, 4])
        self.assertEqual(str(context.exception), "List must contain nine numbers.")

if __name__ == "__main__":
    unittest.main()
