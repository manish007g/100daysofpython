import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer
    window.after_cancel(timer)
    work_label.config(text="TIMER", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    timer = None
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0:
        work_label.config(text="BREAK", fg=RED)
        count_down(LONG_BREAK_MIN)

    elif reps % 2 == 0:
        work_label.config(text="BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN)

    else:
        work_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN)

# count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    minu = math.floor(count / 60)
    sec = count % 60
    if minu < 10:
        minu = f"0{minu}"
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{minu}:{sec}")
    if count > -1:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmark = ""
        for _ in range(math.floor(reps/2)):
            checkmark += "✅"
        check_label.config(text=checkmark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file= r"C:\Users\91809\PycharmProjects\Day28\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

work_label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
work_label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

check_label= Label(text="", fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=4)


window.mainloop()