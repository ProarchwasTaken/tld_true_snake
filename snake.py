import pygame, random

snakeBody = []
directions = ["up", "down", "left", "right"]
randomDir = random.choice(directions)

class Head:
    def __init__(self,tilesize, prevtime, delay):
        
        self.rect = pygame.Rect(250, 250, tilesize, tilesize)
        # Randomly sets the starting direction.
        self.direction = str(randomDir)
        print(f"Starting direction: {self.direction}")
        
        # How far the snake moves after each delay depends on the tilesize
        self.distance = tilesize
        # Hands the time between each time the engine activates
        self.engineDelay = delay
        self.prevTime = prevtime
        # The Snake's length
        self.length = 2
        # The size of the snake.
        self.snakeSize = tilesize
        print(f"Starting length: {self.length}")
    
    # This function is called once every cycle
    def update(self, surface, color, now, apple):
        
        # This function has everything that'll make the snake and the other game elements function.
        self.engine(now, apple)
        # Draws the head
        self.draw(surface,color)
        # Draws the body
        for obj in snakeBody:
            obj.draw(surface, color)
    
    def draw(self, surface, color):
        
        pygame.draw.rect(surface, color, self)
    
    def engine(self, now, apple):
        # Most important function, activates after enough time has passed then it resets the timer
        if now - self.prevTime >= self.engineDelay:
            
            # This is to check for apple collision.
            apple.eatDetection(self, snakeBody, self.snakeSize, now)
            
            # Creates a snakeBody instance
            snakeBody.append(Body(self.rect.x, self.rect.y, self.snakeSize, self.length))
            
            # Automatically moves the snake in a certain direction based on self.direction
            self.move()
            
            # Calls the tick function for every single Body Instance   
            for obj in snakeBody:
                obj.tick()
            
            # Resets the timer
            self.prevTime = now
    
    def move(self):
        if self.direction == "left":
            self.rect.x -= self.distance
                
        elif self.direction == "right":
            self.rect.x += self.distance
                
        elif self.direction == "up":
            self.rect.y -= self.distance
                
        elif self.direction == "down":
            self.rect.y += self.distance

class Body():
    def __init__ (self, x, y, tilesize, length):
        self.rect = pygame.Rect(x, y, tilesize, tilesize)
        # How long the instance will be present be disappearing
        self.timer = length
        # Adds instance to snakeBody instance for later use.
        snakeBody.append(self)
    
    # Draws the snake body
    def draw(self, surface, color):
        
        pygame.draw.rect(surface, color, self)
    
    # At the end of each movement cycle, self.time ticks down by 1.
    def tick(self):
        self.timer -= 1
        
        # If self.time hits 0, the instance is removed from the game.
        if self.timer <= 0:
            snakeBody.remove(self)
    
    # Checks if the body instances has collided with the snake head when called.        
    def collideCheck(self, head):
        if self.rect.colliderect(head):
            return True

# This function checks for any lose conditions when called.            
def failureDetection(snake, screenWidth, screenHeight):
    # Checks if snake head is outside the screen. Return True if it is.
    if snake.rect.left < 0 or snake.rect.right > screenWidth or snake.rect.top < 0 or snake.rect.bottom > screenHeight:
        return True
    # Checks if the snake head has collided with it's tail. Returns True if it is.
    for obj in snakeBody:
        if obj.collideCheck(snake):
            return True