import unittest
from src.circle import area, perimeter
import math

class TestCircle(unittest.TestCase):
    def test_area(self):
        params = [(1, math.pi), (0, 0), (2.1, math.pi * 2.1**2)]
        for radius, expected_area in params:
            with self.subTest(radius=radius, expected_area=expected_area):
                self.assertAlmostEqual(area(radius), expected_area)
    
    def test_negative_radius(self):
        self.assertRaises(ValueError, area, -1)
    
    def test_perimeter(self):
        params = [(1, 2 * math.pi), (0, 0), (2.1, 2 * math.pi * 2.1)]
        for radius, expected_perimeter in params:
            with self.subTest(radius=radius, expected_perimeter=expected_perimeter):
                self.assertAlmostEqual(perimeter(radius), expected_perimeter)
    
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
