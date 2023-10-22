import random
from quadtree import *
from py5 import Py5Vector

class Boid():
    def __init__(self):
        from main import x_screen_size, y_screen_size
        self.position = Py5Vector(random.randint(0,x_screen_size),random.randint(0,y_screen_size))
        self.velocity = Py5Vector(random.uniform(-1,1),random.uniform(-1,1))
        self.velocity.set_mag(random.randint(2,4))
        self.acceleration = Py5Vector(random.uniform(-1,1),random.uniform(-1,1))
        self.vision = 100
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
        x, y, z = self.flocking_rules(Boids)

        acceleration = Py5Vector(acceleration) + Py5Vector(x) 
        acceleration =  Py5Vector(acceleration) + Py5Vector(y) 
        acceleration = Py5Vector(acceleration) + Py5Vector(z) 
        
        self.acceleration = acceleration

    def flocking_rules(self, flock):
            average_allign = Py5Vector(0,0) 
            average_cohesion = Py5Vector(0,0) 
            average_sep = Py5Vector(0,0)
            vision = self.vision
            total = 0
            for i in flock:
                # i = i.userData - used for quadtree
                distance = Py5Vector.dist(self.position, i.position)
                if (self != i and distance < vision):
                    average_allign = Py5Vector(average_allign) + i.velocity
                    average_cohesion = Py5Vector(average_cohesion) + i.position
                    diff = self.position - Py5Vector(i.position)
                    diff = Py5Vector(diff) / distance 
                    average_sep = Py5Vector(average_sep) + diff
                    total += 1
            if total > 0:
                average_allign = self.calc_avg(average_allign, total)
                average_cohesion = self.calc_avg(average_cohesion, total, True)
                average_sep = self.calc_avg(average_sep, total)
            return average_allign, average_cohesion, average_sep
    
    def calc_avg(self, v, total, coh = False):
        v = Py5Vector(v) / total
        if coh:
            v = Py5Vector(v) - self.position
        v.set_mag(self.maxSpeed)
        v = Py5Vector(v) - self.velocity
        v.set_limit(self.maxForce)
        return v
