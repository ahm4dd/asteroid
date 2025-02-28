import random
from circleshape import *
from constants import *
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,ASTEROID_MAX_RADIUS)
    
    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if(self.radius == ASTEROID_MIN_RADIUS):
            return
        random_angle = random.uniform(20,50)
        asteroid1_velocity = self.velocity.rotate(random_angle)
        asteroid2_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)

        asteroid_1.velocity = asteroid1_velocity * ASTEROID_SMALLER_SPEED
        asteroid_2.velocity = asteroid2_velocity * ASTEROID_SMALLER_SPEED