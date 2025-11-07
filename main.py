import pygame
from constants import *
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Game clock
    game_clock = pygame.time.Clock()
    dt = 0
    
    #Initiate Player object
    Player_sprite = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)


    #Game loop
    running = True
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, BLACK)
        Player_sprite.update(dt)
        Player_sprite.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)
        dt = dt/1000






if __name__ == "__main__":
    main()
