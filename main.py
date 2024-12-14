import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for object in updatable:
            object.update(dt)

        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        
        for object in asteroids:
            if object.check_collision(player):
                print("Game over!")
                return
            for shot in shots:
                if object.check_collision(shot):
                    object.split()
                    shot.kill()
            
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(240) / 1000

if __name__ == "__main__":
    main()