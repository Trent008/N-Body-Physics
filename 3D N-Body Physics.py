from planet import Planet
from vector import Vector
import pygame
import sys
import keyboard

pygame.init()

# Set up the window
screenSize = Vector([1800, 1200])
screen = pygame.display.set_mode(screenSize.v)
pygame.display.set_caption("Planets Simulation") # 
white = (255, 255, 255)  # White color
yellow = (255, 255, 0)  # yellow color
font = pygame.font.Font('freesansbold.ttf', 14) # font object

azimuth = 1
heading = 0
displayPosition = Vector()

dt = 0.000001 # physics delta time
timewarp = 1
scale = 1 # display scale factor for zoom

planets = [] # list of planet objects
planets.append(Planet(Vector([0.0, 0.0, 0.0]), Vector([0.0, -0.3, 0.0]), 40.0))
planets.append(Planet(Vector([1.0, 0.0, 0.0]), Vector([0.0, 6, 0.0]), 1.0))
planets.append(Planet(Vector([2.5, 0.0, 0.0]), Vector([0.0, 4, 0.0]), 2.0))


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # todo: prevent multiple press detection
        keys = pygame.key.get_pressed()
        # timewarp faster or slower
        if keys[pygame.K_PERIOD] and timewarp < 8000:
            timewarp *= 2.5
        if keys[pygame.K_COMMA] and timewarp > 2:
            timewarp /= 2.5

        # zoom in or out
        if keys[pygame.K_EQUALS]:
            scale *= 1.02
        if keys[pygame.K_MINUS]:
            scale /= 1.02

        # change viewing angle
        if keys[pygame.K_RIGHT]:
            heading += 0.05;
        if keys[pygame.K_LEFT]:
            heading -= 0.05;
        if keys[pygame.K_UP]:
            azimuth += 0.05;
        if keys[pygame.K_DOWN]:
            azimuth -= 0.05;


    # Clear the screen
    screen.fill((0, 0, 0))
    text = font.render(f'TimeWarp = {timewarp}X', True, yellow)
    # create a rectangular object for the text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (150, 20)
    screen.blit(text, textRect)

    # loop through the planets
    for i in planets:
        # run update function
        i.update(dt * timewarp, planets)
        # update the screen display
        i.displayPosition.rotateZCW(heading)
        i.displayPosition.rotateX(azimuth)
        i.displayPosition.v.pop()
        i.displayPosition.v[1] *= -1
        i.displayPosition *= scale * 150
        i.displayPosition += screenSize * (1 / 2)
        i.displayDiameter = scale*2*pow(i.mass, 1/3)
        pygame.draw.circle(screen, white, i.displayPosition.v, i.displayDiameter)
    # display updated graphics
    pygame.display.flip()
