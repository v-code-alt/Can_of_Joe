while True:    
    user_input = input("Enter integers separated by spaces: ")
    try:
        int_list = [int(x) for x in user_input.split()]
    except ValueError:
        print("Please enter only integers separated by spaces.")
        exit(1)

    unique_ints = sorted(set(int_list), key=int_list.index)
    print("List without duplicates (preserving order):", unique_ints)
    print('-------------------------------------------------------')

    choice = input("Do you want to enter another list? (yes/no): ").strip().lower()
    print('-------------------------------------------------------')
    if choice != "yes":
        print("Goodbye! 👋")
        print('-------------------------------------------------------')
        exit(0)