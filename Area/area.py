# Calculating area of a rectangle
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