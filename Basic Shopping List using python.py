def display_list(shopping_list):
    print("Your Shopping List:")
    for item in shopping_list:
        print("- " + item)

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(item + " has been added to your shopping list.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(item + " has been removed from your shopping list.")
    else:
        print(item + " is not in your shopping list.")

def main():
    shopping_list = []
    while True:
        print("\nMenu:")
        print("1. Display Shopping List")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            display_list(shopping_list)
        elif choice == '2':
            item = input("Enter the item you want to add: ")
            add_item(shopping_list, item)
        elif choice == '3':
            item = input("Enter the item you want to remove: ")
            remove_item(shopping_list, item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
