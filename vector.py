import math

# stores and manipulates (x, y, z) coordinates
class Vector:
    def __init__(self, v = [0, 0, 0]):
        self.v = list(v)

    # return the vector addition
    def __add__(self, other):
        res = []
        for i, j in zip(self.v, other.v):
            res.append(i + j)
        return Vector(res)

    # add a vector to this vector
    def __iadd__(self, other):
        return self + other

    # return the vector subtraction
    def __sub__(self, other):
        res = []
        for i, j in zip(self.v, other.v):
            res.append(i - j)
        return Vector(res)

    # subtract a vector from this vector
    def __isub__(self, other):
        return self - other

    # vector * constant or vector dot product
    def __mul__(self, obj):
        if (isinstance(obj, float) or isinstance(obj, int)):
            res = []
            for i in self.v:
                res.append(i * obj)
            return Vector(res)
        else:
            res = 0
            for i, j in zip(self.v, obj.v):
                res += i * j
            return res

    # scale by a constant
    def __imul__(self, obj):
        return self * obj
    
    # rotate this vector clockwise by the given angle
    def rotateZCW(self, angle):
        newx = self.v[0] * math.cos(angle) + self.v[1] * math.sin(angle)
        newy = self.v[1] * math.cos(angle) - self.v[0] * math.sin(angle)
        self.v[0] = newx
        self.v[1] = newy
    
    def rotateX(self, angle):
        newy = self.v[1] * math.cos(angle) + self.v[2] * math.sin(angle)
        newz = self.v[2] * math.cos(angle) - self.v[1] * math.sin(angle)
        self.v[1] = newy
        self.v[2] = newz

    # reset to x=0, y=0, z=0
    def reset(self):
        self.v = [0, 0, 0]

    def __str__(self):
        return str(self.v)