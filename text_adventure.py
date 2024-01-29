import time

def intro():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at the entrance of a mysterious cave.")
    time.sleep(1)
    print("Your goal is to navigate through the cave and reach the treasure at the end.")
    time.sleep(1)

def make_choice(choices):
    while True:
        print("\nChoose your action:")
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")

        try:
            user_input = int(input("Enter the number of your choice: "))
            if 1 <= user_input <= len(choices):
                return user_input
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def cave_path():
    print("\nYou enter the cave and come across a fork in the path.")
    time.sleep(1)
    print("Which path will you take?")
    
    choices = ["Go left", "Go right"]
    user_choice = make_choice(choices)
    
    if user_choice == 1:
        print("\nYou chose to go left.")
        time.sleep(1)
        print("You encounter a pack of hungry wolves.")
        time.sleep(1)
        print("What will you do?")
        
        choices = ["Fight the wolves", "Try to sneak past them"]
        user_choice = make_choice(choices)
        
        if user_choice == 1:
            print("\nYou choose to fight the wolves.")
            time.sleep(1)
            print("It's a tough battle, but you manage to defeat them.")
            return True
        else:
            print("\nYou choose to sneak past the wolves.")
            time.sleep(1)
            print("You successfully sneak past them.")
            return True
    else:
        print("\nYou chose to go right.")
        time.sleep(1)
        print("You discover a hidden shortcut that leads directly to the treasure.")
        return True

def treasure_room():
    print("\nCongratulations! You've reached the treasure room.")
    time.sleep(1)
    print("You open the chest and find a pile of gold and precious gems.")
    time.sleep(1)
    print("You've successfully completed the adventure!")

def game():
    intro()
    
    if cave_path():
        treasure_room()

if __name__ == "__main__":
    game()
