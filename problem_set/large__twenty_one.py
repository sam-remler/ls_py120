import random

class Card:
    VALUES = {str(num): num for num in range(2, 11)}
    VALUES.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    @property
    def value(self):
        return self.VALUES[self.number]


class Deck:
    def __init__(self):
        self.cards = [Card(num) for num in Card.VALUES.keys()] * 4
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None  # Prevent drawing from empty deck


class Player:
    def __init__(self, deck):
        self.deck = deck
        self.cards = [deck.draw(), deck.draw()]
        self.stop = False

    def hit(self):
        if not self.stop:
            self.cards.append(self.deck.draw())

    def stay(self):
        self.stop = True

    def card_value(self):
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.number == 'A')

        # Adjust Aces from 11 to 1 if needed
        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def is_bust(self):
        return self.card_value() > 21

    def display(self, hide_first_card=False):
        if hide_first_card:
            print(f"Dealer shows: {self.cards[1]}")
        else:
            print(" ".join(str(card) for card in self.cards))
            


class TwentyOneGame:
    def welcome_message(self):
        print("\nWelcome to Twenty One!\n")

    def exit_message(self):
        print("\nThanks for playing!\n")

    def play(self):
        while True:
            deck = Deck()
            player = Player(deck)
            dealer = Player(deck)

            self.welcome_message()

            # Show player's cards
            print("\nYour cards:")
            player.display()

            # Show dealer's first card only
            dealer.display(hide_first_card=True)

            while not player.stop and not player.is_bust():
                hit = input("\nWould you like to hit? (y/n): ").strip().lower()
                if hit == 'y':
                    player.hit()
                    print("\nYour cards:")
                    player.display()
                elif hit == 'n':
                    player.stay()
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

            if player.is_bust():
                print("\nYou busted! Dealer wins.")
            else:
                while dealer.card_value() < 17:
                    dealer.hit()

                print("\nDealer's hand:")
                dealer.display()

                if dealer.is_bust():
                    print("Dealer busts! You win!")
                elif dealer.card_value() > player.card_value():
                    print("Dealer wins!")
                elif player.card_value() > dealer.card_value():
                    print("You win!")
                else:
                    print("It's a tie!")

            print(f"\nFinal Scores - Dealer: {dealer.card_value()}, You: {player.card_value()}")

            replay = input("\nWould you like to play again? (y/n): ").strip().lower()
            if replay != 'y':
                self.exit_message()
                break


# Run the game
game = TwentyOneGame()
game.play()