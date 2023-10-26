# stores and manipulates (x, y, z) coordinates
class Vector:
    def __init__(self, coordinates = [0.0, 0.0, 0.0]):
        self.coordinates = coordinates

    # add another vector to this vector
    def add(self, other):
        for i in range(len(self.coordinates)):
            self.coordinates[i] += other.coordinates[i]

    # subtract another vector from this vector
    def subtract(self, other):
       for i in range(len(self.coordinates)):
            self.coordinates[i] -= other.coordinates[i]

    # return the vector addition with another vector
    def getAdded(self, other):
        return Vector([i + j for i, j in zip(self.coordinates, other.coordinates)])

    # return the vector subtraction of another vector
    def getSubtracted(self, other):
        return Vector([i - j for i, j in zip(self.coordinates, other.coordinates)])

    # scale by a constant
    def scale(self, k):
        for i in range(len(self.coordinates)):
            self.coordinates[i] *= k

    # return this vector scaled by a constant
    def getScaled(self, k):
        return Vector([i * k for i in self.coordinates])

    # return x^2 + y^2 + z^2
    def getRSquared(self):
        result = 0.0
        for i in self.coordinates:
            result += pow(i, 2.0)
        return result

    # reset to x=0, y=0, z=0
    def reset(self):
        for i in self.coordinates:
            i = 0.0
            
    def getX(self):
        return self.coordinates[0]
            
    def getY(self):
        return self.coordinates[1]

    def __str__(self):
        return str(self.coordinates)