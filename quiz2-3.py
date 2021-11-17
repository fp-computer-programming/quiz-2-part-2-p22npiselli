# Author: Nolan Piselli
import random

x = list(input("Enter 3 numbers between 1-50 with spaces: "))
y = random.randint(1, 50)
a = random.randint(1, 50)
c = random.randint(1, 50)
b = x[0] + x[2] + x[4]

if b == y + a + c:
    print("You won")
elif b == y + a:
    print("You got two numbers correct")
elif b == y + c:
    print("You got two numbers correct")
elif b == c + a:
    print("You got two numbers correct")
elif b == a:
    print("You got one number correct")
elif b == y:
    print("You got one number correct")
elif b == c:
    print("You got one number correct")
else:
    print("None of your numbers are correct")
