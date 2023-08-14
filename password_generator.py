import random
import string
import tkinter as tk

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Error: At least one character set must be selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_click():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Label for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

# Entry for password length
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for character sets
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

uppercase_var.set(True)
lowercase_var.set(True)
digits_var.set(True)
special_chars_var.set(True)

uppercase_cb = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
lowercase_cb = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
digits_cb = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
special_chars_cb = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)

uppercase_cb.pack(anchor=tk.W)
lowercase_cb.pack(anchor=tk.W)
digits_cb.pack(anchor=tk.W)
special_chars_cb.pack(anchor=tk.W)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=on_generate_click)
generate_button.pack(pady=20)

# Label to display generated password
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
