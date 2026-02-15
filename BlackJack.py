import random

class blackJack():
    def __init__(self):
        self.cardNames = ["One", "Two", "Three", "Four", "Five",
                      "Six", "Seven", "Eight", "Nine", "Ten",
                        "Jack", "Queen", "King", "Ace"]

    def beginGame(dealer, player):
        outcome = False
        static = 0
        while outcome == False:
            dealer.dealerTurn()
            player.calculateScore()
            print(f"\n Your score is {player.score}, your hand {player.hand}")
            print(f" The dealer has a score of {dealer.score}, his hand {dealer.hand}")

            if dealer.score >= 22:
                outcome = True
                print("\n You win!")

            elif player.score <= 21:
                choice = int(input(f"Your current hand is {player.hand} would you like to draw another? (1 or 0): "))
                if choice == 1:
                    player.takeTurn()
                    player.calculateScore()
                else: 
                    static += 1
                    if int(static) >= 2:
                        outcome = True
                        if 21 % dealer.score >= 21 % player.score:
                            print("\n You win!")
                        else:
                            print("\n You lose!")
                
            elif player.score >= 22:
                outcome = True
                print("\n You lose!")
        
    def drawCard(self):
        randomNumber = random.random()
        suit = self._pickSuit(randomNumber)
        cardValue = self._pickCardValue()
        return (cardValue, suit)
    
    def _pickSuit(self, randomNumber):
        if randomNumber >= 0.75:
            suit = "clubs"
        elif randomNumber >= 0.5:
            suit = "spades"
        elif randomNumber >= 0.25:
            suit = "hearts"
        else:
            suit = "diamonds"
        return suit
    
    def _pickCardValue(self):
        #cards can be one of 14 cards with equal prob
        return self.cardNames[random.randrange(1,14)]
    
class player(blackJack):
    def __init__(self, name):
        super().__init__()
        self.hand = self.drawCard()
        self.name = name
        self.score = 0
        self.calculateScore()
        
    def takeTurn(self):
        self.hand += (self.drawCard())
                 
    def calculateScore(self):
        new_score = 0
        cardValues = dict(zip(self.cardNames, range(0,15)))
        for card in self.hand:
            if card in self.cardNames:
                if cardValues[card] >= 11:
                    if card == "Ace":
                        if self.score >= 22:
                            new_score += 1
                        else:
                            new_score += 11
                    else:
                        new_score += 10
                else:
                    new_score += cardValues[card] + 1
        self.score = new_score
        
    
class dealer(player):
    def __init__(self, name):
        super().__init__(name)
        self.hand = self.drawCard()
        self.score = 0
        self.calculateScore()
    
    def dealerTurn(self):
        self.calculateScore()
        if self.score <= 15:
            self.takeTurn()
        else:
            print("The dealer holds")
        self.calculateScore()