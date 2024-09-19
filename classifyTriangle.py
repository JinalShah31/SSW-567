import math

def classify_triangle(a, b, c):
    # First, check if the sides form a valid triangle
    if not (a + b > c and a + c > b and b + c > a):
        return "Not a triangle"
    
    # Classify based on the equality of sides
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    
    # Check if it's a right triangle
    if is_right_triangle(a, b, c):
        triangle_type += " and Right"
    
    return triangle_type

def is_right_triangle(a, b, c):
    # Sort the sides to ensure c is the largest side
    sides = sorted([a, b, c])
    # Check the Pythagorean theorem for right triangle
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

def main():
    try:
        # Take user input
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))

        # Classify and display result
        result = classify_triangle(a, b, c)
        print(f"The triangle is classified as: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers for the sides of the triangle.")

if __name__ == '__main__':
    main()
