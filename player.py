from circleshape import *
from constants import *
import sys
from shot import *

class Player(CircleShape):
    def __init__ (self, x, y, PLAYER_RADIUS):
        super().__init__(x,y, PLAYER_RADIUS)

        self.x=x
        self.y=y
        self.rotation=0
        self.shoot_timer=0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width= 2 )

    def rotate(self, dt, direction):
        self.rotation += direction * PLAYER_TURN_SPEED * dt    
        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt
        if keys[pygame.K_a]:
            self.rotate(dt,-1)
        if keys[pygame.K_d]:
            self.rotate(dt,1)
        if keys[pygame.K_w]:
            self.move(dt,1)
        if keys[pygame.K_s]:
            self.move(dt,-1)
        if keys[pygame.K_SPACE]:
            self.shoot()

        
            

    def move(self, dt, direction):

    # Create a unit vector pointing up and rotate it by the player's rotation
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += direction * forward * PLAYER_SPEED * dt
    
    def shoot(self):
        # Create a new shot at the player's position
        shot_position = self.position  # Where the player currently is
        shot_velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        if self.shoot_timer <= 0:
        # Create the Shot object and add it to the shots group
            Shot(shot_position.x, shot_position.y, SHOT_RADIUS, shot_velocity)
            self.shoot_timer = 0.3
        