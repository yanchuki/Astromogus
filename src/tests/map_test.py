import pygame as pg

class Room(pg.sprite.Sprite):

    def __init__(self, image_path: str, pos: tuple, style: str):
        super().__init__()
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(topleft=pos)
        if style == "communication":
            self.hitboxes = [
                pg.Rect(pos[0], pos[1], 250, 125),
                pg.Rect(pos[0] + 375, pos[1], 65, 100),
                pg.Rect(pos[0], pos[1]+122, 15, 155),
                pg.Rect(pos[0] + 10, pos[1] + 205, 57, 75),
                pg.Rect(pos[0] + 130, pos[1] + 300, 210, 70),
                pg.Rect(pos[0] + 380, pos[1] + 205, 57, 75),
                pg.Rect(pos[0] + 427, pos[1] + 100, 15, 155)
            ]
        elif style == "com_eng_caf":
            self.hitboxes = [
                pg.Rect(pos[0] + 13, pos[1], 727, 10),
                pg.Rect(pos[0] + 25, pos[1] + 166, 390, 10),
                pg.Rect(pos[0] + 548, pos[1] + 170, 175, 10)
            ]
        elif style == "cafeteria":
            self.hitboxes = [
                pg.Rect(pos[0] + 191, pos[1] + 10, 530, 66),
                pg.Rect(pos[0] + 15, pos[1] + 160, 17, 205),
                pg.Rect(pos[0] + 15, pos[1] + 533, 20, 200),
                pg.Rect(pos[0] + 228, pos[1] + 934, 198, 22),
                pg.Rect(pos[0] + 550, pos[1] + 934, 198, 22),
                pg.Rect(pos[0] + 955, pos[1] + 533, 20, 200),
                pg.Rect(pos[0] + 955, pos[1] + 245, 17, 140)
            ]
        elif style == "up_eng":
            self.hitboxes = [
                pg.Rect(pos[0] + 107, pos[1], 293, 10),
                pg.Rect(pos[0] + 400, pos[1] + 3, 10, 115),
                pg.Rect(pos[0], pos[1] + 146, 317, 191),
                pg.Rect(pos[0] + 292, pos[1] + 438, 118, 13),
                pg.Rect(pos[0] + 397, pos[1] + 270, 11, 178),
                pg.Rect(pos[0], pos[1] + 438, 165, 13),
                pg.Rect(pos[0], pos[1] + 335, 6, 110)
            ]
        elif style == "bed_hall":
            self.hitboxes = [
                pg.Rect(pos[0], pos[1], 10, 303),
                pg.Rect(pos[0] + 135, pos[1], 12, 119),
                pg.Rect(pos[0] + 135, pos[1] + 264, 12, 49)



            ]




    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.rect.x -= 4
        elif keys[pg.K_a]:
            self.rect.x += 4
        if keys[pg.K_w]:
            self.rect.y += 4
        elif keys[pg.K_s]:
            self.rect.y -= 4
        for i in self.hitboxes:
            if keys[pg.K_d]:
                i.x -= 4
            elif keys[pg.K_a]:
                i.x += 4
            if keys[pg.K_w]:
                i.y += 4
            elif keys[pg.K_s]:
                i.y -= 4
            pg.draw.rect(pg.display.get_surface(), 'red', i, 5)

    def update(self, display):
        display.blit(self.image.convert_alpha(), self.rect)
        self.move()
