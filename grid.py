import pygame
# Holds a list of all created tile instances.
tileObjs = []

# By how many rows of tiles will the game display
gridrows = 20
gridcols = 20

class Tile:
    def __init__(self, x, y, tilesize):
        self.rect = pygame.Rect(x, y, tilesize - 1, tilesize - 1)
    
    # Draws the instance    
    def draw(self, surface, color):
        
        pygame.draw.rect(surface, color, self)
       
def createGrid(tilesize):
    tileObjs.clear()
    
    # Creates all the grid tile at the right positions
    for row_index in range(gridcols):
        for col_index in range(gridrows):
            x = col_index * tilesize
            y = row_index * tilesize
            
            tileObjs.append(Tile(x, y, tilesize))