import Classes.tile as t
import random
class Wall:

    tiles = [t.Tile("dragon", "red"),t.Tile("dragon", "green"),t.Tile("dragon", "white"),
    t.Tile("manzu", 1),t.Tile("manzu", 2),t.Tile("manzu", 3),t.Tile("manzu", 4),t.Tile("manzu", 5),t.Tile("manzu", 6),t.Tile("manzu", 7),t.Tile("manzu", 8),t.Tile("manzu", 9),
    t.Tile("souzu", 1),t.Tile("souzu", 2),t.Tile("souzu", 3),t.Tile("souzu", 4),t.Tile("souzu", 5),t.Tile("souzu", 6),t.Tile("souzu", 7),t.Tile("souzu", 8),t.Tile("souzu", 9),
    t.Tile("pinzu", 1),t.Tile("pinzu", 2),t.Tile("pinzu", 3),t.Tile("pinzu", 4),t.Tile("pinzu", 5),t.Tile("pinzu", 6),t.Tile("pinzu", 7),t.Tile("pinzu", 8),t.Tile("pinzu", 9),
    t.Tile("wind", "north"),t.Tile("wind", "west"),t.Tile("wind", "south"),t.Tile("wind", "east")]


    n_dora=1

    def mount_wall(tiles):
        live=[]
        for tile in tiles:
            live.append(tile)
            live.append(tile)
            live.append(tile)
            live.append(tile)
        random.shuffle(live)

        return live[-14:], live[:-14]

    def __init__(self) -> None:
        
        self.dead_wall, self.live_wall= self.mount_wall(self.tiles)
        self.dead_wall.reverse()

    def draw(self):
        draw = self.live_wall[0]
        self.live_wall.pop(0)
        return draw