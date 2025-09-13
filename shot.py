import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        #groups attributes
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.update_image()

    def update_image(self):
        self.image.fill((0, 0, 0, 0))
        white = (255, 255, 255)
        pygame.draw.circle(self.image, white, (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS, width=2)
        self.rect.center = (self.position.x, self.position.y)

    def draw(self, screen):
        self.update_image()
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt
        self.update_image()
