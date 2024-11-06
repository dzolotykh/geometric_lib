import unittest
from src.triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area(self):
        params = [(1, 1, 0.5), (0, 0, 0), (2.1, 2.1, 2.205)]
        for a, b, expected_area in params:
            with self.subTest(a=a, b=b, expected_area=expected_area):
                self.assertAlmostEqual(area(a, b), expected_area)
    
    def test_negative_area(self):
        self.assertRaises(ValueError, area, -1, -1)
    
    def test_perimeter(self):
        params = [(1, 1, 1, 3), (0, 0, 1, 0), (2.1, 2.1, 2.1, 6.3)]
        for a, b, c, expected_perimeter in params:
            with self.subTest(a=a, b=b, c=c, expected_perimeter=expected_perimeter):
                self.assertAlmostEqual(perimeter(a, b, c), expected_perimeter)
                
    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1, -1, 100)

    def test_wrong_types_area(self):
        params = [(1, '2'), ('2', 2), ('2', '2')]
        for a, b in params:
            with self.subTest(a=a, b=b):
                self.assertRaises(TypeError, area, a, b)
    
    def test_wrong_types_perimeter(self):
        params = [(1, '2', 3), ([1], '2', 2), (1, 2, None)]
        for a, b, c in params:
            with self.subTest(a=a, b=b, c=c):
                self.assertRaises(TypeError, perimeter, a, b, c)

if __name__ == '__main__':
    unittest.main()
