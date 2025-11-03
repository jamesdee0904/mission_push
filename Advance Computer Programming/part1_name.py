def main():
    fruits = []

    num_fruits = int(input("Enter number of fruits: "))

    for i in range(num_fruits):
        fruit = input("Enter fruit: ").strip().lower()
        fruits.append(fruit)

    while True:
        print();
        command = input("Enter Command: ").strip().upper()

        if command.startswith("COUNT"):
            parts = command.split()
            if len(parts) > 1:
                fruit = parts[1].lower()
                count = fruits.count(fruit)
                print(f"{fruit} appears {count} time(s)")
            else:
                print("Please specify a fruit to count.")

        elif command.startswith("ADD"):
            parts = command.split()
            if len(parts) > 1:
                fruit = parts[1].lower()
                fruits.append(fruit)
                print(f"{fruit} added")
            else:
                print("Please specify a fruit to add.")
                

        elif command.startswith("REMOVE"):
            parts = command.split()
            if len(parts) > 1:
                fruit = parts[1].lower()
                if fruit in fruits:
                    fruits.remove(fruit)
                    print(f"{fruit} removed")
                else:
                    print(f"{fruit} not found")
            else:
                print("Please specify a fruit to remove.")

        elif command == "UNIQUE":
            unique_fruits = set(fruits)
            print(f"Unique fruits: {unique_fruits}")

        elif command == "END":
            print("Program ended.")
            break

        else:
            print("Invalid command. Please try again.")

main()
