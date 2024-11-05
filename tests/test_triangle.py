import unittest
from src.triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(2, 2), 2)
        self.assertAlmostEqual(area(0, 0), 0)
        self.assertAlmostEqual(area(5.5, 5.5), 15.125)
        self.assertAlmostEqual(area(3, 4), 6)

        self.assertRaises(ValueError, area, -1, -1)
    
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(2, 2, 2), 6)
        self.assertAlmostEqual(perimeter(0, 0, 0), 0)
        self.assertAlmostEqual(perimeter(5.5, 5.5, 5.5), 16.5)

        self.assertRaises(ValueError, perimeter, -1, -1, -1)
        self.assertRaises(ValueError, perimeter, 3, 4, 228)

    def test_wrong_types(self):
        self.assertRaises(TypeError, area, '2', 2)
        self.assertRaises(TypeError, area, 2, '2')
        self.assertRaises(TypeError, area, '2', '2')

        self.assertRaises(TypeError, perimeter, '2', 2, 2)
        self.assertRaises(TypeError, perimeter, 2, '2', 2)
        self.assertRaises(TypeError, perimeter, 2, 2, '2')
        self.assertRaises(TypeError, perimeter, '2', '2', '2')

if __name__ == '__main__':
    unittest.main()
