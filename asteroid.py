from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x, y, radius, velocity):
        super().__init__(x,y, radius)
        self.velocity= pygame.math.Vector2(velocity)
        


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width= 2 )

    def update(self,dt):
        asteroid_velocity=self.velocity*dt
        self.position += asteroid_velocity
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle =random.uniform(20,50)
        velocity_1=self.velocity.rotate(random_angle)
        velocity_2=self.velocity.rotate(-random_angle)
        velocity_1 *= 1.2
        velocity_2 *=1.2
        new_radius= self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, velocity_1)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, velocity_2)
        return asteroid_1, asteroid_2
            

        
