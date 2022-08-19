import tkinter

windows = tkinter.Tk()
windows.title("Calculator")
input_num = tkinter.Entry(width=40, borderwidth=5, font=("Arial", 12), bg="black", fg="white")
input_num.grid(row=0, column=0, columnspan=4, padx=10, pady=10, )
windows.config(bg="black")


def first_num(number):
    current = input_num.get()
    input_num.delete(0, tkinter.END)
    input_num.insert(0, str(current) + str(number))


def clear_all():
    input_num.delete(0, tkinter.END)


def subtraction():
    f_num = input_num.get()
    global first_number
    global sign
    sign = "subtract"
    first_number = int(f_num)
    input_num.delete(0, tkinter.END)


def multiplication():
    f_num = input_num.get()
    global first_number
    global sign
    sign = "multiply"
    first_number = int(f_num)
    input_num.delete(0, tkinter.END)


def division():
    f_num = input_num.get()
    global first_number
    global sign
    sign = "divide"
    first_number = int(f_num)
    input_num.delete(0, tkinter.END)


def addition():
    f_num = input_num.get()
    global first_number
    global sign
    sign = "add"
    first_number = int(f_num)
    input_num.delete(0, tkinter.END)


def equal():
    second_num = input_num.get()
    input_num.delete(0, tkinter.END)
    if sign == "add":
        input_num.insert(0, int(second_num) + first_number)
    elif sign == "subtract":
        input_num.insert(0, first_number - int(second_num))
    elif sign == "multiply":
        input_num.insert(0, first_number * int(second_num))
    elif sign == "divide":
        input_num.insert(0, first_number / int(second_num))


# create the button
button1 = tkinter.Button(text="1", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(1))
button2 = tkinter.Button(text="2", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(2))
button3 = tkinter.Button(text="3", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(3))
button4 = tkinter.Button(text="4", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(4))
button5 = tkinter.Button(text="5", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(5))
button6 = tkinter.Button(text="6", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(6))
button7 = tkinter.Button(text="7", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(7))
button8 = tkinter.Button(text="8", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(8))
button9 = tkinter.Button(text="9", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(9))
button0 = tkinter.Button(text="0", padx=40, pady=20, bg="#1d1c1c", fg="white", command=lambda: first_num(0))
clear = tkinter.Button(text="clear", padx=30, pady=20, bg="#1d1c1c", fg="white", command=clear_all)
button_add = tkinter.Button(text="+", padx=39, pady=20, bg="orange", command=addition)
button_divide = tkinter.Button(text="/", padx=40, pady=20, bg="orange", command=division)
button_multiply = tkinter.Button(text="*", padx=40, pady=20, bg="orange", command=multiplication)
button_subtract = tkinter.Button(text="-", padx=40, pady=20, bg="orange", command=subtraction)

equal_to = tkinter.Button(text="=", padx=39, pady=20, bg="royal blue", command=equal)

# place the buttons
button9.grid(row=1, column=0)
button8.grid(row=1, column=1)
button7.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button6.grid(row=2, column=0)
button5.grid(row=2, column=1)
button4.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button3.grid(row=3, column=0)
button2.grid(row=3, column=1)
button1.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button0.grid(row=4, column=0)
clear.grid(row=4, column=1)
button_add.grid(row=4, column=3)
equal_to.grid(row=4, column=2)



































windows.mainloop()