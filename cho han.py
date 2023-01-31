"""
The traditional Japanese game "Cho Han" consists of throwing two dices into a glass and then placing it on the ground with
the opening facing down, hiding the dice. Players must guess whether the sum of the dice is Cho(even) or Han(odd).

    - if you guess: You win double what you bet, for example, if you have $10 in your wallet and bet 2, then you have $12.

    - if you don't guess: You lose what you bet, for example, if you have $10 in your wallet and bet $2 then you will have $8.

The game ends when the user runs out of money or enters "no" to continue.

The result of each round should be shown, the money in the wallet and at the end of each round the number of games won by the player
should be shown.
"""

import random as rd 
dice1= [1,2,3,4,5,6] 
dice2= [1,2,3,4,5,6]

wallet= 10
play="YES" 
win=0

print()
print("Welcome to the Cho Han game!")
print()

while play=="YES" and wallet>0:
    rdice1= rd.choice(dice1) 
    rdice2= rd.choice(dice2) 
    rdices= rdice1+rdice2
    evenNumber= rdices%2==0

    print("Your wallet: ${}".format(wallet))
    bet=int(input("How much do you want to bet?: "))
    print()

    ## betting more than you have ##
    if bet>wallet:
        print("you don't have that much money. Try again")
    else:
        dices=input("Odd or Even? ").upper()
        if dices!="EVEN" and dices!="ODD":
            print("is not a valid answer. Try again")
        else:
            result=""
            if evenNumber is True:
                result="EVEN"
            else:
                result="ODD"
        #################################################################################################

            ## Win / Lose ##
            if dices=="EVEN" and evenNumber is True: #WIN
                win+=1
                wallet-=bet
                print("Result: {} + {} = {} {}".format(rdice1,rdice2,rdices,result))
                print("You WIN!")
                wallet+= bet*2 
                print("Your wallet: ${}".format(wallet))
                print("")
                play=input("Do you want to keep playing? ").upper()
                print("-----------------------------------------------------")
            
            elif dices=="ODD" and evenNumber is False: #WIN
                win+=1
                wallet-=bet 
                print("Result: {} + {} = {} {}".format(rdice1,rdice2,rdices,result))
                print("You WIN!")
                wallet+= bet*2 
                print("Your wallet: ${}".format(wallet))
                print("")
                play=input("Do you want to keep playing? ").upper()
                print("-----------------------------------------------------")
            
            else: #LOSE
                print("Result: {} + {} = {} {}".format(rdice1,rdice2,rdices,result))
                print("You LOSE!")
                wallet-= bet

                if wallet>0: 
                    print("Your wallet: ${}".format(wallet))
                    print()
                    play=input("Do you want to keep playing? ").upper()
                    print("-----------------------------------------------------")
                else:
                    print("Your wallet: ${}".format(wallet))
                    print("your money has flown. You can't afford to keep playing")
                    play="NO"
            ###############################################################################################################

print("")
print("OVERVIEW:")
print("You have won: {} games ".format(win))
print("your wallet has a total of: ${} ".format(wallet))
print()
print("Thank's for playing. We'll glad to see you again")