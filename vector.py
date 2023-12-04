import math

# stores and manipulates (x, y, z) coordinates
class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    # add another vector to this vector
    def add(self, obj):
        self.x += obj.x
        self.y += obj.y
        self.z += obj.z

    # subtract another vector from this vector
    def subtract(self, obj):
        self.x -= obj.x
        self.y -= obj.y
        self.z -= obj.z

    # return the vector addition with another vector
    def getAdded(self, obj):
        return Vector(self.x + obj.x, self.y + obj.y, self.z + obj.z)

    # return the vector subtraction of another vector
    def getSubtracted(self, obj):
        return Vector(self.x - obj.x, self.y - obj.y, self.z - obj.z)

    # scale by a constant
    def scale(self, k):
        self.x *= k
        self.y *= k
        self.z *= k

    # return this vector scaled by a constant
    def getScaled(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)

    # return x^2 + y^2 + z^2
    def getRSquared(self):
        return pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)
    
    # rotate this vector clockwise by the given angle
    def rotateZCW(self, angle):
        newx = self.x * math.cos(angle) + self.y * math.sin(angle)
        newy = self.y * math.cos(angle) - self.x * math.sin(angle)
        self.x = newx
        self.y = newy
    
    def rotateX(self, angle):
        newy = self.y * math.cos(angle) + self.z * math.sin(angle)
        newz = self.z * math.cos(angle) - self.y * math.sin(angle)
        self.y = newy
        self.z = newz

    # reset to x=0, y=0, z=0
    def reset(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"