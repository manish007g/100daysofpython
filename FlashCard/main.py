from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
flip_timer = None
#----------------------------------------------Show Cards--------------------------------------------------------------#
try:
    data = pandas.read_csv("./data/words_to_known.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/spanish_words.csv")
finally:
    to_learn = data.to_dict("records")


def know_cards():
    global current_card
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_known.csv", index=False)
    show_cards()
def show_cards():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=back_cards)

#----------------------------------------------Show Back---------------------------------------------------------------#


def back_cards():

    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


#----------------------------------------------UI Setup----------------------------------------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=back_cards)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong= PhotoImage(file="./images/wrong.png")


canvas_image = canvas.create_image(400, 250, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
show_cards()

right_button = Button(image=right, highlightthickness=0, command=know_cards)
right_button.grid(row=1, column=1)


wrong_button = Button(image=wrong, highlightthickness=0, command=show_cards)
wrong_button.grid(row=1, column=0)

window.mainloop()