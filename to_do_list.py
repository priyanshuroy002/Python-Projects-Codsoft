import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Task Entry
task_entry = tk.Entry(root, font=("Helvetica", 16))
task_entry.pack(pady=20, padx=10, fill=tk.BOTH)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Remove Task Button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Clear Tasks Button
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(pady=5)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, font=("Helvetica", 14), selectbackground="lightblue", selectmode=tk.SINGLE)
tasks_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()
