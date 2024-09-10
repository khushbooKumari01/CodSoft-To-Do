import tkinter as tk
from tkinter import messagebox

# Main window setup
windows = tk.Tk()
windows.title("GUI Interface")
windows.minsize(300,100)
windows.maxsize(500,1000)
windows.geometry("999x456")
f1= tk.Frame(windows, bg="grey", borderwidth=6,)
l=tk.Label(f1,text="To-Do-App",fg="red",font=("comicsansms",19,"bold"))
l.pack(padx=142)
f1.pack()

# Start from add operation
def add_task():
    task = entry_task.get() #retrive the current text
    if task:  # Check task
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)  # Clear the entry field after adding
#Start here update operation
def update_task(task=None):
            chooseIndex = listbox_tasks.curselection()
            if chooseIndex:
                update = entry_task.get() #retrive the current text
                if update.strip() == "":
                    messagebox.showwarning("Input Error", "Task cannot be empty")
                    return
                index = chooseIndex[0]
                listbox_tasks.delete(index)
                listbox_tasks.insert(index, update)
                task[index] = update
                entry_task.delete(0, tk.END)
            else:
                messagebox.showwarning("Selection Error", "No task selected")

# operation for deletion
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        pass  #nothing do, task is not selected

# clear all operation
def clear_all_tasks():
    listbox_tasks.delete(0, tk.END)

# Entry widget for task input
entry_task = tk.Entry(windows, width=40,)
entry_task.pack(pady=10)

# Add button
add_button = tk.Button(windows, text="Add Task", width=15, command=add_task,fg="navy blue")
add_button.pack(pady=5,padx=3)

# Listbox to display
listbox_tasks = tk.Listbox(windows, width=50, height=10)
listbox_tasks.pack(pady=10)

update_button = tk.Button(windows, text="Update Task", width=15, command=update_task,fg="navy blue")
update_button.pack(pady=5,padx=3)
# Delete button
delete_button = tk.Button(windows, text="Delete Task", width=15, command=delete_task,fg="navy blue")
delete_button.pack(pady=5,padx=3)

# Clear button
clear_button = tk.Button(windows, text="Clear All Tasks", width=15, command=clear_all_tasks,fg="navy blue" )
clear_button.pack(pady=5,padx=3)

# Start the main event loop
windows.mainloop()