def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area
radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print(f"The area of the circle is: {area}")