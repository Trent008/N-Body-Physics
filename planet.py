from vector import Vector


class Planet:
    def __init__(self, startPosition, startVelocity, mass):
        self.position = startPosition  # starting position
        self.velocity = startVelocity  # starting velocity
        self.mass = mass  # mass of planet
        self.acceleration = Vector()  # current acceleration
        displayPosition = [0, 0]  # position to display the planet on screen
        displayDiameter = 0  # diameter to display the planet

    # return this planet's acceleration toward another planet
    def getRelativeAcceleration(self, obj):
        difference = obj.position.getSubtracted(self.position) # find the distance vector to the other planet
        rSquared = difference.getRSquared() # the distance between the planets squared
        # return the acceleration vector pulling this planet toward the other planet
        return difference.getScaled(obj.mass / pow(rSquared, 1.5))

    # update position and velocity
    def update(self, dt):
        self.position.add(self.velocity.getScaled(dt))
        self.velocity.add(self.acceleration.getScaled(dt))
        self.acceleration.reset()
