import random
from art import logo
def game():
    print(logo)
    cards=[]
    t=int(input("Number of decks dealer has? "))
    if t<=0:
        t=1
    for j in range (2,12):
        cards.extend([j for k in range (0,4*t)]) 
    cards.extend([10 for k in range (0,3*4*t)])  
    player=[]
    dealer=[]    
    print("Shuffling Cards")
    random.shuffle(cards)
    def a (d):
        if sum(d)>21:
            if 11 in d:
                d[d.index(11)]=1
    for k in range (0,2):
        player.append(cards.pop(0))
        dealer.append(cards.pop(0))
    a(player)
    a(dealer) 
    if sum(player)==21:
        print("Player has a Blackjack")
        if sum(dealer)==21:
            print("            ")
            print("Draw")
            return 0
        else:
            print("            ")
            print("Player Wins")   
            return 0
        print(f"Player Cards {*player,}")
        print(f"Dealer Cards {*dealer,}")
    else:    
        print(f"Player Cards {*player,}")       
        print("Dealer Cards "+str(dealer[0])+" _")
    
    K=int(input("Player 1-Hit 2-Stand "))
    while (K==1):    
        player.append(cards.pop(0))
        a(player)
        if sum(player)>21:
            print("            ")
            print(f"Player Cards {*player,}") 
            print(f"Dealer Cards {*dealer,}")
            print("Dealer Wins")
            return 0
        else:
            print(f"Player Cards {*player,}")    
            K=int(input("Player 1-Hit 2-Stand "))
    print(f"Dealer Cards {*dealer,}")
    while(sum(dealer)<17):
        dealer.append(cards.pop(0))
        a(dealer)
        print(f"Dealer Cards {*dealer,}")
    if sum(dealer)>sum(player) and sum(dealer)<=21:
        print("            ")
        print("Dealer Wins")
        print(f"Player Cards {*player,}") 
        print(f"Dealer Cards {*dealer,}")
        return 0
    if sum(dealer)>21:
        print("            ")
        print("Player Wins")
        print(f"Player Cards {*player,}") 
        print(f"Dealer Cards {*dealer,}")
        return 0
 
game()
