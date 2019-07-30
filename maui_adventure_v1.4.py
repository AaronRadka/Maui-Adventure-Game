# maui.py
# Aaron Radka
# Created 23/7

# v1.0 - 23/7
# v1.1 - 23/7
# v1.2 - 24/7
# v1.3 - 24/7
# v1.4 - 30/7
#
#
#
#
#


import random

def start():
    #                |        A        |  |        B         |  |          C           |  |          D           |  |          E           |  |          F           |
    game_board_pos = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35]]

    # Will remove game_board_col for final iteration
    game_board_col = ['A', 'B', 'C', 'D', 'E', 'F']

    discovered_pos = []
    undiscovered_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    
    # Randomly selects the column
    start_list = game_board_pos.index(random.choice(game_board_pos)) + 1


    # Randomly selects the position
    start_pos = random.choice(game_board_pos[start_list - 1])
    player_pos = start_pos
    
    print(discovered_pos)
    undiscovered_pos.pop(start_pos)
    discovered_pos.append(start_pos)
    print(discovered_pos)
    
    
    start_col = game_board_col[(start_pos // 6)]
    start_row = (start_pos % 6) + 1

    # Delete in final program
    print("Starting coordinate: {}{}".format(start_col, start_row))
    print()

    movement(player_pos, game_board_pos, game_board_col, discovered_pos, undiscovered_pos)

    

def movement(player_pos, game_board_pos, game_board_col, discovered_pos, undiscovered_pos):
    move_count = 0
    alive = True
    while alive:
        repeat = True
        while repeat:
            direction = input("Which direction? (WASD): ").lower()
            if direction not in ('w', 'a', 's', 'd', ''):
                print("That input was invalid\n")
            else:
                move_count += 1
                repeat = False

        if direction == 'w':
            # Will stop if player is at the top of the board
            if player_pos % 6 == 0:
                print("You cannot go further..\n")
            else:
                player_pos -= 1
                print("You move North..\n")

                
        elif direction == 'a':
            # Will stop if player is on left side of the board
            if player_pos // 6 == 0:
                print("You cannot go further..\n")
            else:
                player_pos -= 6
                print("You move West..\n")


        elif direction == 's':
            # Will stop if player is on the bottom of board
            if player_pos % 6 == 5:
                print("You cannot go further..\n")
            else:
                player_pos += 1
                print("You move South..\n")


        elif direction == 'd':
            # Will stop if player is on the right side of the board
            if player_pos // 6 == 5:
                print("You cannot go further..\n")
            else:
                player_pos += 6
                print("You move East..\n")


        else:
            alive = False


        ### Delete in final program
        coord_col = game_board_col[(player_pos // 6)]
        coord_row = (player_pos % 6) + 1
        print("Coordinate: {}{}\n".format(coord_col, coord_row))
        ###

        if player_pos not in discovered_pos:
            undiscovered_pos.pop(undiscovered_pos.index(player_pos))
            discovered_pos.append(player_pos)
        else:
            print("This place looks familiar.")

        print("New Zealand Discovered: {}/36\n".format(len(discovered_pos)))


start()
