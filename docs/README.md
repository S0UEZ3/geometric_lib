# Geometric Lib


### Description
Geometric Lib is library for python that provides
simple workflow with geometric structres
This library contains functions to calculate parametres of
squares and circles based on values provided by users.

### Functions
---
#### Circle 
* ```
    def area(r):
    return math.pi * r * r
    ```
    Function takes variable a as circle's radius and return it's square multiplied on pi.

* ```
    def perimeter(r):
    return 2 * math.pi * r
    ```
    Function takes variable a as circle's radius and return it's value multiplied by 2 and pi.

#### Square 
* ```
    def area(a):
    return a * a
    ```
    Function takes value of square's side and return square of this argument.

* ```
    def perimeter(a):
    return 4 * a
    ```
    function takes value of square's side and returns it's value multipled by 4.

#### Circle 
* ```
    def area(a, h): 
    return a * h / 2 
    ```
    Function takes a as size of width of and h as height and returns it's multimplication devided by 2.

* ```
    def perimeter(a, b, c): 
    return a + b + c 
    ```
    Function takes sizes of triangle sides and return their sum.


### Tests
---
#### Circle tests
```
class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), pi*3**2)
        self.assertEqual(area(1), pi)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(2.5), pi*2.5**2)
    def test_values(self):
        self.assertRaises(ValueError, area, -3)
        self.assertRaises(ValueError, area, -3.5)
    def test_types(self):
        self.assertRaises(TypeError, area, 2+3j)
        self.assertRaises(TypeError, area, 'four')
        self.assertRaises(TypeError, area, [10, 31])
        self.assertRaises(TypeError, area, [6])
        self.assertRaises(TypeError, area, False)

    def test_perimeter(self):
        self.assertEqual(perimeter(3), 2*pi*3)
        self.assertEqual(perimeter(1), 2*pi)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(2.5), 2*pi*2.5)
    def test_values(self):
        self.assertRaises(ValueError, perimeter, -3)
        self.assertRaises(ValueError, perimeter, -3.5)
    def test_types(self):
        self.assertRaises(TypeError, perimeter, 2+3j)
        self.assertRaises(TypeError, perimeter, 'four')
        self.assertRaises(TypeError, perimeter, [10, 31])
        self.assertRaises(TypeError, perimeter, [6])
        self.assertRaises(TypeError, perimeter, False)
```

#### Square tests 
```
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
```

#### Triangle tests
```
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
    def test_types(self):
        self.assertRaises(TypeError, area, 3+4j, 1+3j)
        self.assertRaises(TypeError, area, 'two', 'four')
        self.assertRaises(TypeError, area, [5], [4])
        self.assertRaises(TypeError, area, {3,5}, {4,7})

    def test_perimeter(self):
        self.assertEqual(perimeter(2,3,4), 2+3+4)
        self.assertEqual(perimeter(2.6, 3.2, 8), 2.6 + 3.2 + 8)
    def test_values(self):
        self.assertRaises(ValueError, perimeter, -6, 3, 5)
        self.assertRaises(ValueError, perimeter, -2, -3, -6)
        self.assertRaises(ValueError, perimeter, 0, 3, 7)
    def test_types(self):
        self.assertRaises(TypeError, perimeter, 'two', 3, 'one')
        self.assertRaises(TypeError, perimeter, [2], 3+6j, 11)
        self.assertRaises(TypeError, perimeter, 2, {3}, 9)
```

### Tests Result
| Name | Tests Runned | Tests Failed | Success | Run Time |
| --- | --- | --- | --- | --- |
| circle_tests | 4 |  2 | 50% | 0.002 |
| square_tests | 4 |  2 | 50% | 0.001 |
| triangle_tests | 4 |  2 | 50% | 0.001 |

---
### Commit History


* ff5683b (HEAD -> main) docs: description for each function provided
    * 86edb1c (origin/release) L-05: Update Docs. Add user agreement info
        * 438b89a L-05: Add user agreement
        * 6adb962 L-03: Docs added
            * 3049431 (origin/feature) L-04: Add rectangle.py
    * b5b0fae (origin/develop) L-04: Update docs for calculate.py
        * d76db2a L-04: Add calculate.py
        * 51c40eb L-04: Doc updated for triangle
        * d080c78 L-04: Triangle added
* d078c8d (origin/main, origin/HEAD) L-03: Docs added
* 8ba9aeb L-03: Circle and square added

