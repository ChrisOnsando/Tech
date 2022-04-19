import cmath
import math

# Return cosine of different numbers
print(math.cos(0.00))
print(math.cos(-1.23))
print(math.cos(10))
print(math.cos(3.1423))

# Return the inverse hyperbolic cosine
print(math.acosh(7))
print(math.acosh(56))
print(math.acosh(2.78))

# Return the arc sine of numbers
print(math.asin(0.55))
print(math.asin(0))
print(math.asin(1))

# Return the arc tangent of numbers
print(math.atan(0.39))

# Rounds a number upward to its nearest integer
print(math.ceil(1.4))
print(math.ceil(5.3))
print(math.ceil(22.6))

# Rounds a number down to the nearest integer
print(math.floor(0.6))
print(math.floor(1.55))
print(math.floor(-5.5))
print(math.floor(10.9))

# Find the arc tangent of a complex number
print(cmath.atan(2 + 3j))

# Compare the closeness of two complex values using relative tolerance
print(cmath.isclose(10 + 5j, 11.5 + 2j))
print(cmath.isclose(10+5j,10.01 + 5j))

# Print log value of some given parameters
print(cmath.log(1 + 1j))
print(cmath.log(1, 2.5))

# Print base-10 log value of complex numbers
print(cmath.log10(2 +3j))
print(cmath.log10(1 + 2j))

# Print phase of some given parameters
print(cmath.phase(2 + 3j))

# Convert a polar coordinate to rectangular form
print(cmath.rect(3.15252626152617, 1.2828891889199))

# Returns square root of a complex number
print(cmath.sqrt(2 + 3j))
print(cmath.sqrt(15))