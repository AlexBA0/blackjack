import random

class blackJack():
    def __init__(self):
        self.cardNames = ["One", "Two", "Three", "Four", "Five",
                      "Six", "Seven", "Eight", "Nine", "Ten",
                        "Jack", "Queen", "King", "Ace"]
        self.prettyHand = []

    def beginGame(dealer, player):
        outcome = False
        static = 0
        while outcome == False:
            dealer.dealerTurn()
            player.calculateScore()
            print(f"\n Your score is {player.score}, your hand {player.prettyHand}")
            print(f" The dealer has a score of {dealer.score}, his hand {dealer.prettyHand}")

            if dealer.score >= 22:
                outcome = True
                print("\n You win!")

            elif player.score <= 21:
                if player.score == 21:
                    outcome = True
                    print("\n You win!")

                else:   
                    choice = int(input(f"\n Your current score is {player.score}, would you like to draw another card? (1 or 0): "))

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
        self.prettyHand.append(f"{cardValue} of {suit}")
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

    def ace_handler(self, curr_score, ace_count):
        best_score = curr_score + ace_count
        for i in range(0, ace_count):
            new_score = curr_score + ace_count + 11*ace_count - 1*ace_count
            print(f"\n new score {new_score}, best score {best_score}")
            if new_score <= 21 and (21 - new_score < 21 - best_score):
                print(f"\n new best score {new_score}")
                best_score = new_score
        return best_score

    def calculateScore(self):
        cardValues = dict(zip(self.cardNames, range(0,15)))
        new_score = 0
        ace_count = 0
        for card in self.hand:
            if card in self.cardNames:
                if cardValues[card] >= 11:
                    if card == "Ace":
                        ace_count += 1
                    else:
                        new_score += 10
                else:
                    new_score += cardValues[card] + 1

        if ace_count >= 1: #ace handling left until end of card evaluation loop
            new_score = self.ace_handler(new_score, ace_count)
            self.score = new_score

        self.score = new_score
        
    
class dealer(player):
    def __init__(self, name):
        super().__init__(name)
    
    def dealerTurn(self):
        self.calculateScore()
        if self.score <= 15:
            self.takeTurn()
        else:
            print("\n The dealer holds")
        self.calculateScore()