import pygame as pg
from support import walk_images


class Player(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.default_image = pg.transform.scale(pg.image.load("images/pl/idle.png"), (50, 63))
        self.image = self.default_image
        self.walk_images = walk_images

        self.rect = self.image.get_rect(center=(pg.display.get_window_size()[0] // 2,
                                                pg.display.get_window_size()[1] // 2))

        self.hitbox = self.rect.copy()

        self.speed = 3
        self.direction = pg.math.Vector2()

        self.animation_timer = 0

    def get_dir(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.direction.x = -1
        elif keys[pg.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pg.K_s]:
            self.direction.y = 1
        elif keys[pg.K_w]:
            self.direction.y = -1
        else:
            self.direction.y = 0

    def colliding(self, hitboxes: list):
        for hitbox in hitboxes:
            if self.hitbox.colliderect(hitbox):
                print('Touch')
                if self.direction.y == -1:
                    self.hitbox.y += self.speed
                elif self.direction.y == 1:
                    self.hitbox.y -= self.speed

                if self.direction.x == -1:
                    self.hitbox.x += self.speed
                elif self.direction.x == 1:
                    self.hitbox.x -= self.speed

                self.direction.y = 0
                self.direction.x = 0

    def move(self):
        self.get_dir()
        self.rect.center += self.direction * self.speed

    def animate(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d] or keys[pg.K_a] or keys[pg.K_s] or keys[pg.K_w]:
            self.animation_timer += 1
            if self.animation_timer == 60:
                self.animation_timer = 0
            if keys[pg.K_d] or keys[pg.K_s]:
                self.image = self.walk_images[self.animation_timer // 5]
            elif keys[pg.K_a] or keys[pg.K_w]:
                self.image = pg.transform.flip(self.walk_images[self.animation_timer // 5], True, False)
        else:
            if self.direction == 1:
                self.image = self.default_image
            else:
                self.image = pg.transform.flip(self.default_image, True, False)

    def update(self):
        self.move()
        self.animate()
