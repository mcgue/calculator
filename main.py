# Calculator with tkinter

from tkinter import *
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(expression_field.get())
        expression_field.set(str(result))  # Update expression with the result
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")

# Function to update the expression when a button is clicked
def update_expression(value):
    current_expression = expression_field.get()
    expression_field.set(current_expression + str(value))

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

    # Buttons for digits and operators
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
    ]

    for (text, row, column) in buttons:
        if text == '=':
            button = Button(calc_gui, text=text, font=("Arial", 24), bd=10, command=evaluate_expression)
        else:
            button = Button(calc_gui, text=text, font=("Arial", 24), bd=10, command=lambda t=text: update_expression(t))
        button.grid(row=row, column=column, sticky='nsew')

    # Configure row and column weights to make the buttons expand
    for i in range(5):
        calc_gui.grid_rowconfigure(i, weight=1)
        calc_gui.grid_columnconfigure(i, weight=1)

    # Start up the gui
    calc_gui.mainloop()