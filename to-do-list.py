import tkinter as tk

def add_list():
    task = entry.get() # type: ignore
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END) #type: ignore

def delete_list():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

#GUI
root = tk.Tk()
root.title("To-Do List App")

#Element of GUI
frame = tk.Frame(root)
frame.pack(pady=10)
listbox = tk.Listbox(frame, width = 70, height = 20, bd = 1, font=("Courier New", 14))
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set) 
scrollbar.config(command=listbox.yview)
entry = tk.Entry(root, font=("Courier New", 14))
entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", command=add_list, font=("Courier New", 14)) #type:ignore
add_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete Task", command=delete_list, font=("Courier New", 14)) #type:ignore
delete_button.pack(pady=5)
root.mainloop()