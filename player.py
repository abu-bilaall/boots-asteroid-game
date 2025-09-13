import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        #groups attributes
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS *2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.update_image()
    
    def update_image(self):
        self.image.fill((0, 0, 0, 0))
        color = (255, 255, 255)
        points = self.triangle()
        adjusted_points = [(p.x - self.position.x + PLAYER_RADIUS, p.y - self.position.y + PLAYER_RADIUS) for p in points]
        width = 2
        pygame.draw.polygon(self.image, color, adjusted_points, width)
        self.rect.center = self.position

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        self.update_image()
        screen.blit(self.image, self.rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.update_image()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        self.update_image()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
