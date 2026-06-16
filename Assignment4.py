"""
GUI CALCULATOR WITH FUNCTIONS
Uses tkinter for graphical interface and functions for all operations.
"""

import tkinter as tk
from tkinter import messagebox
import math

# ============================================================
# CALCULATOR FUNCTIONS
# ============================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot take sqrt of negative!"
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: Factorial not for negative!"
    if a == 0:
        return 1
    result = 1
    for i in range(1, int(a) + 1):
        result *= i
    return result

# ============================================================
# GUI APPLICATION CLASS
# ============================================================

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

        # Variables
        self.current_input = ""
        self.first_number = None
        self.operation = None
        self.new_input = True

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#34495e", height=100)
        display_frame.pack(fill="both", padx=10, pady=10)

        # Display label
        self.display = tk.Label(
            display_frame,
            text="0",
            font=("Arial", 28, "bold"),
            bg="#34495e",
            fg="white",
            anchor="e",
            padx=10
        )
        self.display.pack(fill="both", expand=True)

        # History label (small)
        self.history_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 10),
            bg="#2c3e50",
            fg="#95a5a6",
            anchor="e",
            padx=10
        )
        self.history_label.pack(fill="x")

        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#2c3e50")
        buttons_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Button layout
        buttons = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "√"],
            ["1", "2", "3", "-", "!"],
            ["0", ".", "=", "+", "x²"],
            ["Mod", "Pow", "Clear", "Exit", ""]
        ]

        for row_idx, row in enumerate(buttons):
            row_frame = tk.Frame(buttons_frame, bg="#2c3e50")
            row_frame.pack(fill="both", expand=True, pady=2)
            for col_idx, text in enumerate(row):
                if text == "":
                    continue
                btn = tk.Button(
                    row_frame,
                    text=text,
                    font=("Arial", 14, "bold"),
                    bg=self.get_button_color(text),
                    fg="white",
                    relief="flat",
                    cursor="hand2",
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.pack(side="left", fill="both", expand=True, padx=2)

    def get_button_color(self, text):
        """Return color based on button type."""
        if text in ["=", "C", "Clear", "Exit"]:
            return "#e67e22"  # Orange
        elif text in ["+", "-", "*", "/", "√", "!", "x²", "Mod", "Pow"]:
            return "#3498db"  # Blue
        elif text == "Exit":
            return "#e74c3c"  # Red
        else:
            return "#2c3e50"  # Dark

    def on_button_click(self, value):
        """Handle all button clicks."""
        if value == "Exit":
            if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
                self.root.quit()
            return

        if value == "C" or value == "Clear":
            self.clear()
            return

        if value in ["+", "-", "*", "/", "Mod", "Pow"]:
            self.set_operation(value)
            return

        if value in ["√", "!", "x²"]:
            self.unary_operation(value)
            return

        if value == "=":
            self.calculate()
            return

        if value == ".":
            if "." not in self.current_input:
                self.current_input += "."
                self.update_display()
            return

        # Number input
        if self.new_input:
            self.current_input = ""
            self.new_input = False

        # Limit input length
        if len(self.current_input) < 15:
            self.current_input += value
            self.update_display()

    def set_operation(self, op):
        """Set the operation for binary calculations."""
        if self.current_input == "" and self.first_number is None:
            return

        if self.first_number is None:
            try:
                self.first_number = float(self.current_input)
                self.operation = op
                self.history_label.config(text=f"{self.first_number} {op}")
                self.new_input = True
            except ValueError:
                self.display.config(text="Error")

    def unary_operation(self, op):
        """Perform unary operations (sqrt, factorial, square)."""
        try:
            num = float(self.current_input)
            result = None

            if op == "√":
                result = square_root(num)
            elif op == "!":
                result = factorial(num)
            elif op == "x²":
                result = num ** 2

            if isinstance(result, str):
                self.display.config(text=result)
            else:
                self.display.config(text=str(result))
                self.current_input = str(result)
                self.new_input = True
                self.history_label.config(text=f"{op}({num}) = {result}")
        except ValueError:
            self.display.config(text="Error")

    def calculate(self):
        """Perform the calculation."""
        if self.first_number is None or self.operation is None:
            return

        try:
            second_num = float(self.current_input)
            result = None

            if self.operation == "+":
                result = add(self.first_number, second_num)
            elif self.operation == "-":
                result = subtract(self.first_number, second_num)
            elif self.operation == "*":
                result = multiply(self.first_number, second_num)
            elif self.operation == "/":
                result = divide(self.first_number, second_num)
            elif self.operation == "Mod":
                result = modulus(self.first_number, second_num)
            elif self.operation == "Pow":
                result = power(self.first_number, second_num)

            if isinstance(result, str):
                self.display.config(text=result)
                self.history_label.config(text=result)
            else:
                display_text = str(result)
                if display_text.endswith(".0"):
                    display_text = display_text[:-2]
                self.display.config(text=display_text)
                self.history_label.config(
                    text=f"{self.first_number} {self.operation} {second_num} = {display_text}"
                )
                self.current_input = str(result)

            self.first_number = None
            self.operation = None
            self.new_input = True

        except ValueError:
            self.display.config(text="Error")
            self.clear()

    def clear(self):
        """Clear all inputs."""
        self.current_input = ""
        self.first_number = None
        self.operation = None
        self.new_input = True
        self.display.config(text="0")
        self.history_label.config(text="")

    def update_display(self):
        """Update the display label."""
        if self.current_input == "":
            self.display.config(text="0")
        else:
            self.display.config(text=self.current_input)

# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()