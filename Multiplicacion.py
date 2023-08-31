from tkinter import *

root = Tk()

root.title("Multiplicación")
root.geometry("400x200")

show_result = Label(root)

def add():
    result = 2 * 1012
    show_result["text"] = result
    
btn = Button(root, text="Multiplicar", command=add)

btn.pack()
show_result.pack()

root.mainloop()