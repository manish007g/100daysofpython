import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300) 
window.config(padx=20, pady=20)
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1 )

def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text
#Button1
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

#Button2
button1 = tkinter.Button(text="Click Me Again")
button1.grid(column=3, row=1)

input = tkinter.Entry(width=10)
input.grid(column=4, row=3)

window.mainloop()