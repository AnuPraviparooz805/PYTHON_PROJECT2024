import time
import random
import sys
SlEEP_TIME=1
DICE_VALUE=6
MAX_VAL=100
p1_current_position=0
p2_current_position=0
snake_position = {
    12: 4,
    22: 11,
    36: 7,
    53: 31,
    67: 36,
    80: 41,
    84: 53,
    94: 65,
    99: 10
}
ladders_position = {
    3: 26,
    5: 15,
    13: 44,
    25: 51,
    29: 74,
    36: 57,
    42: 72,
    49: 86,
    57: 76,
    61: 93,
    77: 86,
    81: 98,
    88: 91
}
class Snake_Ladder:
   
    def dice_value():
        time.sleep(SlEEP_TIME)
        dice_value = random.randint(1, DICE_VALUE)
        print("Dice value ",str(dice_value))
        return dice_value
 
    def snake_ladder(player_name, current, dice_value):
        time.sleep(SlEEP_TIME)
        old_value = current
        current = current + dice_value
        print("\n",player_name,"moved from ",str(old_value)," to ",str(current))
        if current in snake_position:
            final_value = snake_position.get(current)
            print("\n",player_name,"got a bite from snake. Going down from",str(current),'to',final_value)
        elif current in ladders_position:
            final_value = ladders_position.get(current)
            print("\n",player_name,"is clibing the ladder from",str(current),'to',final_value)

        else:
            final_value = current

        return final_value

    def check_win(player_name, position):
        time.sleep(SlEEP_TIME)
        if  position >= MAX_VAL:
            return position
        if position == MAX_VAL:
            print("\n",player_name,"has  won the game.")
            print("CONGRATULATIONS !!! ",player_name)
            sys.exit(1)

c1=Snake_Ladder
c2=Snake_Ladder
player_1_name=input('Enter player 1 name....').upper()
player_2_name=input('Enter player 2 name....').upper()

while True:
        #player 1
        time.sleep(SlEEP_TIME)
        print("\n",player_1_name)
        input_1 = input("Press enter for rolling the dice: ")
        print(input_1,"\nDice is being rolled...")
        dice_value = c1.dice_value()
        time.sleep(SlEEP_TIME)
       
        print(player_1_name,"moving....")
        p1_current_position =c1.snake_ladder(player_1_name, p1_current_position, dice_value)
        
        c1.check_win(player_1_name, p1_current_position)
        
        #player 2
        print("\n",player_2_name)
        input_2 = input("Press enter for rolling the dice: ")
        print(input_2,"\nDice is being rolled...")
        dice_value = c2.dice_value()
        time.sleep(SlEEP_TIME)
        
        print(player_2_name," moving....")
        p2_current_position = c2.snake_ladder(player_2_name, p2_current_position, dice_value)
        
        
        c2.check_win(player_2_name, p2_current_position)
        
        
        
