import os, keyboard, time



# starting variables used for the game
block_part = '#'

# x and y positions of the said block
x = 0     
y = 0

# entire map of the game
map =[[],[],[],[],[],[],[],[],[],[], [], [],[], [],[],[],[], [],[],[]]
score = 0


# generates the map by adding dashed lines to show a visible grid on the screen
def map_generate():
    global map
    for row in map:
        for _ in range(15):
            row.append('-')





# renders the map, as in shows the map on the screen with updates to any of the grid positions
def map_render():
    for row in map:
        print(8 * " ", end="")
        for i in range(15):
            print(row[i], end="  ")
        print("")
    time.sleep(0.5)
    os.system('cls')




# controls of the game (a and d keys) along with cool-down timer for controls
def controls(start, current):
    global x,y
    if keyboard.is_pressed('a') and current - start >= 0.2:
        if x > 0:
            x -= 1
            map[y-1][x+1] = '-'
            map[y][x+1] = '-'
        start = time.time()
    if keyboard.is_pressed('d') and current - start >= 0.2:
        if x < 14:
            x += 1
            map[y-1][x-1] = '-'
            map[y][x-1] = '-'
        start = time.time()


# function here runs the entire game
def game():
    current_time = time.time()
    global x, y, isNotGrounded, start

    # controls are off when the said part is on the ground
    if isNotGrounded:
        controls(start, current_time)
    # sets the part to it's current position
    map[y][x] = block_part
    
    # as long as the part is not on the ground, it will keep descending
    if y < 19 and current_time - start >= 2:
        y += 1
        start = time.time()

    # checks boolean to determine whether on the ground or not (the last row of the grid)    
    if y == 19:
        isNotGrounded = False
    
    # map is rendered
    map_render()

    # previous positions of the part are cleared
    map[y-1][x] = '-'




# map is generated before the start of the game
map_generate()

# marks the time stamp for when the game first begins.
start = time.time()
# checks if the said part is on the ground or not
isNotGrounded = True

#game constantly being updated via the while loop
while True:
    print('''



 _________  _______  _________  ________  ___  ________      
|\___   ___\\  ___ \|\___   ___\\   __  \|\  \|\   ____\     
\|___ \  \_\ \   __/\|___ \  \_\ \  \|\  \ \  \ \  \___|_    
     \ \  \ \ \  \_|/__  \ \  \ \ \   _  _\ \  \ \_____  \   
      \ \  \ \ \  \_|\ \  \ \  \ \ \  \\  \\ \  \|____|\  \  
       \ \__\ \ \_______\  \ \__\ \ \__\\ _\\ \__\____\_\  \ 
        \|__|  \|_______|   \|__|  \|__|\|__|\|__|\_________\ 
                                                 \|_________|
                                                                                                                
          ''')
    game()

   

    
    