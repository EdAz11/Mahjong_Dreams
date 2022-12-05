import Classes.player as p
import Classes.wall as w
import Classes.tile as t

completed_melds=[]
temp_melds=[]
walls = w.Wall()

def discard(self,tile_index):
    if tile_index>=0:
        self.player.discard(tile_index)
        self.player.tile_to_hand(tile_drawn)
    
    tile_drawn= walls.draw()

def appendPop(hand, index=0, secnd_ind=0, last_ind=0):
    melds=[]
    melds.append([t.Tile(hand[index].suit, hand[index].value),
                                    t.Tile(hand[index+secnd_ind].suit, hand[index+secnd_ind].value),
                                    t.Tile(hand[index+last_ind].suit, hand[index+last_ind].value)])
    
    if melds not in completed_melds:
        completed_melds.append(melds)

    hand.pop(last_ind)
    hand.pop(secnd_ind)
    hand.pop(0)

    return hand


def check_tempai(hand):
    temp_hand= hand
    check_meld=[]
    index = 0
    check_index=0
    #cycle list
    #check for 3/2 of kind then for sequences
    print("Current hand size: ", len(temp_hand))
    while index < len(temp_hand):
        #check 3 of a kind
        if index<len(temp_hand)-2:
            if check_index>= len(check_meld):
                check_index=len(check_meld)-1
            if (temp_hand[index].suit ==temp_hand[index+1].suit) & (temp_hand[index].value ==temp_hand[index+1].value):
                check_meld.append([temp_hand[index], temp_hand[index+1]])
                if index<len(temp_hand)-3:
                    if check_index>= len(check_meld):
                        check_index=len(check_meld)-1
                    if (temp_hand[index].suit ==temp_hand[index+2].suit) & (temp_hand[index].value ==temp_hand[index+2].value):
                        check_meld.pop(check_index)
                        temp_hand= appendPop(temp_hand)
                        if check_index>= len(check_meld):
                            check_index=len(check_meld)-1
                        if index >= len(temp_hand):
                            index = len(temp_hand)-1

             # check same value type (to separate dragons from numbers and numbers from winds)
            elif type(temp_hand[index].value) == type(temp_hand[index+1].value):
                #sequence distance +1      
                if (temp_hand[index].suit ==temp_hand[index+1].suit) & (temp_hand[index].suit !="dragon")& (temp_hand[index].suit !="wind"):
                    if(temp_hand[index].value ==temp_hand[index+1].value-1):
                        check_meld.append([temp_hand[index], temp_hand[index+1]])

                        #value type check again
                        if index<len(temp_hand)-3:
                            if check_index>= len(check_meld):
                                check_index=len(check_meld)-1
                            if type(temp_hand[index].value) == type(temp_hand[index+2].value):
                                #sequence distance +2
                                if (temp_hand[index].suit ==temp_hand[index+2].suit) & (temp_hand[index].value ==temp_hand[index+2].value-2):
                                    check_meld.pop(check_index)
                                    temp_hand= appendPop(temp_hand, index,1,2)
                                    if check_index>= len(check_meld):
                                        check_index=len(check_meld)-1
                                    if index >= len(temp_hand):
                                        index = len(temp_hand)-1

                                # third type check
                                if index<len(temp_hand)-4:
                                    if check_index>= len(check_meld):
                                        check_index=len(check_meld)-1
                                    if type(temp_hand[index].value) == type(temp_hand[index+3].value):
                                        #sequence distance +3
                                            if (temp_hand[index].suit ==temp_hand[index+3].suit) & (temp_hand[index].value ==temp_hand[index+3].value-2):
                                                check_meld.pop(check_index)
                                                temp_hand= appendPop(temp_hand, index,1,3)
                                                if check_index>= len(check_meld):
                                                    check_index=len(check_meld)-1
                                                if index >= len(temp_hand):
                                                    index = len(temp_hand)-1
                                        
                                            # 4th type check
                                            if index<len(temp_hand)-5:
                                                if check_index>= len(check_meld):
                                                    check_index=len(check_meld)-1
                                                if type(temp_hand[index].value) == type(temp_hand[index+4].value):
                                                #sequence distance +4
                                                    if (temp_hand[index].suit ==temp_hand[index+4].suit) & (temp_hand[index].value ==temp_hand[index+4].value-2):
                                                        check_meld.pop(check_index)
                                                        temp_hand= appendPop(temp_hand, index,1,4)
                                                        if check_index>= len(check_meld):
                                                            check_index=len(check_meld)-1
                                                        if index >= len(temp_hand):
                                                            index = len(temp_hand)-1
                                                
                                                    # FINAL type check
                                                    if index<len(temp_hand)-6:
                                                        if check_index>= len(check_meld):
                                                            check_index=len(check_meld)-1
                                                        if type(temp_hand[index].value) == type(temp_hand[index+5].value):
                                                        #sequence distance +5
                                                            if (temp_hand[index].suit ==temp_hand[index+5].suit) & (temp_hand[index].value ==temp_hand[index+5].value-2):
                                                                check_meld.pop(check_index)
                                                                temp_hand= appendPop(temp_hand, index,1,5)
                                                                if check_index>= len(check_meld):
                                                                    check_index-=len(check_meld)-1
                                                                if index >= len(temp_hand):
                                                                    index = len(temp_hand)-1
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
    if len(temp_hand)==0:
        print("You didn't reach tempai, better luck next time.")
        exit()
    return False

