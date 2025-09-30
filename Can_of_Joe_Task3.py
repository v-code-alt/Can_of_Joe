import math

while True:
    radius = float(input("Enter the radius of the circle: "))
    print('-------------------------------------------------------')

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius

    print(f"Area: {area:.2f}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Diameter: {diameter:.2f}")
    print('-------------------------------------------------------')

    choice = input("Do you want to enter another radius? (yes/no): ").strip().lower()
    print('-------------------------------------------------------')
    if choice != "yes":
        print("Goodbye! 👋")
        print('-------------------------------------------------------')
        exit(0)