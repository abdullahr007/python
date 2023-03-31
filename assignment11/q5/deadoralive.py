# JTMS-14
# a11 p5.py
# Abdullah Rafique
# arafique@jacobs-university.de
from cards import Deck, Card


class Player(object):

    def __init__(self, cards):
        self._cards = cards
        self._wins = 0
        self._losses = 0

    def __str__(self):
        result = ", ".join(map(str, self._cards))
        return result

    def increment_win(self):  # used as a setter
        self._wins += 1

    def increment_loss(self):  # used as a setter
        self._losses += 1

    def get_win(self):  # getter
        return self._wins

    def get_loss(self):  # getter
        return self._losses

    @property  # property to be accessed in the game function
    def get_card_power(self):
        # idea is to set the value/ power of card as floats,
        # such that in general ranks have 'higher priority'
        # whereas the colors contribute only with 0.{something}
        power_of_card = 0
        for card in self._cards:
            if card.rank == 1:
                power_of_card = 14  # ace the strongest
            else:  # the other ranks match
                power_of_card = card.rank
            if card.suit == 'Spades':
                power_of_card += 0.2
            elif card.suit == 'Hearts':
                power_of_card += 0.4
            elif card.suit == 'Diamonds':
                power_of_card += 0.6
            else:  # Spades
                power_of_card += 0.8
        return power_of_card

    def draw_card(self, deck):
        # as far as I know the game rules
        # each time only one card is being compared
        self._cards.pop()  # remove previous
        # it is mot explicitly specified in the task, if we are
        # about to compare multiple cards at a time, therefore
        # I assume, we should care only about one and 'discard'
        # the others
        self._cards.append(deck.deal())  # take a new card from the deck


class Dealer(Player):  # has nothing special
    pass  # same as the player class


class DeadOrAlive(object):

    def __init__(self):  # similar to the blackjack
        self._deck = Deck()
        self._deck.shuffle()
        # we only draw/ have one card initially
        self._player = Player([self._deck.deal()])
        self._dealer = Dealer([self._deck.deal()])

    def play(self):
        round = 1  # for convenience count the rounds
        # I need this part to read the very first values
        print("\nROUND:", round)
        # show intermediate steps
        print("You:\n", self._player)
        print("Dealer:\n", self._dealer)
        if self._player.get_card_power > self._dealer.get_card_power:
            print("You won now! :)")
            self._player.increment_win()
            self._dealer.increment_loss()
        else:  # self explanatory
            print("Dealer won now! :(")
            self._dealer.increment_win()
            self._player.increment_loss()

        while self._deck:
            # repeat the same strategy for the whole deck
            round += 1
            self._player.draw_card(self._deck)
            self._dealer.draw_card(self._deck)
            print("\nROUND:", round)
            print("You:\n", self._player)
            print("Dealer:\n", self._dealer)
            if self._player.get_card_power > self._dealer.get_card_power:
                print("You won now! :)")
                self._player.increment_win()
                self._dealer.increment_loss()
            else:
                print("Dealer won now! :(")
                self._dealer.increment_win()
                self._player.increment_loss()

        # show the final 'statistical' information
        print("\n\nYou have", self._player.get_win(), "wins")
        print("You have", self._player.get_loss(), "losses")
        print("Dealer has", self._dealer.get_win(), "wins")
        print("Dealer has", self._dealer.get_loss(), "losses\n")

        # determine the global winner
        if self._player.get_win() > self._dealer.get_win():
            print("You are the BIG winner")
        elif self._player.get_win() < self._dealer.get_win():
            print("The dealer is the BIG winner")
        else:  # == (13 and 13 wins)
            print("Draw!")


def main():  # similar to the black jack main
    game = DeadOrAlive()
    game.play()


main()
