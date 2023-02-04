import pygame, random
from grid import gridrows, gridcols

def randomTilePos(tilesize):
    # First it makes a random number of for x and y with a range of 0 to tilesize.
    randomX = random.randint(0, gridcols - 1)
    randomY = random.randint(0, gridrows - 1)
    # Then it multiplys the new random values by tilesize.
    tileX = randomX * tilesize
    tileY = randomY * tilesize
    # And finally, it returns the tile values to the original statement that called it.
    return tileX, tileY
    
class Apple:
    def __init__(self, tilesize, prevtime, eatDelay):
        self.rect = pygame.Rect(0, 0, tilesize, tilesize)
        # This generates a random tile position.
        self.rect.topleft = randomTilePos(tilesize)
        
        print(f"Apple starting position: {self.rect.topleft}")
        
        # Sets up how much time must pass before the apple can be eaten again.
        self.prevtime = prevtime
        self.eatDelay = eatDelay
    
    # Draws the apple
    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self)
    
    # This function is for checking if the head of the snake has eaten the apple and moving the apple to a random tile.
    # There are some extra code for preventing the apple's new position from being inside of the head or body of the snake.
    def eatDetection(self, snakeHead, snakeBody, tilesize, now):
        # Checks if apple has collided with the head of the snake.
        if self.rect.colliderect(snakeHead):
            # If true then it checks if eat delay is over. Increases the snake's length if true
            if now - self.prevtime >= self.eatDelay:
                snakeHead.length += 2
                
                # Debug Text
                print(f"Apple pos: {self.rect.topleft} | Snake Length: {snakeHead.length} | Total Body Instances: {len(snakeBody)}")
            
            # If the conditions are not met then it simply resets the timer and move to another random tile.    
            self.prevtime = now
            self.rect.topleft = randomTilePos(tilesize)
            
        # If not, then it executes this code.
        else:
            for obj in snakeBody: # This checks if any of the body instances has collided with the apple
                if self.rect.colliderect(obj):
                    # If true then reset the timer and move to another random tile
                    self.prevtime = now
                    self.rect.topleft = randomTilePos(tilesize)
                    
                    # Debug Text
                    print(f"Apple pos: {self.rect.topleft}")