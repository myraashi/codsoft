import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TO-DO LIST")


#entry field

tasklabel = tk.Label(root,text="Task Entry",font="Arial",height=3)
tasklabel.pack(pady=2)
tentry = tk.Entry(root,width=40,bd=3)
tentry.pack(pady=5)

#task listbox
display = tk.Label(root,text="Tasks",font="Arial",height=3)
display.pack(pady=2)
tlbox = tk.Listbox(root,width=40,selectmode=tk.SINGLE,border=4)
tlbox.pack()

def addTask():
    task = tentry.get()
    if task:
        tlbox.insert(tk.END,task)
        tentry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","Please enter a task.")

        
def deleteTask():
    stask = tlbox.curselection()
    if stask:
        tlbox.delete(stask)
    else:
        messagebox.showwarning("Warning","Please select a task.")
    

def compltd():
    stask = tlbox.curselection()
    if stask:
        tlbox.itemconfig(stask,{'bg':'light green'})
    else:
        messagebox.showwarning("Warning","Please select a proper task.")
    
    
    
    
addbut = tk.Button(root,text="Add Task",command=addTask)
deletebut = tk.Button(root,text="Delete Task", command = deleteTask)
markbut = tk.Button(root,text="Completed",command=compltd)
addbut.pack(pady=5)
markbut.pack(pady=5)
deletebut.pack(pady=5)

root.mainloop()