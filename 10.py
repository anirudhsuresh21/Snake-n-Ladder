from random import randint
print("-------------------------SNAKES N LADDERS-------------------------")

#defining global variables
global idn,val,idn1, val1,num_players,player1,player2,  player3,player4
#function to find if the user has found a ladder
def ladders(x):
    #usage of arrays/lists according to the project requirements
    lad1 = [2,7,20,33,41,53]
    lad2 = [25,31,44,76,96,89]
    global idn, val, idn1, val1
    if x in lad1:
        idn = lad1.index(x)
        val = lad2[idn]
        return val
    else:
        return x

#function to find if the user has found a snake
def snakes(x):
    #usage of arrays/lists according to the project requirements
    sna1 = [40,46,99,70,83,92]
    sna2 = [5,11,23,27,57,48]
    global idn, val, idn1, val1
    if x in sna1:
        idn1 = sna1.index(x)
        val1 = sna2[idn1]
        return val1
    else:
        return x

#Main running block of the Progarm
def start():
    global idn, val, idn1, val1, num_players, player1, player2, player3, player4
    play = input("Please 'click' ENTER to Start the Game")
    if play == "":
        #selection of mode
        mode = int(input("Select your Mode.\n\t1.v/s Computer.\n\t2.Multiplayer."))
        if mode == 1:
            player1=input("Enter player 1 name: ")
            player2 = "Computer"
            num_players = 2
            
        elif mode == 2:
            num_players = int(input("Enter the Number of Players : "))
            if 5>num_players>1:
                player2=input("\nEnter player 2 name: \n")
                
            if 5>num_players>2:
                player3=input("Enter player 3 name: \n")
                
            if 5>num_players>3:
                player4=input("Enter player 4 name: \n")

            print("Good Luck!")
        else:
            print("Try Again.......!")
            start()
        print()
        #calling the function according to the no. of players
        while True:
            on_play()                   
            break                                                
    elif play=="exit" or play=="Exit":
        quit()
    else:
        print("Try Again.......!")
        start()

def on_play():
    global idn, val, idn1, val1, num_players, player1, player2, player3, player4
    play2=input("Press Enter to start.")
    if play2=="":
        player1_score=player2_score=player3_score=player4_score=0
        while True:
                if 5>num_players>1:
                    player1_score=play_on(player1,player1_score)
                    if player1_score==100:
                        break
                    player2_score=play_on(player2,player2_score)
                    if player2_score==100:
                        break
                if 5>num_players>2:
                    player3_score=play_on(player3,player3_score)
                    if player3_score==100:
                        break    
                if 5>num_players>3:
                    player4_score=play_on(player4,player4_score)
                    if player4_score==100:
                        break
                print("________________________________________________________________")
    else:
        print("Try Again.......!")
        on_play()
#Main running algorithm of the game 
def play_on(player,score): 
    global idn, val, idn1, val1
    print()
    print("It's",player,"turn.")
    roll_dice=input("Please 'Click' ENTER to Roll\n")
    if roll_dice=="":
        a=randint(1,6)
        #player dice roll
        print(player,"rolled the dice")
        print(player,"got a",a)
        score+=a
        if score<=100:
            lad_score=ladders(score)
            #checking for ladders for player
            if lad_score!=score:
                print("There's a ladder!\n",player,"climbed up by",(lad_score-score),"places")
                score=lad_score
            snk_score=snakes(score)
            if snk_score!=score:
                #checking for snakes for player
                print("Fella You got 'Unlucky' You found a Snake at ",score)
                print(player,"got bitten by a snake!\n",player,"fell down by",(score-snk_score),"places")
                score=snk_score
            print(player,"is now on box",score)    
        else:
            #checks if player score is not grater than 100
            score-=a
            print(player,"can't move.")
            print(player,"is still on box",score)
        if score==100:
            print()
            print(player,"Wins!")
        return score
    else:
        print("Try Again...!")
        play_on()
start()
