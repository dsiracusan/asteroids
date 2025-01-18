# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
import time

    


def main():
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    dt=0
    last_print_time = 0  # Tracks the last time we printed a message
    PRINT_INTERVAL = 10  # Interval in seconds
    while True:
        current_time = time.time()

        if current_time - last_print_time >= PRINT_INTERVAL:
            print("running")
            last_print_time = current_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        dt=clock.tick(60)/1000
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()
    
        
        
    
    
    if __name__ == "__main__":
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")




main()