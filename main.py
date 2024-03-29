from tkinter import *

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

deck = {}


def deal_card():
    pass


def check_win():
    pass


# -------------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Blackjack")
window.config(width=696, height=480)

canvas = Canvas(width=696, height=480)
table_img = PhotoImage(file="assets/table_with_chips.png")
canvas.create_image(348, 240, image=table_img)
canvas.pack()

window.mainloop()
