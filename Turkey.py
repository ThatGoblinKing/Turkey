import pygame
pygame.init()
pygame.display.set_caption("toiky")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
PINK = (245, 154, 219)
BLUE = (140, 214, 237)
WHITE = (252, 239, 237)
BRIGHT_WHITE = (255,255,255)
BLACK = (0,0,0)
OFFWHITE = (255, 231, 227)
TAIL_SIZE = 50

class Turkey:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        
    def changeSize(self, sizeChange):
        if (self.size + sizeChange) > 0:
            self.size += sizeChange
    def move(self, xChange, yChange):
        self.x += xChange
        self.y += yChange
            
    def getSize(self):
        return self.size * 100
    
    def draw(self):
        #TAIL----------
        pygame.draw.circle(screen, PINK, (self.x, self.y - 140 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, PINK, (self.x - 110 * self.size, self.y + 20 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, PINK, (self.x + 80 * self.size, self.y - 100 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, PINK, (self.x - 80 * self.size, self.y - 100 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, PINK, (self.x + 120 * self.size, self.y - 20 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, PINK, (self.x - 120 * self.size, self.y - 20 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, PINK, (self.x + 110 * self.size, self.y + 20 * self.size), TAIL_SIZE * self.size)

        pygame.draw.circle(screen, BLUE, (self.x + 45 * self.size, self.y - 120 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, BLUE, (self.x - 45 * self.size, self.y - 120 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, BLUE, (self.x + 100 * self.size, self.y - 45 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, BLUE, (self.x - 100 * self.size, self.y - 45 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, BLUE, (self.x - 90 * self.size, self.y + 30 * self.size), TAIL_SIZE * self.size)
        pygame.draw.circle(screen, BLUE, (self.x + 90 * self.size, self.y + 30 * self.size), TAIL_SIZE * self.size)
        
        #Legs-------------------
        pygame.draw.rect(screen, PINK, ((self.x - 60 * self.size, self.y + 65 * self.size), (20 * self.size, 100 * self.size)))
        pygame.draw.rect(screen, PINK, ((self.x + 40 * self.size, self.y + 65 * self.size), (20 * self.size, 100 * self.size)))
        
        # Body
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 120 * self.size)
        
        # Face
        pygame.draw.ellipse(screen, OFFWHITE, (self.x - 55 * self.size, self.y - 180 * self.size, 110 * self.size, 150 * self.size))
        #Beak
        pygame.draw.polygon(screen, BLUE, ((self.x, self.y - 100 * self.size), (self.x - 25 * self.size, self.y - 140 * self.size), (self.x + 25 * self.size, self.y - 140 * self.size)))
        
        #Eyes
        pygame.draw.circle(screen, BRIGHT_WHITE, (self.x - 40 * self.size, self.y - 140 * self.size), 20 * self.size)
        pygame.draw.circle(screen, BRIGHT_WHITE, (self.x + 40 * self.size, self.y - 140 * self.size), 20 * self.size)
        pygame.draw.circle(screen, BLACK, (self.x + 37 * self.size, self.y - 140 * self.size), 10 * self.size)
        pygame.draw.circle(screen, BLACK, (self.x - 37 * self.size, self.y - 140 * self.size), 10 * self.size)
#turkey = Turkey(1, 400, 400)
tinyTurk = Turkey(1, 400, 400)
gameOver = False
while not gameOver:
    gameEvents = pygame.event.get()
    # Input Section------------------------------------------------------------
    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                tinyTurk.changeSize(-0.05)
            elif event.key == pygame.K_UP:
                tinyTurk.changeSize(0.05)
            if event.key == pygame.K_w:
                tinyTurk.move(0, -20)
            elif event.key == pygame.K_s:
                tinyTurk.move(0, 20)
            elif event.key == pygame.K_a:
                tinyTurk.move(-20, 0)
            elif event.key == pygame.K_d:
                tinyTurk.move(20, 0)

    screen.fill(BLACK)
    
    tinyTurk.draw()
    font = pygame.font.SysFont(None, 64)
    img = font.render(f"Size: {tinyTurk.getSize():0.0f}%", True, (255, 255, 255))
    screen.blit(img, (0, 0))
    
    pygame.display.flip()
    