import unittest
from src.square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(2), 4)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(5.5), 30.25)

        self.assertRaises(ValueError, area, -1)
    
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(2), 8)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(5.5), 22)

        self.assertRaises(ValueError, perimeter, -1)

    def test_wrong_types(self):
        self.assertRaises(TypeError, area, '2')
        self.assertRaises(TypeError, perimeter, '2')


if __name__ == '__main__':
    unittest.main()
