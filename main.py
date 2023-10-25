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

# Function to update the expression when a button is clicked
def update_expression(value):
    current_expression = expression.get()
    expression.set(current_expression + str(value))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create and configure window for calculator
    calc_gui = Tk()
    calc_gui.configure(background="light blue")
    calc_gui.geometry("400x450+50+50")
    calc_gui.title("CALCULATOR")
    calc_gui.resizable(0,0)

    # Instance of StringVar() for entry field
    string_variable = StringVar()

   # Entry field
    expression_field = Entry(calc_gui, textvariable=string_variable,
        font=("open sans", 24), bd=5, insertwidth=1, width=15)

    expression_field.grid(row=0, column=0, columnspan=3, padx = 10, pady = 10)

    # Start up the gui
    calc_gui.mainloop()