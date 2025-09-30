def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Main program with loop
while True:
    num = int(input("Enter a number: "))
    print("-------------------------------------------------------")

    if num < 0:
        print("Sorry, factorial does not exist for negative numbers.")
        print("-------------------------------------------------------")
    else:
        print(f"The factorial of {num} is {factorial(num)}")
        print("Calculation complete! ✅")
        print("-------------------------------------------------------")

    # Ask if the user wants to continue
    choice = input("Do you want to compute another factorial? (yes/no): ").strip().lower()
    print("-------------------------------------------------------")

    if choice != "yes":
        print("Goodbye! 👋")
        print("-------------------------------------------------------")
        break