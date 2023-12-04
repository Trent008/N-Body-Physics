from planet import Planet
from vector import Vector
import pygame
import sys
import keyboard

pygame.init()

# Set up the window
X = 1800
Y = 1200
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Planets Simulation") # 
white = (255, 255, 255)  # White color
yellow = (255, 255, 0)  # yellow color
font = pygame.font.Font('freesansbold.ttf', 14) # font object

azimuth = 1
heading = 0
displayX = 0
displayY = 0

dt = 0.000001 # physics delta time
timewarpIndex = 0 # timewarp option index
timewarpOptions = [1, 5, 10, 50, 100, 1000, 10000]
scale = 1 # display scale factor for zoom

planets = [] # list of planet objects
planets.append(Planet(Vector(0.0, 0.0, 0.0), Vector(0.0, -0.3, 0.0), 40.0))
planets.append(Planet(Vector(1.0, 0.0, 0.0), Vector(0.0, 6, 0.0), 1.0))
planets.append(Planet(Vector(2.5, 0.0, 0.0), Vector(0.0, 4, 0.0), 2.0))


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # todo: prevent multiple press detection
        keys = pygame.key.get_pressed()
        # timewarp faster or slower
        if keys[pygame.K_PERIOD] and timewarpIndex < 12:
            timewarpIndex += 1
        if keys[pygame.K_COMMA] and timewarpIndex > 0:
            timewarpIndex -= 1

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
        
    print(azimuth)


    # Clear the screen
    screen.fill((0, 0, 0))
    text = font.render(f'TimeWarp = {timewarpOptions[timewarpIndex//2]}X', True, yellow)
    # create a rectangular object for the text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (150, 20)
    screen.blit(text, textRect)

    # loop through the planets
    for i in planets:
        # for each planet loop through the planets
        for j in planets:
            # find the accel of planet i toward every planet except itself
            if j != i:
                # add the acceleration toward planet j to planet i's current acceleration
                i.acceleration.add(i.getRelativeAcceleration(j))
        # update each planet's position and velocity
        i.update(dt * timewarpOptions[timewarpIndex//2])
        # update the screen display
        i.displayPosition.rotateZCW(heading)
        i.displayPosition.rotateX(azimuth)
        displayX = X//2 + scale*150*i.displayPosition.x
        displayY = Y//2 - scale*150*i.displayPosition.y
        i.displayDiameter = scale*2*pow(i.mass, 1/3)
        pygame.draw.circle(screen, white, [displayX, displayY], i.displayDiameter)
    # display updated graphics
    pygame.display.flip()
