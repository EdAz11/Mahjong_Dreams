import Classes.tile as t
import operator

class Player:



    def __init__(self, hand):
        self.hand = hand
        self.hand = sorted(self.hand, key=lambda x: (x.suit, x.value), reverse=False)

    def tile_to_hand(self, draw):
        self.hand.append(draw)
        self.hand = sorted(self.hand, key=lambda x: (x.suit, x.value), reverse=False)
        

    def discard(self, tile):
        self.hand.pop(tile)

    def showhand(self):
        i=0
        repeat_counter=0
        hand_str=""
        current_suit=""
        while i <len(self.hand):
            if self.hand[i].suit != current_suit:
                if current_suit== self.hand[i].suit == "dragon" or current_suit== self.hand[i].suit =="wind":
                    hand_str+=current_suit
                elif self.hand[i].suit[0] != current_suit:
                    if self.hand[i].suit == "manzu":
                        hand_str+=current_suit
                        current_suit="m"
                    elif self.hand[i].suit =="pinzu":
                        hand_str+=current_suit
                        current_suit="p"
                    elif self.hand[i].suit =="souzu":
                        hand_str+=current_suit
                        current_suit="s"
                else:
                    current_suit == self.hand[i].suit

            if self.hand[i].suit == "dragon" or self.hand[i].suit == "wind":
                hand_str+= self.hand[i].value[0].upper()
            else:

                temp_str = str(self.hand[i].value)[0]
                hand_str= hand_str+temp_str
                #hand_str = operator.concat(hand_str, temp_str)
                
            i+=1
        if (current_suit!="wind") & (current_suit!="dragon") & ((current_suit=="s") or (current_suit=="p") or (current_suit=="m")):
            hand_str+=current_suit
            

        return hand_str