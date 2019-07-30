# compass_v3.py
# 31/07

import time

def compass():

    news = ['N', 'W', 'E', 'S']
    space = ""

    direction = input("Which way? (n/w/e/s): ")
    num = int(input("Number of nz found: "))
    new = input("If new place press: (1): ")
    food = input("Food is: (n/w/s/e/none) ").lower()

    # Changes the compass brackets and sets the direction
    if direction == 'n':
        direction = 'North'
        news = ['[ N ]', '  W  ', '  E  ', '  S  ']

    elif direction == 'w':
        direction = 'West'
        news = ['  N  ', '[ W ]', '  E  ', '  S  ']
        
    if direction == 'e':
        direction = 'East'
        news = ['  N  ', '  W  ', '[ E ]', '  S  ']
        
    elif direction == 's':
        direction = 'South'
        news = ['  N  ', '  W  ', '  E  ', '[ S ]']
   
    # Changes the desription based on if the player has already been to the position
    # Will be found from the discovered/undiscorvered lists in final program 
    if new == '1':
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
    
        
    print("\nTraveling {}..".format(direction))


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
    """.format(direction, space.ljust(5-len(direction)), news[0], food_avaliable, food_direction, space.ljust(37-(len(food_avaliable)+len(food_direction))), news[1], news[2], description, space.ljust(33-len(description)), num, space.ljust(2-len(str(num))), news[3]))



compass()
