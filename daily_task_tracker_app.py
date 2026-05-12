# Daily Task Tracker App
# Sources used:
# 1. Python Tkinter documentation: https://docs.python.org/3/library/tkinter.html
# 2. GeeksforGeeks Tkinter tutorial: https://www.geeksforgeeks.org/python-tkinter-tutorial/
# 3. YouTube Tkinter examples: https://www.youtube.com/results?search_query=tkinter+task+list+python

import tkinter as tk  # Line 1 - Borrowed idea/source support: imports tkinter so the app can create a GUI window.
from tkinter import messagebox  # Line 2 - Borrowed idea/source support: imports messagebox for popup alerts.

def add_task():  # Line 3 - My code: function that adds a new task into the listbox.
    task = entry.get().strip()  # Line 4 - My code: gets the typed text from the entry box and removes extra spaces.
    if task == "":  # Line 5 - My code: checks if the user left the box empty.
        messagebox.showwarning("Empty Task", "Please type a task first.")  # Line 6 - My code: shows a warning if nothing was typed.
    else:  # Line 7 - My code: runs when the task box is not empty.
        task_list.insert(tk.END, task)  # Line 8 - Borrowed structure, my use: adds the task to the listbox at the end.
        entry.delete(0, tk.END)  # Line 9 - Borrowed structure, my use: clears the entry box after adding the task.
        update_count()  # Line 10 - My code: updates the task counter label after a new task is added.

def delete_task():  # Line 11 - My code: function that deletes the selected task from the listbox.
    selected = task_list.curselection()  # Line 12 - Borrowed structure, my use: finds which task is selected.
    if selected:  # Line 13 - My code: checks that the user selected a task.
        task_list.delete(selected[0])  # Line 14 - Borrowed structure, my use: removes the selected task from the listbox.
        update_count()  # Line 15 - My code: updates the task counter after deleting a task.
    else:  # Line 16 - My code: runs if no task is selected.
        messagebox.showinfo("Select Task", "Please select a task to delete.")  # Line 17 - My code: tells the user to select a task first.

def clear_tasks():  # Line 18 - My code: function that removes all tasks from the listbox.
    if task_list.size() > 0:  # Line 19 - My code: checks whether the listbox has any tasks in it.
        answer = messagebox.askyesno("Clear All", "Do you want to remove all tasks?")  # Line 20 - My code: asks for confirmation before clearing.
        if answer:  # Line 21 - My code: continues only if the user clicks Yes.
            task_list.delete(0, tk.END)  # Line 22 - Borrowed structure, my use: deletes every task from the first to the last item.
            update_count()  # Line 23 - My code: updates the task counter after clearing everything.

def update_count():  # Line 24 - My code: function that shows how many tasks are currently in the list.
    count_label.config(text=f"Total Tasks: {task_list.size()}")  # Line 25 - My code: changes label text using the current list size.

root = tk.Tk()  # Line 26 - Borrowed source support: creates the main application window.
root.title("Daily Task Tracker")  # Line 27 - My code: gives the window a title shown at the top.
root.geometry("360x420")  # Line 28 - Borrowed structure, my choice: sets the window width and height in pixels.
root.configure(bg="lightblue")  # Line 29 - My code: changes the background color to make the app look more personal.

title_label = tk.Label(root, text="My Daily Task Tracker", font=("Arial", 16, "bold"), bg="lightblue")  # Line 30 - My code: creates the heading label.
title_label.pack(pady=10)  # Line 31 - Borrowed structure, my use: places the title on the window with vertical spacing. .pack() automatically arranges widgets.

entry = tk.Entry(root, width=28, font=("Arial", 12))  # Line 32 - Borrowed structure, my use: creates a text box where the user types a task.
entry.pack(pady=8)  # Line 33 - Borrowed structure, my use: places the entry widget below the title.

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)  # Line 34 - Borrowed structure, my use: creates a button that runs add_task when clicked.
add_button.pack(pady=5)  # Line 35 - Borrowed structure, my use: places the add button on the window.

task_list = tk.Listbox(root, width=32, height=10, font=("Arial", 11))  # Line 36 - Borrowed structure, my use: creates the box that displays all tasks.
task_list.pack(pady=10)  # Line 37 - Borrowed structure, my use: places the listbox in the center area of the window.

delete_button = tk.Button(root, text="Delete Selected Task", width=18, command=delete_task)  # Line 38 - My code: creates a button for deleting one chosen task.
delete_button.pack(pady=5)  # Line 39 - Borrowed structure, my use: places the delete button on the window.

clear_button = tk.Button(root, text="Clear All Tasks", width=18, command=clear_tasks)  # Line 40 - My code: creates a button for removing all tasks.
clear_button.pack(pady=5)  # Line 41 - Borrowed structure, my use: places the clear button below the delete button.

count_label = tk.Label(root, text="Total Tasks: 0", font=("Arial", 11), bg="lightblue")  # Line 42 - My code: creates a label that shows the number of tasks.
count_label.pack(pady=10)  # Line 43 - Borrowed structure, my use: places the count label near the bottom of the window.

root.mainloop()  # Line 44 - Borrowed source support: keeps the GUI window open and waiting for user actions.