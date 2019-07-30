# maui.py
# Aaron Radka
# Created 23/7

# v1.0 - 23/07
# v1.1 - 23/07
# v1.2 - 24/07
# v1.3 - 24/07
# v1.4 - 30/07
# 
# v2.0 - 31/07
# 
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
    
    undiscovered_pos.pop(start_pos)
    discovered_pos.append(start_pos)    
    
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
        move = False
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
                move = True
                
        elif direction == 'a':
            # Will stop if player is on left side of the board
            if player_pos // 6 == 0:
                print("You cannot go further..\n")
            else:
                player_pos -= 6
                move = True

        elif direction == 's':
            # Will stop if player is on the bottom of board
            if player_pos % 6 == 5:
                print("You cannot go further..\n")
            else:
                player_pos += 1
                move = True

        elif direction == 'd':
            # Will stop if player is on the right side of the board
            if player_pos // 6 == 5:
                print("You cannot go further..\n")
            else:
                player_pos += 6
                move = True

        # Spacebar
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
            # new used in compass function
            new = True
        else:
            new = False

        if move == True:
            compass(direction, new, discovered_pos)
        else:
            print()




def compass(direction, new, discovered_pos):

    news = ['N', 'W', 'E', 'S']
    space = ""

    # Bring through: direction, new

    discovered_num = len(discovered_pos)
    food = input("Food is: (n/w/s/e/none) ").lower()


    # Changes the compass brackets and sets the direction
    if direction == 'w':
        direction_moved = 'North'
        news = ['[ N ]', '  W  ', '  E  ', '  S  ']

    elif direction == 'a':
        direction_moved = 'West'
        news = ['  N  ', '[ W ]', '  E  ', '  S  ']
        
    if direction == 'd':
        direction_moved = 'East'
        news = ['  N  ', '  W  ', '[ E ]', '  S  ']
        
    elif direction == 's':
        direction_moved = 'South'
        news = ['  N  ', '  W  ', '  E  ', '[ S ]']
   
    # Changes the desription based on if the player has already been to the position
    # Will be found from the discovered/undiscorvered lists in final program 
    if new == True:
        description = "You don't recognise this place..."
    else:
        description = "This place looks familiar..."
        
    # Description if food is nearby wih direction
    # Will be found off position list in final program
    food_avaliable = "Something catches your eye..."
    if food == 'n':
        food_direction = "North"
    elif food == 'w':
        food_direction = "West"
    elif food == 's':
        food_direction = "South"
    elif food == 'e':
        food_direction = "East"
    elif food == 'none':
        food_direction = ""
        food_avaliable = ""
    else:
        print("Inputs were incorrect")
    
        
    print("\nTraveling {}..".format(direction_moved))


    # Prints compass
    print("""
                                                       .  
                                                     .` `.               
                                                   .`     `.             
    You travel {}...{}                          .`         `.      
                                               .`    {}    `.          
    {} {}{}   .`        |        `.  
                                           .`         )|(         `.      
                                         .`         )  |  (         `.     
                                       .`         )    |    (         `.  
                                     .`         )      |      (         `.
                                   .`  {}--)--------O--------(--{}  `.
                                    `.          )      |      (          .`    
                                      `.          )    |    (          .` 
    {}{}   `.          )  |  (          .` 
                                          `.          )|(          .`     
    New Zealand Discovered: ({}/36){}         `.         |         .`     
                                              `.     {}     .`         
                                                `.           .`     
                                                  `.       .`            
                                                    `.   .`             
                                                      `.`                                                    
    """.format(direction_moved, space.ljust(5-len(direction_moved)), news[0], food_avaliable, food_direction, space.ljust(37-(len(food_avaliable)+len(food_direction))), news[1], news[2], description, space.ljust(33-len(description)), discovered_num, space.ljust(2-len(str(discovered_num))), news[3]))






start()
