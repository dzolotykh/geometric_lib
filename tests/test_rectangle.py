import unittest
from src.rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(2, 2), 4)
        self.assertAlmostEqual(area(0, 0), 0)
        self.assertAlmostEqual(area(5.5, 5.5), 30.25)

        self.assertRaises(ValueError, area, -1, -1)
    
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(2, 2), 8)
        self.assertAlmostEqual(perimeter(0, 0), 0)
        self.assertAlmostEqual(perimeter(0, 5.5), 0)
        self.assertAlmostEqual(perimeter(5.5, 5.5), 22)

        self.assertRaises(ValueError, perimeter, -1, -1)

    def test_wrong_types(self):
        self.assertRaises(TypeError, area, '2', 2)
        self.assertRaises(TypeError, area, 2, '2')
        self.assertRaises(TypeError, area, '2', '2')
        
        self.assertRaises(TypeError, perimeter, '2', 2)
        self.assertRaises(TypeError, perimeter, 2, '2')
        self.assertRaises(TypeError, perimeter, '2', '2')


if __name__ == '__main__':
    unittest.main()
