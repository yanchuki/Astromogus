import pygame as pg
from charecters import Player
from map import Camera, Room
from support import rooms_info


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((700, 700))
        self.fr = pg.time.Clock()
        self.camera_group = Camera()

        [Room(self.camera_group, *info) for info in rooms_info]
        self.player = Player(self.camera_group)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            self.screen.fill('black')

            self.camera_group.update()
            self.camera_group.custom_draw(self.player)
            print(Room.ALL_HITBOXES)

            pg.display.update()
            self.fr.tick(60)


game = Game()
game.run()
