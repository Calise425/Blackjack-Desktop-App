from tkinter import *
from random import randint

YELLOW = "#fde371"
GREEN = "#3C6633"
PURPLE = "#633068"
TANGERINE = "#F98948"
BLUE = "#058ED9"
BLUE2 = "#0C6291"

window = Tk()


# -------------------------------- VARIABLE SETUP -------------------------------- #
# PhotoImage constants of all the card images
card_back = PhotoImage(file="assets/card back.png")
card_2 = PhotoImage(file="assets/2.png")
card_3 = PhotoImage(file="assets/3.png")
card_4 = PhotoImage(file="assets/4.png")
card_5 = PhotoImage(file="assets/5.png")
card_6 = PhotoImage(file="assets/6.png")
card_7 = PhotoImage(file="assets/7.png")
card_8 = PhotoImage(file="assets/8.png")
card_9 = PhotoImage(file="assets/9.png")
card_10 = PhotoImage(file="assets/10.png")
card_jack = PhotoImage(file="assets/jack.png")
card_queen = PhotoImage(file="assets/queen.png")
card_king = PhotoImage(file="assets/king.png")
card_ace = PhotoImage(file="assets/ace.png")

# I assigned a number from 2-14 to these cards to then pick a 'random' card using randint(2,14)
# The value is saved for the calculating of total hand value, and the card will be used to render in the GUI
deck = {
    2: {"value": 2, "image": card_2},
    3: {"value": 3, "image": card_3},
    4: {"value": 4, "image": card_4},
    5: {"value": 5, "image": card_5},
    6: {"value": 6, "image": card_6},
    7: {"value": 7, "image": card_7},
    8: {"value": 8, "image": card_8},
    9: {"value": 9, "image": card_9},
    10: {"value": 10, "image": card_10},
    11: {"value": 10, "image": card_jack},
    12: {"value": 10, "image": card_queen},
    13: {"value": 10, "image": card_king},
    14: {"value": 11, "image": card_ace},
}

player_hand = []
dealer_hand = []


# -------------------------------- GAMEPLAY FUNCTIONS -------------------------------- #
def start_new_game(p_hand, d_hand):
    """Clears both hands then deals the dealer and player each 2 cards"""
    play_again_button.place(x=1000, y=1000)
    canvas.itemconfig(game_state_label, text="")
    p_hand.clear()
    d_hand.clear()
    deal_card(p_hand)
    deal_card(p_hand)
    deal_card(d_hand)
    deal_card(d_hand)
    check_blackjack()


def play_again():
    start_new_game(player_hand, dealer_hand)


def deal_card(target_player: list):
    """Deals a new random card from the deck to the chosen players hand (dealer or player)
    and then calls the function to display them on screen"""
    random_num = randint(2, 14)
    target_player.append(deck[random_num])
    render_table()


def hit_me():
    """Wrapper function to call deal_card as a button command"""
    deal_card(player_hand)
    check_bust()


def dealer_turn():
    dealer_total = 0
    dealer_has_ace = False
    for card in dealer_hand:
        dealer_total += card["value"]
        if card["value"] == 11:
            dealer_has_ace = True
    if dealer_total > 21:
        if dealer_has_ace:
            # Reduce the ace value to 1 if busting
            dealer_total -= 10
            if dealer_total < 17:
                dealer_turn()
            else:
                check_winner()
        else:
            check_winner()
    elif dealer_total < 17:
        deal_card(dealer_hand)
        dealer_turn()
    else:
        check_winner()


def check_bust():
    player_total = 0
    has_ace = False
    for card in player_hand:
        player_total += card["value"]
        if card["value"] == 11:
            has_ace = True

    if player_total > 21:
        if has_ace:
            if player_total > 31:
                canvas.itemconfig(game_state_label, text="Player Bust! Dealer wins.")
                game_end(True)
        else:
            canvas.itemconfig(game_state_label, text="Player Bust! Dealer wins.")
            game_end(True)


def check_blackjack():
    player_total = 0
    for card in player_hand:
        player_total += card["value"]
    if player_total == 21:
        canvas.itemconfig(game_state_label, text="BLACKJACK!")
        game_end(True)


