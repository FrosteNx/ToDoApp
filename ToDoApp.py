from tkinter import *
from tkinter import font

root = Tk()
root.title("ToDoApp")
root.geometry("400x650+400+100")
root.resizable(False, False)

custom_font = font.Font(family="Arial Rounded MT Bold", size=20)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    
    if(task):
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)
        
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + '\n')
                
        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task) 
    except:
        file = open("tasklist.txt", "w")
        file.close()

image_icon = PhotoImage(file="Image/todolist.png")
root.iconphoto(False, image_icon)

top_image = PhotoImage(file="Image/topbar.png")
Label(root, image=top_image).pack()

dock_image = PhotoImage(file="Image/dock.png")
Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)

heading = Label(root, text="TO DO:", font=custom_font, fg="white", bg="#32405b")
heading.place(x=150, y=20)

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=100)

task = StringVar()
task_entry = Entry(frame, width=18, font=custom_font, bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font=custom_font, width=6, bg="#800080", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(90, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=20, bg="#32405b", fg="white", cursor="hand2", selectbackground="#800080")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

delete_icon = PhotoImage(file="Image/delete1.png")
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=27)

openTaskFile()

root.mainloop()