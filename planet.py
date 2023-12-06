from vector import Vector
import math

class Planet:
    def __init__(self, startPosition, startVelocity, mass):
        self.position = startPosition  # starting position
        self.velocity = startVelocity  # starting velocity
        self.mass = float(mass)  # mass of planet
        self.acceleration = Vector()  # current acceleration
        self.displayPosition = Vector()  # position to display the planet on screen
        self.displayDiameter = 0  # diameter to display the planet

    # return this planet's acceleration toward another planet
    def getRelativeAcceleration(self, obj):
        difference = obj.position - self.position # find the distance vector to the other planet
        rSquared = difference * difference # the distance between the planets squared
        # return the acceleration vector pulling this planet toward the other planet
        return difference * (obj.mass / math.pow(rSquared, 1.5))

    # update position and velocity
    def update(self, dt, planets):
        for i in planets:
            # find the accel of planet i toward every planet except itself
            if i != self:
                # add the acceleration toward planet j to planet i's current acceleration
                self.acceleration += self.getRelativeAcceleration(i)
        self.position += self.velocity * dt
        self.velocity += self.acceleration * dt
        self.acceleration.reset()
        self.displayPosition = Vector(self.position.v)
