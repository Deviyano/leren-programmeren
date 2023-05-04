import random

# Define card colors and values
colors = ["red", "yellow", "green", "blue","brown"]
values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"]

# Define a function to create a deck of Uno cards
def create_deck():
    deck = []
    for color in colors:
        for value in values:
            card_value = color + " " + value
            deck.append(card_value)
            if value != "0":
                deck.append(card_value)
    return deck

# Define a function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Define a function to deal cards to players
def deal_cards(deck, num_players):
    hands = []
    for i in range(num_players):
        hand = []
        for j in range(7):
            card = deck.pop(0)
            hand.append(card)
        hands.append(hand)
    return hands

# Define a function to check if a card can be played
def can_play(card, prev_card):
    split_card = card.split(" ")
    if len(split_card) != 2:
        return False
    card_color, card_value = split_card
    prev_color, prev_value = prev_card.split(" ")
    if card_color == prev_color or card_value == prev_value:
        return True
    elif card_value == "Wild" or card_value == "Wild Draw Four":
        return True
    else:
        return False

# Define a function to play a turn
def play_turn(player, hand, prev_card, deck):
    print("Player", player, "turn")
    print("Previous card:", prev_card)
    print("Your hand:", hand)
    playable_cards = [card for card in hand if can_play(card, prev_card)]
    if len(playable_cards) > 0:
        print("Playable cards:", playable_cards)
        chosen_card = input("Choose a card to play: ")
        while chosen_card not in playable_cards:
            chosen_card = input("Invalid card. Choose a card to play: ")
        hand.remove(chosen_card)
        return chosen_card
    else:
        print("No playable cards. Drawing a card.")
        card = deck.pop(0)
        print("Drawn card:", card)
        if can_play(card, prev_card):
            hand.append(card)
            return card
        else:
            return None

# Define a function to play the game
def play_game(num_players):
    deck = create_deck()
    shuffle_deck(deck)
    hands = deal_cards(deck, num_players)
    prev_card = deck.pop(0)
    while prev_card.split(" ")[1] in ["Skip", "Reverse", "Draw", "Wild"]:
        deck.append(prev_card)
        shuffle_deck(deck)
        prev_card = deck.pop(0)
    print("Starting card:", prev_card)
    current_player = 0
    while True:
        hand = hands[current_player]
        card = play_turn(current_player, hand, prev_card, deck)
        if card is not None:
            prev_card = card
            if len(hand) == 0:
                print("Player", current_player, "wins!")
                break
        current_player = (current_player + 1) % num_players

# Play the game with 2 players
play_game(2)