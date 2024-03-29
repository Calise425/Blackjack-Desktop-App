from tkinter import *
from random import randint

window = Tk()

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


def deal_card(target_player: list):
    """This function deals a new random card from the deck to the chosen players hand (dealer or player)"""
    random_num = randint(2, 14)
    target_player.append(deck[random_num])


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

print(player_hand, dealer_hand)
deal_card(player_hand)

print(player_hand)


def check_win():
    pass


def render_cards():
    pass


# -------------------------------- UI SETUP -------------------------------- #

window.title("Blackjack")
window.config(width=696, height=480)

canvas = Canvas(width=696, height=480)
table_img = PhotoImage(file="assets/table_with_chips.png")
canvas.create_image(348, 240, image=table_img)
canvas.pack()

window.mainloop()
