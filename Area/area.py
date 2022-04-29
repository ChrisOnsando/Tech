from cmath import pi, sqrt

# Calculating area of a rectangle.
def area_of_rectangle(length: float, width: float) -> float:

    if length < 0 or width < 0:
        raise ValueError("area_of_rectangle() only accepts non-negative values")
    return length * width 
    
print(f"Rectangle: {area_of_rectangle (10 ,20) = } cm squared")

# Calculating area of rhombus.
def area_of_rhombus(diagonal_1: float, diagonal_2: float) -> float:
    
    if diagonal_1 < 0 or diagonal_2 < 0:
        raise ValueError("area_of_rhombus() only accepts non-negative values")
    return 1 / 2 * diagonal_1 * diagonal_2

print(f"Rhombus: {area_of_rhombus (10, 20) = } cm squared")

# Calculating area of circle.
def area_of_circle(radius: float) -> float:
   pi = 3.142
   if radius < 0:
        raise ValueError("area_of_circle() only accepts non-negative values")
   return pi * radius**2

print(f"Circle: {area_of_circle(20) = } cm squared")   

# Calculating area of ellipse.
def area_of_ellipse(radius_x: float, radius_y: float) -> float:

    if radius_x < 0 or radius_y < 0:
        raise ValueError("area_of_ellipse() only accepts non-negative values")
    return pi * radius_x * radius_y

print(f"Ellipse: {area_of_ellipse(20,30) = } cm squared")    

# Calculating area of trapezium.
def area_of_trapezium(base1: float, base2: float, height: float) -> float:
    
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("area_of_trapezium() only accepts non-negative values")
    return 1 / 2 * (base1 + base2) * height

print(f"Trapezium: {area_of_trapezium(10, 20, 30) = } cm squared")

# Calculating area of triangle.
def area_of_triangle(base: float, height: float) -> float:
  
  if base < 0 or height < 0:
        raise ValueError("area_of_triangle() only accepts non-negative values")
  return (base * height) / 2

print(f"Triangle: {area_of_triangle(10, 10) = } cm squared")

# Calculating area of triangle when the length of 3 sides are known.
def area_of_triangle_three_sides(side1: float, side2: float, side3: float) -> float:
    
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("area_of_triangle_three_sides() only accepts non-negative values")
    elif side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
        raise ValueError("Given three sides do not form a triangle")
    semi_perimeter = (side1 + side2 + side3) / 2
    area = sqrt(
        semi_perimeter
        * (semi_perimeter - side1)
        * (semi_perimeter - side2)
        * (semi_perimeter - side3)
    )
    return area

print(f"Triangle: {area_of_triangle_three_sides(5, 12, 13) = } cm squared")

# Calculating area of parallelogram.
def area_of_parallelogram(base: float, height: float) -> float:
    
    if base < 0 or height < 0:
        raise ValueError("area_of_parallelogram() only accepts non-negative values")
    return base * height

print(f"Parallelogram: {area_of_parallelogram(10, 20) = } cm squared")   

# Calculating area of a square.
def area_of_square(side_length: float) -> float:
    
    if side_length < 0:
        raise ValueError("area_of_square() only accepts non-negative values")
    return side_length**2
 
print(f"Square: {area_of_square(20) = } cm squared")