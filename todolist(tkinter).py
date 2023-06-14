import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

# Function to mark a task as completed
def complete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(index, fg="gray")
        listbox_tasks.selection_clear(0, tk.END)
    except IndexError:
        pass

# Function to remove a task
def remove_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
        listbox_tasks.selection_clear(0, tk.END)
    except IndexError:
        pass

# Create the main window
window = tk.Tk()
window.title("Todo List Manager")

# Create the task list
listbox_tasks = tk.Listbox(window, height=10, width=50, font=("Arial", 12))
listbox_tasks.pack(pady=10)

# Create a scrollbar
scrollbar_tasks = tk.Scrollbar(window)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Set the scrollbar to the task list
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Create the task entry
entry_task = tk.Entry(window, font=("Arial", 12))
entry_task.pack(pady=5)

# Create the buttons
frame_buttons = tk.Frame(window)
frame_buttons.pack()

button_add = tk.Button(frame_buttons, text="Add Task", font=("Arial", 12), command=add_task)
button_add.pack(side=tk.LEFT)

button_complete = tk.Button(frame_buttons, text="Complete Task", font=("Arial", 12), command=complete_task)
button_complete.pack(side=tk.LEFT)

button_remove = tk.Button(frame_buttons, text="Remove Task", font=("Arial", 12), command=remove_task)
button_remove.pack(side=tk.LEFT)

# Run the main window's event loop
window.mainloop()
