from math import sqrt
from termcolor import colored
from random import randint

def heron_sqrt(n, tolerance=0.0001):
    if n < 0:
        return None
    if n == 0:
        return 0
    
    x = n / 2.0

    while True:
        new_x = 0.5 * (x + n / x)

        if abs(new_x - x) < tolerance:
            break

        x = new_x
        
    return new_x

TEST_N = randint(0, 9999)

py_sqrt = sqrt(TEST_N)
py_sqrt = f"{py_sqrt:.15f}"
h_sqrt = heron_sqrt(TEST_N)
h_sqrt = f"{h_sqrt:.15f}"

diff_index = 0
for i in range(len(py_sqrt)):
    if py_sqrt[i] != h_sqrt[i]:
        diff_index = i
        break
    
print(f"Test N: {TEST_N}")
if diff_index == 0:
    print(f"py sqrt: {colored(py_sqrt, "green")}")
    print(f"heron sqrt: {colored(h_sqrt, "green")}")    
else:
    print(f"py sqrt: {colored(py_sqrt[:i],"green")}{colored(py_sqrt[i:],"red")}")
    print(f"heron sqrt: {colored(h_sqrt[:i],"green")}{colored(h_sqrt[i:],"red")}")
