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

