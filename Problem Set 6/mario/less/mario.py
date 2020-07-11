# importing get_int function from cs50 library
from cs50 import get_int
# prompting user for input between 1 and 8 inclusively
while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break
# for loop for building half pyramid
for i in range(1, n + 1):
    print(" " * (n - i) + i * '#')