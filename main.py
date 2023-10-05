# Graphical Calculator with Python and tkinter

from tkinter import *

def print_hi(name):
    # remove this?
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create and configure window for calculator
    calc_gui = Tk()
    calc_gui.configure(background="light blue")
    calc_gui.geometry("400x450")
    calc_gui.title("CALCULATOR")

    # Create instance of StringVar()
    string_variable = StringVar(calc_gui, "Let's go!!")

    # Create data entry box
    expression_field = Entry(calc_gui, textvariable=string_variable)

    expression_field.grid(columnspan=4, ipadx=70)

    # Start up the gui
    calc_gui.mainloop()




