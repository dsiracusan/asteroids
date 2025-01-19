# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
import time
from asteroid import *
from asteroidfield import *   
from shot import *


def main():
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable= pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Shot.containers=(updateable, drawable, shots)
    AsteroidField.containers= (updateable)
    Asteroid.containers= (asteroids,updateable,drawable)
    Player.containers=(updateable, drawable)
    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroidfield=AsteroidField()
    
    dt=0
    last_print_time = 0  # Tracks the last time we printed a message
    PRINT_INTERVAL = 10  # Interval in seconds
    while True:
        current_time = time.time()
        screen.fill("black")
        
        if current_time - last_print_time >= PRINT_INTERVAL:
            print("running")
            last_print_time = current_time
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            print("asteroids closed")
            sys.exit()
        
        
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                pygame.quit()
                sys.exit()
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    new_asteroids= asteroid.split()
                    if new_asteroids:
                        asteroids.add (*new_asteroids)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updateable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)

        
        
        dt=clock.tick(60)/1000
        pygame.display.flip()
    
        
        
    
    
    if __name__ == "__main__":
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")




main()