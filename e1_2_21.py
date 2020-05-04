import sys
import math

p = float(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])

# применяем формулу сложеного процента x = P*e**(r * t)
print(p * math.e ** (r * t))