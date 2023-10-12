# Calculator with Python tkinter
# To do - add ico

# test to make sure git working

from tkinter import *

def print_hi(name):
    # remove this?
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create and configure window for calculator
    calc_gui = Tk()
    calc_gui.configure(background="light blue")
    calc_gui.geometry("400x450+50+50")
    calc_gui.title("CALCULATOR")

    # Create instance of StringVar()
    string_variable = StringVar(calc_gui, "Let's go!!")

   # Create field to show equation
    expression_field = Entry(calc_gui, textvariable=string_variable)

    expression_field.grid(columnspan=100, padx=10, pady = 10)

    # Start up the gui
    calc_gui.mainloop()