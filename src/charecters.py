import pygame as pg
from support import walk_images
from map import Room

class Player(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.default_image = pg.transform.scale(pg.image.load("images/pl/idle.png"), (50, 63))
        self.image = self.default_image
        self.walk_images = walk_images

        self.rect = self.image.get_rect(center=(pg.display.get_window_size()[0] // 2,
                                                pg.display.get_window_size()[1] // 2))

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

        self.colliding()

    def move(self):
        self.get_dir()
        self.rect.center += self.direction * self.speed

    def colliding(self):
        flag = False
        for hitbox in Room.ALL_HITBOXES:
            if self.rect.colliderect(hitbox):
                if self.direction.x == 1:
                    self.rect.right = hitbox.left
                elif self.direction.x == -1:
                    self.rect.left = hitbox.right
                if self.direction.y == 1:
                    self.rect.bottom = hitbox.top
                elif self.direction.y == -1:
                    self.rect.top = hitbox.bottom
                flag = True
                break
        return flag



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
