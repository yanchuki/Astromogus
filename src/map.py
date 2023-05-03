import pygame as pg
from support import get_hitboxes
from charecters import Player


class Room(pg.sprite.Sprite):
    ALL_HITBOXES = []

    def __init__(self, group, image_path: str, pos: tuple, style: str):
        super().__init__(group)
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(topleft=pos)

        self.hitboxes = get_hitboxes(pos, style)
        self.ALL_HITBOXES.extend(self.hitboxes)

    def hitboxes_update(self, player):
        for hitbox in self.hitboxes:
            hitbox.center -= player.direction * player.speed



class Camera(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.offset = pg.math.Vector2()

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):
        self.center_target_camera(player)
        hitboxes = []
        for sprite in self.sprites():
            if isinstance(sprite, Room):
                hitboxes.extend(sprite.hitboxes)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            if not isinstance(sprite, Player):
                self.display_surface.blit(sprite.image, offset_pos)
            else:
                self.display_surface.blit(sprite.image, player.hitbox)
            if isinstance(sprite, Room):
                sprite.hitboxes_update(player)
                for hitbox in hitboxes:
                    pg.draw.rect(self.display_surface, 'red', hitbox, 2)
        player.colliding(hitboxes)
        pg.draw.rect(pg.display.get_surface(), 'red', player.hitbox, 2)
#  and not player.rect.collidelistall(Room.ALL_HITBOXES)