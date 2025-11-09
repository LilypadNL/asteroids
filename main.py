import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys

def main():
    #Initializing game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    #Game clock
    game_clock = pygame.time.Clock()
    dt = 0
   

    #Defining groups and membership
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)


    #Initiate Player object
    Player_sprite = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)   
    AsteroidField_sprite = AsteroidField()


    #Game loop
    running = True
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, BLACK)
        updatable.update(dt)
        for asteroid in asteroids:
            if Player.collides_with(Player_sprite, asteroid) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)
        dt = dt/1000






if __name__ == "__main__":
    main()
