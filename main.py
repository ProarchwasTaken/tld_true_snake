import pygame, time
from grid import tileObjs, createGrid
from snake import Head, failureDetection
from apple import Apple
#============================================================================
# Proper snake clone made by Tyler "Proarch" @2023
# Thank you for using this script!
#============================================================================

# Sets up the window
pygame.init()
screenWidth, screenHeight = 500, 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake but it actually works properly")

# Sets up the clock and FPS
clock = pygame.time.Clock()
prev_time = time.time()
fps = 60
targetFPS = 60

# Colors
darkGray = 64, 64, 64
black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0

# The size of each tile in the background.
tilesize = 25

# Initializes the grid
createGrid(tilesize)

# Declares player instance
snake = Head(tilesize, prev_time, 0.15)
# Declares apple instance
apple = Apple(tilesize, prev_time, 0.1)

# Main Game Loop
running = True
while running:
    # The game's max framerate
    clock.tick(fps)
    # Handles Delta Time - This is my first time doing suff like this
    # Unfortunatly I can really find a way to use deltatime in this project.
    now = time.time()
    deltatime = now - prev_time
    prev_time = now
    
    # Displays fps count in window caption.
    pygame.display.set_caption(f"Snake but it actually works properly | FPS: {int(clock.get_fps())}")
    
    # Handles events like quiting the game or pressing a key.
    for event in pygame.event.get():
        # Closes the game if the player quits
        if event.type == pygame.QUIT:
            running = False
        # Checks for key inputs, changes snake direction as long as it's not backwards.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not snake.direction == "right":
                snake.direction = "left"
            if event.key == pygame.K_RIGHT and not snake.direction == "left":
                snake.direction = "right"
            if event.key == pygame.K_UP and not snake.direction == "down":
                snake.direction = "up"
            if event.key == pygame.K_DOWN and not snake.direction == "up":
                snake.direction = "down"
    
    # Refreshes the Screen
    screen.fill(darkGray)
    
    # Calls the draw method for every Tile instance.
    for tile in tileObjs:
        tile.draw(screen, black)
    
    # Updates and draws class instances
    apple.draw(screen, red)
    snake.update(screen, green, now, apple)
    
    # Updates the screen
    pygame.display.flip()
    
    # Checks if the player has lost the game, ends the game if true
    if failureDetection(snake, screenWidth, screenHeight):
        running = False
        

# This code is ran when the player ends the game.
print(f"============\nGAMEOVER\n============\nScore: {snake.length} | Thanks for playing!")
time.sleep(3)