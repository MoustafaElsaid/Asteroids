import pygame
from constants import *

def main():
    pygame.init() # Initializing the game
    clock = pygame.time.Clock() # starting the clock
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()  # refreshing the screen every frame
        clock.tick(60)
        dt = clock.tick(60)/1000



print ("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":           # This makes sure that the main() function is called when the file is called in the Terminal.
    main()