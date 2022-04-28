# Calculating area of a rectangle
from cmath import pi


def area_rectangle(length: float, width: float) -> float:

    if length < 0 or width < 0:
        raise ValueError("area_rectangle() only accepts non-negative values")
    return length * width 
    
print(f"Rectangle: {area_rectangle (10 ,20) = } cm squared")

# Calculating area of rhombus

def area_rhombus(diagonal_1: float, diagonal_2: float) -> float:
    
    if diagonal_1 < 0 or diagonal_2 < 0:
        raise ValueError("area_rhombus() only accepts non-negative values")
    return 1 / 2 * diagonal_1 * diagonal_2

print(f"Rhombus: {area_rhombus (10, 20) = } cm squared")

# Calculating area of circle

def area_circle(radius: float) -> float:
   pi = 3.142
   if radius < 0:
        raise ValueError("area_circle() only accepts non-negative values")
   return pi * radius**2

print(f"Circle: {area_circle(20) = } cm squared")   

# Calculating area of ellipse
def area_ellipse(radius_x: float, radius_y: float) -> float:

    if radius_x < 0 or radius_y < 0:
        raise ValueError("area_ellipse() only accepts non-negative values")
    return pi * radius_x * radius_y

print(f"Ellipse: {area_ellipse(20,30) = }")    
