# items by default
backpack = ["sword", "potion", "sword"]

# info menu's
menu_options = {"1": "To add an item","2":  "To remove an item","3":  "Show inventory","4": "Exit"}
removal_options = {"a": "Remove any item","b": "Remove first item","c": "Remove last item"}

# to add item
def to_add_item(item):
    backpack.append(item)
    print(f"Added: {item}")
    
# show inventory
def show_inventory():
    print(f"\nYou have {len(backpack)} item(s).\n")
    for item in backpack:
        print(f" <{item}>")
    print("\n ")

# removal menu
def removal_menu():
    print("\nRemoval options")
    # display removal menu
    for k, v in removal_options.items():
        print(f"[{k}] <{v}>")  
    remove = input("\nChoose an option: ").lower().strip()
    
    # options to remove an item
    if remove == "a":
        item = input("What item do you wanna remove?:\n").lower().strip()
        # checking if the 'item' exist
        if item in backpack:
            print(f"Removed: {item}\n")
            backpack.remove(item)
        else:
            print(f"You don't have the item: {item}. In this backpack...\n ")
    elif remove == "b":
        first_deleted = backpack.pop(0)
        print(f"Removed first item: {first_deleted}\n")
    elif remove == "c":
        second_deleted = backpack.pop(-1)
        print(f"Removed last item: {second_deleted}\n")
    else:
         print("Invalid option")
 
# main.. have to be running all the time
def home():
    while True:
        # welcoming and displaying home menu
        print("="*28)
        print("\tBackpack")
        print("="*28)
        for k, v in menu_options.items():
            print(f"[{k}] <{v}>")
        option = input("\nChoose an option: ").strip()
		
        # interactivity from the home menu
        if option == "1":
            to_add_item(input("What item do you wanna add?: "))
        elif option == "2":
            removal_menu()
        elif option == "3":
            show_inventory()
        elif option == "4":
            print("Exit")
            break

# calling the main function
home()
# 4h doing this
