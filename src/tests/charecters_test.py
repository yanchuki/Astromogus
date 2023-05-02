import pygame as pg
from support_info import walk_images


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.default_img = pg.transform.scale(pg.image.load("../images/pl/idle.png"), (50, 63))
        self.image = self.default_img
        self.rect = self.image.get_rect(center=(500, 312))
        self.walk_img = walk_images

        self.timer = 0
        self.dirx = 1
        self.diry = 1

    def animate(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d] or keys[pg.K_a] or keys[pg.K_s] or keys[pg.K_w]:
            self.timer += 1
            if self.timer == 60:
                self.timer = 0
            if keys[pg.K_d] or keys[pg.K_s]:
                self.image = self.walk_img[self.timer // 5]
            elif keys[pg.K_a] or keys[pg.K_w]:
                self.image = pg.transform.flip(self.walk_img[self.timer // 5], True, False)
        else:
            if self.dirx == 1:
                self.image = self.default_img
            else:
                self.image = pg.transform.flip(self.default_img, True, False)

    def changedir(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.dirx = -1
        elif keys[pg.K_d]:
            self.dirx = 1
        else:
            self.dirx = 0
        if keys[pg.K_s]:
            self.diry = 1
        elif keys[pg.K_w]:
            self.diry = -1
        else:
            self.diry = 0

    def collide(self, main_map: pg.sprite.Group):
        for sprite in main_map.sprites():
            for hitbox in sprite.hitboxes:
                if self.rect.colliderect(hitbox):
                    if self.dirx == 1:
                        self.rect.right = hitbox.left
                    elif self.dirx == -1:
                        self.rect.left = hitbox.right
                    elif self.diry == 1:
                        self.rect.bottom = hitbox.top
                    elif self.diry == -1:
                        self.rect.top = hitbox.bottom

    def update(self, main_map):
        self.collide(main_map)
        self.animate()
        self.changedir()
        pg.display.get_surface().blit(self.image, self.rect)
