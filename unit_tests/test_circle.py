import unittest
from circle import area
from circle import perimeter
from math import pi


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), pi *3**2)
        self.assertEqual(area(1), pi)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(2.5), pi *2.5**2)

    def test_values(self):
        self.assertRaises(ValueError, area, -3)
        self.assertRaises(ValueError, area, -3.5)

    def test_types(self):
        self.assertRaises(TypeError, area, 2 +3j)
        self.assertRaises(TypeError, area, 'four')
        self.assertRaises(TypeError, area, [10, 31])
        self.assertRaises(TypeError, area, [6])
        self.assertRaises(TypeError, area, False)

    def test_perimeter(self):
        self.assertEqual(perimeter(3), 2 *pi *3)
        self.assertEqual(perimeter(1), 2 *pi)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(2.5), 2 *pi *2.5)