def draw_initial_hand():
    hand_tiles =[]
    while len(hand_tiles) !=13:
        draw=walls.draw()
        hand_tiles.append(draw)
    hand_tiles = sorted(hand_tiles, key=lambda x: (x.suit, x.value), reverse=False)
    return hand_tiles

# decode action taken from FF2 interface

def decode_action(key):
    if key== 1:
        return t.Tile("dragon", "green")
    if key== 2:
        return t.Tile("dragon", "red")
    if key== 3:
        return t.Tile("dragon", "white")
    if key==4:
        return t.Tile("manzu", 1)
    if key==5:
        return t.Tile("manzu", 2)
    if key==6:
        return t.Tile("manzu", 3)
    if key==7:
        return t.Tile("manzu", 4)
    if key==8:
        return t.Tile("manzu", 5)
    if key==9:
        return t.Tile("manzu", 6)
    if key==10:
        return t.Tile("manzu", 7)
    if key==11:
        return t.Tile("manzu", 8)
    if key==12:
        return t.Tile("manzu", 9)
    if key==13:
        return t.Tile("pinzu", 1)
    if key==14:
        return t.Tile("pinzu", 2)
    if key==15:
        return t.Tile("pinzu", 3)
    if key==16:
        return t.Tile("pinzu", 4)
    if key==17:
        return t.Tile("pinzu", 5)
    if key==18:
        return t.Tile("pinzu", 6)
    if key==19:
        return t.Tile("pinzu", 7)
    if key==20:
        return t.Tile("pinzu", 8)
    if key==21:
        return t.Tile("pinzu", 9)
    if key==22:
        return t.Tile("souzu", 1)
    if key==23:
        return t.Tile("souzu", 2)
    if key==24:
        return t.Tile("souzu", 3)
    if key==25:
        return t.Tile("souzu", 4)
    if key==26:
        return t.Tile("souzu", 5)
    if key==27:
        return t.Tile("souzu", 6)
    if key==28:
        return t.Tile("souzu", 7)
    if key==29:
        return t.Tile("souzu", 8)
    if key==30:
        return t.Tile("souzu", 9)
    if key==31:
        return t.Tile("wind", "east")
    if key==32:
        return t.Tile("wind", "north")
    if key==33:
        return t.Tile("wind", "south")
    if key==34:
        return t.Tile("wind", "west")


#TODO link network code to game (both train and test modes)
#TODO TRAIN

def start_ai_game():
    return


def game_loop_train():
    walls = w.Wall()

    player = p.Player(draw_initial_hand())

    while len(walls.live_wall) >0:
        #print(player.)
        return


def game_loop():

    walls = w.Wall()
    player = p.Player(draw_initial_hand())
    extra = walls.draw()
    tempai=False
    
    while len(walls.live_wall) >0 or tempai:
        hands = player.showhand()
        print("Your current hand is " + hands + ".")
        if type(extra.value) == type(" "):
            print("You drew the " + extra.value + " " + extra.suit, "tile")
        else:
            print("You drew the", extra.value, extra.suit, "tile")
        
        print("Choose from numbers 1 to 14 the tile to discard")
        while True:
            answer = int(input())
            if type(answer) == type(1):
                if answer >=0 and answer<len(player.hand):
                    player.discard(answer-1)
                    player.tile_to_hand(extra)
                    tempai=check_tempai(player.hand)
                    extra= walls.draw()
                    break
                if answer==14:
                    extra= walls.draw()
                    break
            if tempai:
                print("You have reached tempai, congratulations")
                exit()
            print(player.showhand())
            print("Please pick a number from 1 to 14")

        print(len(walls.live_wall), " tiles left in the live wall")
                
            



    return

def start_game():

    game_mode=""
    
    while game_mode!="ai" or game_mode!="p":
        print("Train AI(ai) or (p)ractice?")
        game_mode= input().lower()
        if game_mode=="ai" or game_mode=="p":
            break
        

    print("Starting game in ", game_mode, " mode.")
    #return walls, player, tile_drawn

    if game_mode=="ai":
        game_loop_train()
    else:
        game_loop()
    
start_game()