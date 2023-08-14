import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.result_var = tk.StringVar()
        self.create_ui()

    def create_ui(self):
        # Entry widget to display the result
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 18))
        result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define calculator buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Function to handle button clicks
        def button_click(event):
            current_result = self.result_var.get()
            button_text = event.widget.cget("text")

            if button_text == "=":
                try:
                    result = eval(current_result)
                    self.result_var.set(result)
                except Exception as e:
                    self.result_var.set("Error")
            elif button_text == "C":
                self.result_var.set("")
            else:
                self.result_var.set(current_result + button_text)

        # Add buttons to the calculator
        row, col = 1, 0
        for button_text in buttons:
            button = tk.Button(self.root, text=button_text, font=("Arial", 18), width=5, height=2)
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

            # Bind button click event
            button.bind("<Button-1>", button_click)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
