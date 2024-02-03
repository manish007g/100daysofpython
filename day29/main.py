from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def pass_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = []

    password_list = pass_letters + pass_symbols + pass_numbers
    shuffle(password_list)

    password = "".join(password_list)


    # print(password)

    pass_text.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_func():
    if len(web_text.get()) < 1 or len(pass_text.get()) < 1 or len(mail_text.get()) < 1:
        messagebox.showinfo(title="Oops", message="Please dont leave any textbox empty")
    else:
        is_ok = messagebox.askokcancel(title=web_text.get(), message=f" These are the details entered : \nEmail: {mail_text.get()} "
                                                         f"\nPassword: {pass_text.get()} \nIs it OK to save?")

        if is_ok:
            with open("data.txt", mode='a') as data:
                data.write(f"{web_text.get()} | {mail_text.get()} | {pass_text.get()}\n")
                web_text.delete(0, END)
                pass_text.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_text = Entry(width=62)
web_text.grid(column=1, row=1, columnspan=2)
web_text.focus()

mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)

mail_text = Entry(width=62)
mail_text.grid(column=1, row=2, columnspan=2)
mail_text.insert(0, "manish2@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_text = Entry(width=44)
pass_text.grid(column=1, row=3)

gen_button = Button(text="Generate Password", command=pass_gen)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=53, command=add_func)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