def check_winner():
    """Checks for a winner after the dealer turn,
    provided the dealer and player are not bust"""
    dealer_total = 0
    player_total = 0
    dealer_has_ace = False
    player_has_ace = False

    # Make the dealer cards visible
    dealer_x = 450
    dealer_y = 30
    for card in dealer_hand:
        card_id = canvas.create_image(dealer_x, dealer_y, image=card["image"])
        dealer_x -= 30
        canvas.itemconfig(card_id, tags="card")

    # Check if dealer or player has an ace
    for card in dealer_hand:
        dealer_total += card["value"]
        if card["value"] == 11:
            dealer_has_ace = True

    for card in player_hand:
        player_total += card["value"]
        if card["value"] == 11:
            player_has_ace = True

    # Adjust total if necessary
    if dealer_total > 21 and dealer_has_ace:
        dealer_total -= 10

    if player_total > 21 and player_has_ace:
        player_total -= 10

    # Compare totals
    if player_total > 21:
        canvas.itemconfig(game_state_label, text="Player Bust! Dealer wins.")
        game_end(True)
    elif dealer_total > 21:
        canvas.itemconfig(game_state_label, text="Dealer Bust! You win!")
        game_end(True)
    elif player_total > dealer_total:
        canvas.itemconfig(game_state_label, text="You win!")
        game_end(True)
    elif player_total < dealer_total:
        canvas.itemconfig(game_state_label, text="Dealer wins.")
        game_end(True)
    else:
        canvas.itemconfig(game_state_label, text="It's a tie!")
        game_end(True)


def render_table():
    """This function removes old card images if there are any, then goes through the
    hands and places the new cards on the GUI, as well as rendering player hand total"""
    # Delete old card images
    canvas.delete("card")

    # Loop through player hand, render the cards, and render hand total
    player_hand_total = 0
    player_has_ace = False
    player_x = 350
    player_y = 350
    for card in player_hand:
        card_id = canvas.create_image(player_x, player_y, image=card["image"])
        # Offsets the next card to be placed
        player_x += 25
        player_y += 18
        player_hand_total += int(card["value"])
        # Tag the card item with "card"
        canvas.itemconfig(card_id, tags="card")
        if card["value"] == 11:
            player_has_ace = True

    # Checks if ace should have a value of 1 or 11 depending on score
    if player_hand_total > 21:
        if player_has_ace:
            player_hand_total -= 10

    canvas.itemconfig(hand_total_text, text=f"{player_hand_total}")

    # Same for the dealer
    dealer_x = 450
    dealer_y = 30
    for index, card in enumerate(dealer_hand):
        # First card is face down
        if index == 0:
            card_id = canvas.create_image(dealer_x, dealer_y, image=card_back)
            dealer_x -= 30
        else:
            card_id = canvas.create_image(dealer_x, dealer_y, image=card["image"])
            dealer_x -= 30
        # Tag the card item with "card"
        canvas.itemconfig(card_id, tags="card")


def game_end(game_over):
    if game_over:
        play_again_button.place(x=270, y=160)


# ----------------------------------- UI SETUP ----------------------------------- #
window.title("Blackjack")
window.config(width=696, height=480)

canvas = Canvas(width=696, height=480)

table_img = PhotoImage(file="assets/table_with_chips.png")
hit_button_image = PhotoImage(file="assets/button_hit-me.png")
hold_button_image = PhotoImage(file="assets/button_hold.png")
play_again_img = PhotoImage(file="assets/button_play-again.png")

background = canvas.create_image(348, 240, image=table_img)
game_state_label = canvas.create_text(348, 240, text="", fill=YELLOW, font='Arial 36 bold')
hand_total_label = canvas.create_text(565, 300, text="Hand Total: ", fill=YELLOW, font='Arial 16 bold')
hand_total_text = canvas.create_text(635, 300, text="0", fill=YELLOW, font='Arial 16 bold')
hit_me_button = Button(image=hit_button_image, background=GREEN, border=0, command=hit_me)
hold_button = Button(image=hold_button_image, background=GREEN, border=0, command=dealer_turn)
play_again_button = Button(image=play_again_img, background=GREEN, border=0, command=play_again)

canvas.pack()
hit_me_button.place(x=520, y=325)
hold_button.place(x=520, y=375)
play_again_button.place(x=1000, y=1000)


# -------------------------------- START THE GAME! -------------------------------- #
start_new_game(player_hand, dealer_hand)

window.mainloop()
