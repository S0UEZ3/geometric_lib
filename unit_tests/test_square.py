import unittest
from square import area
from square import perimeter
from math import pi


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), 3*3)
        self.assertEqual(area(1), 1*1)
        self.assertEqual(area(2.5), (2.5)*(2.5))

    def test_values(self):
        self.assertRaises(ValueError, area, 0)
        self.assertRaises(ValueError, area, -3)
        self.assertRaises(ValueError, area, -3.5)

    def test_types(self):
        self.assertRaises(TypeError, area, 2+3j)
        self.assertRaises(TypeError, area, 'four')
        self.assertRaises(TypeError, area, [6])
        self.assertRaises(TypeError, area, False)
        self.assertRaises(TypeError, area, [10, 31])

    def test_perimeter(self):
        self.assertEqual(perimeter(3), 4*3)
        self.assertEqual(perimeter(1), 4*1)
        self.assertEqual(perimeter(2.5), 4*(2.5))

    def test_values(self):
        self.assertRaises(ValueError, perimeter, 0)
        self.assertRaises(ValueError, perimeter, -3)
        self.assertRaises(ValueError, perimeter, -3.5)

    def test_types(self):
        self.assertRaises(TypeError, perimeter, 2+3j)
        self.assertRaises(TypeError, perimeter, 'four')
        self.assertRaises(TypeError, perimeter, [6])
        self.assertRaises(TypeError, perimeter, False)
        self.assertRaises(TypeError, perimeter, [10, 31])
