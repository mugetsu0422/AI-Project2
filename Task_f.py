import pygame
from pygame.locals import *
import sys
from Task_e import A_star

pygame.init()
SIZE = 8
WIDTH = HEIGHT = 720
WINDOW = pygame.display.set_mode((1000, HEIGHT))

# set caption
pygame.display.set_caption('8-queens')

# load queen images
BLACK_QUEEN = pygame.image.load('blackQ.png').convert_alpha()
WHITE_QUEEN = pygame.image.load('whiteQ.png').convert_alpha()
FILE_INPUT = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (153, 255, 153)

# Create the right side of the chess board, which contains a text box for inputting file name
#           and a "SEARCH" button for running A* algorithm 
def createRightSide(width, height, surface):
    rects = pygame.Rect(WIDTH, 0, 1000 - WIDTH, HEIGHT)
    pygame.draw.rect(surface, GREEN, rects)

    # Search button
    rects = pygame.Rect(770, 300, 200, 100)
    pygame.draw.rect(surface, WHITE, rects)
    pygame.draw.rect(surface, BLACK, rects, 5)

    # Text box
    smallfont = pygame.font.SysFont('Corbel', 50)
    text = smallfont.render('SEARCH' , True , BLACK)
    surface.blit(text , (782 , 330))

# Draw surface of BLACK and WHITE chessboard
def createChessBoard(width, height, surface):
    rect_width = width / 8
    rect_height = height / 8

    for i in range(SIZE):
        for j in range(SIZE):
            if i % 2 == 0:
                if j % 2 == 0:
                    rects = pygame.Rect(j * rect_width, i * rect_height, rect_width, rect_height)
                    pygame.draw.rect(surface, WHITE, rects)
                
                else:
                    rects = pygame.Rect(j * rect_width, i * rect_height, rect_width, rect_height)
                    pygame.draw.rect(surface, BLACK, rects)
            
            else:
                if j % 2 == 1:
                    rects = pygame.Rect(j * rect_width, i * rect_height, rect_width, rect_height)
                    pygame.draw.rect(surface, WHITE, rects)
                
                else:
                    rects = pygame.Rect(j * rect_width, i * rect_height, rect_width, rect_height)
                    pygame.draw.rect(surface, BLACK, rects)

    rects = pygame.Rect(WIDTH, 0, 1000 - WIDTH, HEIGHT)
    pygame.draw.rect(surface, GREEN, rects)

# Place queens on chess board with x, y coordinate
def drawQueen(x, y, surface):
    if x % 2 == 0:
        if y % 2 == 0:
            WINDOW.blit(BLACK_QUEEN, (x * (WIDTH /SIZE), y * (HEIGHT / SIZE)))
        else:
            WINDOW.blit(WHITE_QUEEN, (x * (WIDTH /SIZE), y * (HEIGHT / SIZE)))
    else:
        if y % 2 == 0:
            WINDOW.blit(WHITE_QUEEN, (x * (WIDTH /SIZE), y * (HEIGHT / SIZE)))
        else:
            WINDOW.blit(BLACK_QUEEN, (x * (WIDTH /SIZE), y * (HEIGHT / SIZE)))

FONT = pygame.font.Font(None, 32)

# Implement class for the inputting text box
class InputBox:

    def __init__(self, x, y, w, h, text = ''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLACK
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    # Catch event of user
    def handle_event(self, event):
        #If the user click on the input_box rect
        if event.type == pygame.MOUSEBUTTONDOWN:    
            
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            
            else:
                self.active = False
            
            #Set the color of the input box
            self.color = BLACK 

        #If the user type text in the box
        if event.type == pygame.KEYDOWN:     
            if self.active:
                #If the user ENTER, read file from input
                if event.key == pygame.K_RETURN:    
                    self.readFile()

                #If the user BACKSPACE
                elif event.key == pygame.K_BACKSPACE:   
                    self.text = self.text[:-1]

                else:
                    self.text += event.unicode

                #Re-render the text    
                self.txt_surface = FONT.render(self.text, True, self.color) 

    # Update the size of the box if the text is too long
    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    # Draw text box
    def draw(self):
        WINDOW.blit(self.txt_surface, ((self.rect.x+5, self.rect.y+5)))
        pygame.draw.rect(WINDOW, self.color, self.rect, 2)
        pygame.display.update()
    
    # Read coordinates from input file
    def readFile(self):
        result = []
        filename = self.text
        f = open(filename, 'r')
        n = int(f.readline())
        line = f.readline()
        tempQ = []
        
        for item1 in line.split(')'):
            for item2 in item1.split(','):
                tempQ.append(item2.strip('() '))

        for i in range(n):
            x = int(tempQ.pop(0))
            y = int(tempQ.pop(0))
            result.append([x, y])

        f.close()

        for item in result:
            FILE_INPUT.append(item)
            # Place N first queens from file's coordinate on the chessboard
            drawQueen(item[1], item[0], WINDOW)
        
        pygame.display.update()


def mainloop():
    input_box = InputBox(770, 200, 200, 32)
    done = False
    init = False

    while not done:
        # Catch event of mouse click
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            #If the user click on [x] button -> quit
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
            
            input_box.handle_event(event)

            # Check if the cursor in range of the SEARCH button
            if mouse[0] >= 770 and mouse[0] <= 1070 and mouse[1] >= 300 and mouse[1] <= 400:
                if click[0] == True:

                    # Start placing the rest of the queens on chessboard
                    board = [[ False for i in range(SIZE) ] for j in range(SIZE)]
                    queens = FILE_INPUT
                    queens = A_star(board, queens)

                    for item in queens:
                        old = False

                        for i in FILE_INPUT:
                            if item == i:
                                old = True
                                break

                        if old == False:
                            drawQueen(item[1], item[0], WINDOW)
                            pygame.time.delay(500)
                            pygame.display.update()
         
        if init == False:
            createChessBoard(WIDTH, HEIGHT, WINDOW)
            pygame.display.update()
            init = True
        
        createRightSide(WIDTH, HEIGHT, WINDOW)
        input_box.draw()


def main():
    mainloop()

if __name__ == "__main__":
    main()
    pygame.quit()