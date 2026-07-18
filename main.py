from parser import parse_resume

while True:

    print("\n")
    print("=" * 40)
    print("RESUME PARSER")
    print("=" * 40)

    print("1. Parse Resume")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        filename = input("Enter Resume File Name: ")

        parse_resume(filename)

    elif choice == "2":

        print("Thank You...")
        break

    else:

        print("Invalid Choice")