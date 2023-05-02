import pygame as pg
from charecters import Player
from map_test import Room

main_map = pg.sprite.Group(

    Room('../images/lci/up_engine.png', (0, 260), "up_eng"),
    Room("../images/lci/hall1.png", (385, 363), "com_eng_caf"),
    Room("../images/lci/com.png", (557, 540), "communication"),
    Room("../images/lci/cafeteria.png", (1100, 0), "cafeteria"),
    Room('../images/lci/hall2.png', (1515, 960), "bed_hall")
    # Room('images/lci/hall2.png', (1692, 1142))
)

screen = pg.display.set_mode((1000, 625))
fps = pg.time.Clock()
pl = Player()
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
    screen.fill("black")
    main_map.update(screen)
    pl.update(main_map)
    fps.tick(120)

    pg.display.update()
