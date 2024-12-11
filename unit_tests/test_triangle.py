import unittest
from triangle import area
from triangle import perimeter
from math import pi


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 5), 3*5/2)
        self.assertEqual(area(5, 3), 5*3/2)
        self.assertEqual(area(2.3, 4.6), (2.3)*(4.6))
        self.assertEqual(area(3, 1.5), 3*(1.5)/2)

    def test_values(self):
        self.assertRaises(ValueError, area, 1, 0)
        self.assertRaises(ValueError, area, -7, 2)
        self.assertRaises(ValueError, area, -8, -9)
        self.assertRaises(ValueError, perimeter, -6, 3, 5)
        self.assertRaises(ValueError, perimeter, -2, -3, -6)
        self.assertRaises(ValueError, perimeter, 0, 3, 7)

    def test_types(self):
        self.assertRaises(TypeError, area, 3+4j, 1+3j)
        self.assertRaises(TypeError, area, 'two', 'four')
        self.assertRaises(TypeError, area, [5], [4])
        self.assertRaises(TypeError, area, {3, 5}, {4, 7})
        self.assertRaises(TypeError, perimeter, 'two', 3, 'one')
        self.assertRaises(TypeError, perimeter, [2], 3+6j, 11)
        self.assertRaises(TypeError, perimeter, 2, {3}, 9)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3, 4), 2+3+4)
        self.assertEqual(perimeter(2.6, 3.2, 8), 2.6 + 3.2 + 8)
