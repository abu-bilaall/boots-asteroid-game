import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #groups attributes
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.update_image()

    def update_image(self):
        self.image.fill((0, 0, 0, 0))
        white = (255, 255, 255)
        pygame.draw.circle(self.image, white, (self.radius, self.radius), self.radius, width=2)
        self.rect.center = self.position

    def draw(self, screen):
        self.update_image()
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt
        self.update_image()

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        else:
            random_angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(random_angle)
            vec2 = self.velocity.rotate(-random_angle)
            new_radius =self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vec1 * 1.2
            asteroid2.velocity = vec2 * 1.2