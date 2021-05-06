from tkinter import *

root = Tk()
root.geometry("550x350")
root.title("Adding two numbers")
root.configure(bg='red')

label_1 = Label(root, text="Enter first number:")
label_2 = Label(root, text="Enter second number:")
label_3 = Label(root, text="Answer:")
label4 = Label(root)

first_number = Entry (root)
second_number = Entry(root)
total = Entry(root)


# function
def button_clear():
    total.delete(0, END)
    first_number.delete(0, END)
    second_number.delete(0, END)


def button_add():
    dig_1 = first_number.get()
    dig_2 = second_number.get()
    first_addition = int(dig_1)
    second_addition = int(dig_2)
    sum = first_addition + second_addition

    total.insert(0, sum)


def button_exit():
    import sys
    sys.exit()


# Buttons
button_add = Button(root, borderwidth=5,font="consolas 16 bold", text="add", bg="red", fg="white", width=10,
                    command=button_add)
button_clear = Button(root, borderwidth=5,font="consolas 16 bold", text="clear", bg="red", fg="white", width=10,
                      command=button_clear)
button_exit = Button(root, borderwidth=5,font="consolas 16 bold", text="exit", bg="red", fg="white", width=10,
                     command=button_exit)

# Display
label_1.grid(row=0, column=0, padx=10, pady=10)
label_2.grid(row=1, column=0, padx=10, pady=10)
label_3.grid(row=2, column=0, padx=10, pady=10)
first_number.grid(row=0, column=1, padx=10, pady=10)
second_number.grid(row=1, column=1, padx=10, pady=10)
total.grid(row=2, column=1, padx=10, pady=10)
button_add.place(x=20, y=150)
button_clear.place(x=200, y=150)
button_exit.place(x=380, y=150)
root.mainloop()
