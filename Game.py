import Classes.player as p
import Classes.wall as w
import Classes.tile as t

completed_melds=[]
temp_melds=[]

def start_game():
    walls = w.Wall
    player = p.Player()
    
    tile_drawn = walls.draw()

    return walls, player, tile_drawn

def discard(tile_index):
    if tile_index>=0:
        player.discard(tile_index)
        player.tile_to_hand(tile_drawn)
    
    tile_drawn= walls.draw()

def appendPop(hand, secnd_ind=0, last_ind=0):
    completed_melds.append([t.Tile(hand[0].suit, hand[0].value),
                                    t.Tile(hand[secnd_ind].suit, hand[secnd_ind].value),
                                    t.Tile(hand[last_ind].suit, hand[last_ind].value)])
    hand.pop(last_ind)
    hand.pop(secnd_ind)
    hand.pop(0)

    return hand, meld


def check_tempai(hand):
    temp_hand= hand
    check_meld=[]
    index = 0
    check_index=0
    #cycle list
    #check for 3/2of kind then for sequences
    while index < len(temp_hand):
        #check 3 of a kind
        if (temp_hand[index].suit ==temp_hand[index+1].suit) & (temp_hand[index].value ==temp_hand[index+1].value):
            check_meld.append([temp_hand[index], temp_hand[index+1]])
            if (temp_hand[index].suit ==temp_hand[index+2].suit) & (temp_hand[index].value ==temp_hand[index+2].value):
                check_meld.pop(check_index)
                temp_hand= appendPop(temp_hand)
                if check_index>= len(check_meld):
                    check_index-=1

        # check same value type (to separate dragons from numbers and numbers from winds)
        elif type(temp_hand[index].value) == type(temp_hand[index+1].value):
            #sequence distance +1      
            if (temp_hand[index].suit ==temp_hand[index+1].suit) & (temp_hand[index].value ==temp_hand[index+1].value-1):
                check_meld.append([temp_hand[index], temp_hand[index+1]])

                #value type check again
                if type(temp_hand[index].value) == type(temp_hand[index+2].value):
                    #sequence distance +2
                    if (temp_hand[index].suit ==temp_hand[index+2].suit) & (temp_hand[index].value ==temp_hand[index+2].value-2):
                        check_meld.pop(check_index)
                        temp_hand= appendPop(temp_hand,1,2)
                        if check_index>= len(check_meld):
                            check_index-=1

                    # third type check
                    if type(temp_hand[index].value) == type(temp_hand[index+3].value):
                        #sequence distance +3
                        if (temp_hand[index].suit ==temp_hand[index+3].suit) & (temp_hand[index].value ==temp_hand[index+3].value-2):
                            check_meld.pop(check_index)
                            temp_hand= appendPop(temp_hand,1,3)
                            if check_index>= len(check_meld):
                                check_index-=1
                        
                        # 4th type check
                        if type(temp_hand[index].value) == type(temp_hand[index+4].value):
                        #sequence distance +4
                            if (temp_hand[index].suit ==temp_hand[index+4].suit) & (temp_hand[index].value ==temp_hand[index+4].value-2):
                                check_meld.pop(check_index)
                                temp_hand= appendPop(temp_hand,1,4)
                                if check_index>= len(check_meld):
                                    check_index-=1
                            
                            # FINAL type check
                            if type(temp_hand[index].value) == type(temp_hand[index+5].value):
                            #sequence distance +5
                                if (temp_hand[index].suit ==temp_hand[index+5].suit) & (temp_hand[index].value ==temp_hand[index+5].value-2):
                                    check_meld.pop(check_index)
                                    temp_hand= appendPop(temp_hand,1,5)
                                    if check_index>= len(check_meld):
                                        check_index-=1
        index+=1
        check_index+=1



    #now check the tiles that are left in the "temp_hand" and "check_meld"

    #edge case 1: seven pairs
    true_checks=0
    for melds in check_meld:
        if melds[0].value == melds[1].value:
            true_checks+=1
    if true_checks == len(check_meld):
        return True

    #regular cases
        #single wait
    if len(completed_melds) ==4 & len(temp_hand) == 1:
        return True
        #dual wait
    elif len(completed_melds)== 3 & len(check_meld)==2:
        #double pair wait
        if (check_meld[0][0].value == check_meld[0][1].value) & (check_meld[1][0].value== check_meld[1][1].value):
            return True
        #double wait on sequence extremity
        elif (check_meld[0][0].suit==check_meld[1][0].suit) & type(check_meld[0][0].value==int):
            if (check_meld[0][0].value==check_meld[0][1].value) & (check_meld[1][0].value==check_meld[1][1].value+1):
                return True
            elif (check_meld[0][0].value==check_meld[0][1].value+1) & (check_meld[1][0].value==check_meld[1][1].value+1):
                return True
            elif (check_meld[0][0].value==check_meld[0][1].value+1) & (check_meld[1][0].value==check_meld[1][1].value):
                return True
    
    
    return False


walls, player, tile_drawn = start_game()