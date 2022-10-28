##
# Pygame base template for opening a window
# MVC version
#
# @ Alisha M.
# @date 2022/05/19 Last modified


## Pygame setup
import pygame
import random
import math
pygame.init()
size = (620, 320)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("night sky")
fontObj = pygame.font.Font('freesansbold.ttf', 16)

## MODEL - Data use in system
# Define some colors
# rgb method
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (248, 217, 97.25)
BROWN = (119, 90, 46.67)
PURPLE = (70, 5, 101)
LIGHT_YELLOW = (237, 229, 92.94)
GRAY = (190, 180, 240)
FOREST_GREEN = (11, 58, 23)
triColour = [70, 5, 101]
FADED_WHITE = (203,220,203)
FLICKERING_LIGHTS = [237, 229, 92.94]
pi = 3.141592653

steps = 0
angleRotation = 0.5
lineLen = 20
clockx = 482
clocky = 100

moonX = 100
ufoX = 100
elevatorX = 165
starX = 20
clockTick = 100
snowList = []
font = pygame.font.SysFont('Calibri', 12, True, False)

# Loop until the user clicks the close button.
done = False

# Make it snow 
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snowList.append([x, y])

     
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

## Main Program Loop

while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True

    if (moonX < 640):
        moonX = moonX + 1
    elif (moonX >= 600):
        moonX = -100

    if (elevatorX < 260):
      elevatorX = elevatorX + 0.4
    elif (elevatorX >= 255):
      elevatorX = 120

    if (ufoX < 500):
      ufoX = ufoX + 1
    elif (ufoX >= 500):
      ufoX = ufoX * - 1

    triColour[1] = triColour[1] - 1
    if triColour[1] < 0:
        triColour[1] = 255

    FLICKERING_LIGHTS[1] = FLICKERING_LIGHTS[1] - 2
    if FLICKERING_LIGHTS[1] < 0:
        FLICKERING_LIGHTS[1] = 255

    # Game logic

    ## VIEW
    # Clear screen
    screen.fill(PURPLE)
  
    for i in range(len(snowList)):

        # Draw the snow flake
        pygame.draw.circle(screen, FADED_WHITE, snowList[i], 1)

        # Move the snow flake down one pixel
        snowList[i][1] += 1

      # If the snow flake has moved off the bottom of the screen
        if snowList[i][1] > 600:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snowList[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 600)
            snowList[i][0] = x
    # Draw

  # UFO
    pygame.draw.ellipse(screen, GREEN, [110,30,60,16])
    pygame.draw.ellipse(screen, WHITE, [120,23,40,16])
    pygame.draw.line(screen, BLACK, [140,23], [140,10],1)
    pygame.draw.circle(screen, WHITE, [141,12], 5, 1)
  
  # SHOOTING STAR  
    pygame.draw.line(screen, triColour, [300,40],[270, 20],1)
  
  # MOON
    pygame.draw.circle(screen, WHITE, [moonX, 50], 37, 0)

  # CLOUDS

    pygame.draw.ellipse(screen, GRAY, [490, 80, 30, 10])
    pygame.draw.ellipse(screen, GRAY, [507, 80, 30, 10])

    pygame.draw.ellipse(screen, GRAY, [310, 28, 30, 13])
    pygame.draw.ellipse(screen, GRAY, [330, 30, 20, 10])    

  # BUILDING ONE
    pygame.draw.rect(screen, BLACK, [0, 130, 80, 360])
  
  # BUILDING TWO
    pygame.draw.rect(screen, BLACK, [81, 110, 85, 450])
  
  # HILL
    pygame.draw.ellipse(screen, GREEN, [170, 200, 92, 200])
  
  # TWIN PINES (back to the future!)
    for offsetx in range(180, 260, 70):
        pygame.draw.line(screen, BROWN, [0+offsetx, 270], [0+offsetx, 320], 8)
    pygame.draw.ellipse(screen, FOREST_GREEN, [160, 260, 40, 20])
    pygame.draw.ellipse(screen, FOREST_GREEN, [230, 260, 40, 20])

  # GAZEBO ON HILLTOP
  
    # pillars 
    for offsetx in range(197, 250, 35):
        pygame.draw.line(screen, BROWN, [0+offsetx, 180], [0+offsetx, 210], 4)  
