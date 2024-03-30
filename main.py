from tkinter import *
from random import randint

YELLOW = "#fde371"
GREEN = "#3C6633"
PURPLE = "#633068"
TANGERINE = "#F98948"
BLUE = "#058ED9"
BLUE2 = "#0C6291"

window = Tk()

# TODO: After player accepts another card, trigger a check to see if they go bust
# TODO: Add computer turn functionality, and a way to reset the board
# TODO: Pull files/functions out into another file where possible

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


def start_new_game(p_hand, d_hand):
    """Clears all cards then deals the dealer and player both 2 cards"""
    if len(p_hand) > 0:
        p_hand.clear()
        d_hand.clear()
    deal_card(p_hand)
    deal_card(p_hand)
    deal_card(d_hand)
    deal_card(d_hand)


def deal_card(target_player: list):
    """This function deals a new random card from the deck to the chosen players hand (dealer or player)
    and then calls the function to display them on screen"""
    random_num = randint(2, 14)
    target_player.append(deck[random_num])
    render_hand()


def hit_me():
    """Simply calls deal card but doesn't need an argument so can be passed into the button command"""
    deal_card(player_hand)


def computer_turn():
    pass


def check_state():
    """Checks to see if player total is equal to or over 21,
    and if not who wins between dealer and player"""
    pass


def render_hand():
    """This function removes old card images if there are any, then goes through the
    hands and places the new cards on the GUI, as well as rendering player hand total"""
    # Delete old card images
    canvas.delete("card")

    # Loop through player hand, render the cards, and render hand total
    player_hand_total = 0
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


# -------------------------------- UI SETUP -------------------------------- #

window.title("Blackjack")
window.config(width=696, height=480)

canvas = Canvas(width=696, height=480)

table_img = PhotoImage(file="assets/table_with_chips.png")
hit_button_image = PhotoImage(file="assets/button_hit-me.png")
hold_button_image = PhotoImage(file="assets/button_hold.png")

background = canvas.create_image(348, 240, image=table_img)
hand_total_label = canvas.create_text(565, 300, text="Hand Total: ", fill=YELLOW, font='Arial 16 bold')
hand_total_text = canvas.create_text(635, 300, text="0", fill=YELLOW, font='Arial 16 bold')
hit_me_button = Button(image=hit_button_image, background=GREEN, border=0, command=hit_me)
hold_button = Button(image=hold_button_image, background=GREEN, border=0, command=computer_turn)

canvas.pack()
hit_me_button.place(x=520, y=325)
hold_button.place(x=520, y=375)

start_new_game(player_hand, dealer_hand)

window.mainloop()
