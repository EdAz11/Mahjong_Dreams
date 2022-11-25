import tile as t

class Player:



    def __init__(self, hand, draw):
        self.hand = hand
        self.draw = draw

    def tile_to_hand(self, draw):
        self.hand.append(draw)
        return sorted(self.hand, key=lambda x: (x.suit, x.value), reverse=False)

    def discard(self, tile):
        return self.hand.pop(tile)

