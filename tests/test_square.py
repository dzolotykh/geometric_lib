import unittest
from src.square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area(self):
        params  = [(1, 1), (0, 0), (2.1, 4.41)]
        for a, expected_area in params:
            with self.subTest(a=a, expected_area=expected_area):
                self.assertAlmostEqual(area(a), expected_area)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -1)
    
    def test_perimeter(self):
        params = [(1, 4), (0, 0), (2.1, 8.4)]
        for a, expected_perimeter in params:
            with self.subTest(a=a, expected_perimeter=expected_perimeter):
                self.assertAlmostEqual(perimeter(a), expected_perimeter)

    def test_negative_perimeter(self):
            self.assertRaises(ValueError, perimeter, -1)

    def test_wrong_types_area(self):
        params = ['1', [1], True]
        for param in params:
            with self.subTest(param=param):
                self.assertRaises(TypeError, area, param)

    def test_wrong_types_perimeter(self):
            params = ['1', [1], True]
            for param in params:
                with self.subTest(param=param):
                    self.assertRaises(TypeError, perimeter, param)


if __name__ == '__main__':
    unittest.main()
