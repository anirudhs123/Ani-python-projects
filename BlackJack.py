#importing the deck
import random

suits = ("Hearts","Diamonds","Clubs","Spades")
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True


#class for card
class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return(self.rank+" of "+ self.suit)
        
        
        
#class of the deck        
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp=""
        for item in self.deck:
            deck_comp+=item.__str__()
        return("The deck contains"+deck_comp)
        

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card=self.deck.pop()
        return(single_card)
  
 #class for hand 
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
   
        
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if(card.rank=='Ace'):
            self.aces+=1
    
    
    def adjust_for_ace(self):
        while(self.value>21 and self.aces>0):
            self.value-=10
            self.aces-=1
      
    
    #class for chips
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet
    
def take_bet(chips):
        while True:
            try:
                bet=int(input("enter your bet amount   "))
                chips.bet=bet
            except TypeError:
                print("please enter a integer value")
            else:
                if(bet>chips.total):
                    print("Funds not available!!Please choose a proper bet amount.You have{}".format(chips.total))
                    
                else:
                    break
 

 #function for hit(input a card)                  
def hit(deck,hand):
    
    single_card=deck.deal()
    #print(single_card)
    hand.add_card(single_card)
    hand.adjust_for_ace()
    
    
    
                      
 #function to ask for draw or stop

def hit_or_stand(d,hand):
    global playing
    
    # to control an upcoming while loop
    ch=input("Do you want to Hit or Stand \n ")
    if(ch.lower()=="hit"):
        hit(d,hand)
        playing=True
        
    elif(ch.lower()=="stand"):
        print("\n")
        print("player stands now dealers turn \n")
        
     

            

 #function to print all player cards  
def show_some(player,dealer):
    print("Dealers hand:")
    print("First card is hidden")
    print(dealer.cards[1])
    print("\n")
    print("Players hand:")
    for i in player.cards:
        print(i)
       
    


 #function to print all dealer  cards 
def show_all(player,dealer):
    print("\n")
    print("dealers hand :")
    for i in dealer.cards:
        print(i)
    print("\n")   
    print("players hand: ")
    for item in player.cards:
        print(item)
    print("\n")
    
 
 #function to check if player busts            
def player_busts(player,dealer,chips):
    if(player.value>21):
        print("game over player burst")
        chips.lose_bet()
        
        

    
#function to check if player wins
def player_wins(player,dealer,chips):
    if(player.value> dealer.value and player.value<=21):
        print('player won')
        print("player value is{}".format(player.value))
        print(f"dealer value is{dealer.value}")
        chips.win_bet()
    
    
#function to check if dealer wins
def dealer_busts(player,dealer,chips):
    if(dealer.value>21):
        print("game over player won as dealer bursts")
        print(f" dealer value is {dealer.value}")
        chips.win_bet()
        
    
  #function to check if dealer wins  
def dealer_wins(player,dealer,chips):
    if(player.value < dealer.value and dealer.value<=21):
        print('player lost as dealer wins')
        print(f"player value{player.value}")
        print(f"dealer value{dealer.value}")
        chips.lose_bet()

    
    #function to check if game ends in a draw
def push(player,dealer):
    if(player.value == dealer.value and dealer.value==21):
        print("game ends in a draw")
def draw(player,dealer):
    if(player.value==dealer.value and dealer.value<21):
        print("draw game")
    
 


global playing
x=input("do you want to continue{y/n}")


while (x=='y'):
    playing=True
    # Print an opening statement
    print('WELCOME TO BLACKJACK GAME')
    
    # Create & shuffle the deck, deal two cards to each player
    d=Deck()
    d.shuffle()
    hand_player=Hand()
    hand_player.add_card(d.deal())
    hand_player.add_card(d.deal())
    hand_dealer=Hand()
    hand_dealer.add_card(d.deal())
    hand_dealer.add_card(d.deal())
    
    
    # Set up the Player's chips
    chip_player=Chips()
    
    
    # Prompt the Player for their bet
    
    
    # Show cards (but keep one dealer card hidden)
    show_some(hand_player,hand_dealer)
    take_bet(chip_player)
    
    def replay():
            
            inp=input("DO YOU WANT TO CONTINUE {y/n}")
            if(inp =="y"):
                return(True)
            
                
            elif(inp=="n"):
               
                return(False)
            
    while (playing==True):  
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(d,hand_player)
        
        # Show cards (but keep one dealer card hidden)
       
        show_some(hand_player,hand_dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if(hand_player.value>21):
            player_busts(hand_player,hand_dealer,chip_player)
            playing=False
        else:
            while (17 > hand_dealer.value ):
                hit(d,hand_dealer)
            
                             
            
            
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        # Show all cards
        print("\n")
        print("chances over now cards will be displayed\n")
        show_all(hand_player,hand_dealer)
        
        # Run different winning scenarios
        player_wins(hand_player,hand_dealer,chip_player)
        #player_busts(hand_player,hand_dealer,chip_player)
        dealer_wins(hand_player,hand_dealer,chip_player)
        dealer_busts(hand_player,hand_dealer,chip_player)
        push(hand_player,hand_dealer)
        draw(hand_player,hand_dealer)
    
    # Inform Player of their chips total 
        print('the toatal amount left:{}'.format(chip_player.total))
    
    # Ask to play again
        
        
        inp=input("DO YOU WANT TO CONTINUE {y/n}")
        if(inp =="y"):
            playing=False
            x="y"
            
                
        elif(inp=="n"):
            playing=False
            x="n"
                   
    
    
            
             