# game
    # rooftop
    pygame.draw.polygon(screen, BROWN, 
            [[195, 182], [236,182], [214, 160]], 0)
  
 # BRIDGE BETWEEN BUILDING THREE AND FOUR
    pygame.draw.arc(screen, BLUE, [310, 200, 100, 70],0, pi/2, 9)
    pygame.draw.arc(screen, RED, [310, 200, 100, 70], pi/2,     pi, 9)
 
  # BUILDING THREE
    pygame.draw.rect(screen, BLACK, [265, 140, 68, 360])
  
  # BULDING FOUR
    pygame.draw.rect(screen, BLACK, [390, 140,68, 360])

  # BUILDING FIVE
    pygame.draw.rect(screen, BLACK, [460, 70, 42, 400])

  # CLOCK ON BUILDING FIVE
    pygame.draw.circle(screen, WHITE, [481, 100], 18)
  
  # HAND ON CLOCK ON BUILDING (the clock moves weirdly because the ufo is messing with it 😅)
    angle = steps * angleRotation
    M = lineLen / 2 * math.sin(angle)
    Z = lineLen / 2 * math.cos(angle)
    pygame.draw.line(screen, BLACK, [480, 100], [489, 109], 2)
    
    pygame.draw.line(screen, RED, (((clockx), (clocky + Z))), ((clockx - M),(clocky - Z)), 1)

    pygame.draw.line(screen, BLACK, [480, 100], [485, 90], 1)

  #ROOF OF BUILDING six
    pygame.draw.polygon(screen, BLACK, 
            [[504, 100], [559,57], [604, 100]], 0)
  
  # BUILDING six
    pygame.draw.rect(screen, BLACK, [504, 100, 100, 350])

  # ELEVATOR  #263
    pygame.draw.rect(screen, GRAY, [537, elevatorX, 30, 40])

  # random WINDOWS
    pygame.draw.rect(screen, FLICKERING_LIGHTS, [400, 150, 15, 15])
    pygame.draw.rect(screen, FLICKERING_LIGHTS, [430, 170, 15, 15])

  
  # FLOATING STARS
    pygame.draw.line(screen, WHITE, [300, 80], [298, 79.02],2)
    pygame.draw.line(screen, WHITE, [220, 50], [218, 49.02],2)
    pygame.draw.line(screen, WHITE, [420, 20], [418, 19.02],2)
    pygame.draw.line(screen, WHITE, [500, 40], [498, 39.02],2)
    pygame.draw.line(screen, WHITE, [360, 150], [358, 149.02],2)

    # BUILDING THREE'S ANTENNAS
    for offsetx in range(287, 330, 25):
        pygame.draw.line(screen, RED, [0+offsetx, 110], [0+offsetx, 140], 1) 

    # BUILDING FOUR'S ANTENNAS
    for offsetx in range(410, 453, 25):
        pygame.draw.line(screen, BLUE, [0+offsetx, 110], [0+offsetx, 140], 1) 

  #  WINDOW SET ONE FOR BUILDING TWO
    for offsety in range (115, 340, 40):
      pygame.draw.line(screen, YELLOW, [95, 20 +offsety], [115, 20 +offsety],20)

  # WINDOW SET TWO FOR BUILDING TWO
      for offsety in range (115, 250 , 40):
        pygame.draw.line(screen, YELLOW , [130, 20 + offsety], [150, 20 +offsety], 20)
    
    text = font.render("WELLS FARGO ", True, YELLOW)
    screen.blit(text, [507, 110])
  
    # Update Screen
    pygame.display.flip()
    clock.tick(60)
    steps -= 0.05

# Close the window and quit
pygame.quit()
