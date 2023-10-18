# Calculator with tkinter

from tkinter import *
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(expression.get())
        expression.set(str(result))  # Update expression with the result
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create and configure window for calculator
    calc_gui = Tk()
    calc_gui.configure(background="light blue")
    calc_gui.geometry("400x450+50+50")
    calc_gui.title("CALCULATOR")
    calc_gui.resizable(0,0)

    # Create instance of StringVar()
    string_variable = StringVar(calc_gui, "Let's go!!")

   # Create field to show equation
    expression_field = Entry(calc_gui, textvariable=string_variable)

    expression_field.grid(columnspan=100, padx=10, pady = 10)

    # Start up the gui
    calc_gui.mainloop()