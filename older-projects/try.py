import os

# Set the grid size
GRID_SIZE = 10
player_x, player_y = GRID_SIZE // 2, GRID_SIZE // 2

# Main game loop
while True:
    # Clear the terminal screen
    os.system("clear" if os.name == "posix" else "cls")

    # Create the grid and place the player
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if x == player_x and y == player_y:
                print("P", end=" ")
            else:
                print(".", end=" ")
        print()

    # Get user input
    move = input("Move (W/A/S/D, Q to quit): ").upper()

    # Update player position 
    if move == "W" and player_y > 0:
        player_y -= 1
    elif move == "A" and player_x > 0:
        player_x -= 1
    elif move == "S" and player_y < GRID_SIZE - 1:
        player_y += 1
    elif move == "D" and player_x < GRID_SIZE - 1:
        player_x += 1
    elif move == "Q":
        break
