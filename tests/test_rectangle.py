import unittest
from src.rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area(self):
        params = [(1, 1, 1), (0, 0, 0), (2.1, 2.1, 4.41)]
        for a, b, expected_area in params:
            with self.subTest(a=a, b=b, expected_area=expected_area):
                self.assertAlmostEqual(area(a, b), expected_area)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -1, -1)
    
    def test_perimeter(self):
        params = [(1, 1, 4), (0, 0, 0), (2.1, 2.1, 8.4)]
        for a, b, expected_perimeter in params:
            with self.subTest(a=a, b=b, expected_perimeter=expected_perimeter):
                self.assertAlmostEqual(perimeter(a, b), expected_perimeter)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1, -1)

    def test_wrong_types_area(self):
        params = [(1, '2'), ('2', 2), ('2', '2')]
        for a, b in params:
            with self.subTest(a=a, b=b):
                self.assertRaises(TypeError, area, a, b)
    
    def test_wrong_types_perimeter(self):
        params = [(1, '2'), ('2', 2), ('2', '2')]
        for a, b in params:
            with self.subTest(a=a, b=b):
                self.assertRaises(TypeError, perimeter, a, b)


if __name__ == '__main__':
    unittest.main()
