from tkinter import *
from tkinter import font
from tkinter import messagebox

output=str("0")

taschenrechner = Tk()
taschenrechner.title("Taschenrechner")
taschenrechner.geometry("800x600")
taschenrechner.configure(bg="#ffffff")
taschenrechner.resizable(False,False)


frame1 = Frame(taschenrechner, width=300, height=2, bg='red')
frame1.place(x=25, y=25, relx=0.00, rely=0.00)

Label(frame1, text=output, relief=RAISED, height=3, width=50).grid(row=0, column=0, padx=0, pady=0)

Button(frame1, text="=", height=2, width=5, relief=RAISED).grid(row=0, column=3, padx=0, pady=0)
Button(frame1, text="Clear", height=2, width=5, relief=RAISED).grid(row=0, column=4, padx=0, pady=0)

frame2 = Frame(taschenrechner, width=355, height=400, bg='red')
frame2.place(x=25, y=90, relx=0.00, rely=0.00)

taschenrechner.mainloop()





