def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Prompt for and add an item
            add_item = input("Add an item to your shopping list: ")
            shopping_list.append(input("Enter the item to add: ").strip().lower())
        elif choice == "2":
            # Prompt for and remove an item
            remove_item = input("What item do you wish to remove? ").strip().lower()
            if remove_item == add_item:
                shopping_list.remove(remove_item)
            else:
                print("Sorry item specified is not on the shopping list.")
        elif choice == "3":
            # Display the shopping list
            for item in shopping_list:
                print(item)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
