"""Project Two starter for the student's text-based adventure game."""

# Ginnette Maldonado


def show_instructions():
    """Display the game objective and available commands."""
    print("Haunted Mansion Adventure Game")
    print("Collect all 6 magical items to defeat the Ghost King.")
    print("Move: go North, go South, go East, go West")
    print("Collect items: get Item Name")
    print("Type Exit to quit the game.")

def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("--------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)
    if "item" in room[current_room]:
        print("You see a", rooms[current_room]["item])
    print("--------------------")
def main():
    """Run the main gameplay loop."""
   rooms = {
       "Entrance Hall": {"West": "Kitchen"},
       "Kitchen": {"East": "Entrance Hall",
                   "North": "Library",
                   "item": "Silver Key"},
       "Library": {"South": "Kitchen",
                   "North": "Bedroom",
                   "item": "Magic Book"},
       "Bedroom": {"South": "Library",
                   "East": "Dining Room",
                   "item": "Crystal"},
       "Dining Room": {"West": "Bedroom",
                       "East": "Basement",
                       "item": "Golden Candle"},
       "Basement": {"West": "Dining Room",
                    "South": "Garden",
                    "item": "Magic Shield"},
       "Garden": {"North": "Basement",
                  "West": "Throne Room",
                  "item": "Sacred Flower"},
       "THrone Room": {"East": "Garden"}
       }
       current_room = "Entrance Hall"
       inventory = []
       show_instructions() 

    # TODO: Create the player's inventory.

    # TODO: Call the instruction function at the appropriate time.

       While True: 
           show_status(current_room, inventory, rooms)
           command = input("Enter your move: ").strip()
           if command.lower() == "exit":
               print("Thanks for playing!")
               break
           elif command.lower().startswith("go "):
               direction = command[3:].capitalize()
               if direction in rooms[current_room]:
                   current_room = rooms[current_room][direction]
               else:
                   print("You cannot go that way!")
           elif command.lower().startswith("get "):
               item = command[4:]
               if rooms[current_room].get("item", "").lower() == item.lower()
                   inventory.append(rooms[current_room]["item"]
                   print("You collected", rooms[current_room]["item"]
                   del rooms[current_room]["item"]
               else:
                   print("That item is not in this room.")
            else:
                print("Invalid command")
            if current_room == "Throne Room":
                if len(inventory) == 6:
                    print("Congratulations! You defeated the Ghost King!")
                else:
                    print("The Ghost King defeated you! Game Over!")
                break
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.



if __name__ == "__main__":
    main()
