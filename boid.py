import random
from py5 import Py5Vector


class Boid():
    def __init__(self):
        from main import x_screen_size, y_screen_size
        self.position = Py5Vector(random.randint(0,x_screen_size),random.randint(0,y_screen_size))
        self.velocity = Py5Vector(random.random(),random.random())
        self.velocity.set_mag(random.randint(2,4))
        self.acceleration = Py5Vector(random.uniform(-1,1),random.uniform(-1,1))
        self.vision = 50
        self.maxSpeed = 4
        self.maxForce = 0.2

    def update(self):
        self.position +=  self.velocity
        self.velocity += self.acceleration
        self.velocity.set_limit(self.maxSpeed)

    def border(self):
        from main import x_screen_size, y_screen_size
        if self.position[0] < 50:
            self.position[0] += x_screen_size - 100
        if self.position[0] > x_screen_size - 50: 
            self.position[0] -= x_screen_size - 100 
        if self.position[1] < 50:
            self.position[1] += y_screen_size - 100 
        if self.position[1] > y_screen_size - 50:
            self.position[1] -= y_screen_size - 100

    def flock(self, Boids):
        acceleration = Py5Vector(0,0)
        allign = Py5Vector(Boid.allign(self, Boids))
        cohesion = Py5Vector(Boid.cohes(self, Boids))
        separation = Py5Vector(Boid.sep(self, Boids))
        acceleration = Py5Vector(acceleration) + Py5Vector(allign) 
        acceleration =  Py5Vector(acceleration) + Py5Vector(cohesion) 
        acceleration = Py5Vector(acceleration) + Py5Vector(separation)
        self.acceleration = acceleration
    
    def allign(self, flock):
        average = Py5Vector(0,0)
        vision = self.vision
        total = 0
        for i in flock:
            distance = Py5Vector.dist(self.position, i.position)
            if (self != i and distance < vision):
                average = Py5Vector(average) + i.velocity
                total += 1
        if total > 0:
            average = Py5Vector(average) / total
            average.set_mag(self.maxSpeed)
            average = Py5Vector(average) - self.velocity
            average.set_limit(self.maxForce)
        return average
    
    def cohes(self, flock):
        average = Py5Vector(0,0)
        vision = self.vision
        total = 0
        for i in flock:
            distance = Py5Vector.dist(self.position, i.position)
            if (self != i and distance < vision):
                average = Py5Vector(average) + i.position
                total += 1
        if total > 0:
            average = Py5Vector(average) / total
            average = Py5Vector(average) - self.position
            average.set_mag(self.maxSpeed)
            average = Py5Vector(average) - self.velocity
            average.set_limit(self.maxForce)
        return average

    def sep(self, flock):
        average = Py5Vector(0,0)
        vision = self.vision
        total = 0
        for i in flock:
            distance = Py5Vector.dist(self.position, i.position)
            if (self != i and distance < vision):
                diff = self.position - Py5Vector(i.position)
                diff = Py5Vector(diff) / distance 
                average = Py5Vector(average) + diff
                total += 1
        if total > 0:
            average = Py5Vector(average) / total
            average.set_mag(self.maxSpeed)
            average = Py5Vector(average) - self.velocity
            average.set_limit(self.maxForce)
        return average

