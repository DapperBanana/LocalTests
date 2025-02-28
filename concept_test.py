
import random

def show_instructions():
    print("Welcome to the Text-based RPG Game!")
    print("Commands: go [direction], get [item], use [item]")
    print("Valid directions are: north, south, east, west")
    print("---------------------------------------------")

def game_over():
    print("Game over! Thanks for playing.")
    exit()

def main():
    show_instructions()

    inventory = []
    current_room = "start"
    end_room = "end"
    
    while True:
        print("You are in the " + current_room)
        
        if current_room == end_room:
            print("Congratulations, you have reached the end room!")
            break
        else:
            command = input("What would you like to do? ").split()
            action = command[0].lower()
            item = " ".join(command[1:])
            
            if action == "go":
                direction = item
                if direction in ["north", "south", "east", "west"]:
                    print("You went " + direction)
                    current_room = direction
                else:
                    print("Invalid direction, try again.")
            
            elif action == "get":
                if current_room == "start":
                    print("You picked up the " + item)
                    inventory.append(item)
                else:
                    print("You can only pick up items in the starting room.")
            
            elif action == "use":
                if item in inventory:
                    print("You used the " + item)
                    inventory.remove(item)
                else:
                    print("You don't have that item in your inventory.")
            
            else:
                print("Invalid command, try again.")

if __name__ == "__main__":
    main()
