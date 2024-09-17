from tkinter import *


from tkinter import font
from tkinter import messagebox
from tkinter import PhotoImage



def LabelTextÄndern():
    Label1.config(text="Hallo Welt!")

def InputAnzeigen(): #Definiert die Funktion
    input1 = InputName.get("1.0", END).strip() #Holt die Daten aus der Texteingabe und setzt sie in die Variable 'input1'
    messagebox.showinfo("Info", "Hallo, " + input1) #Zeigt eine Infobox mit dem Namen an

def WeiteresFensterÖffnen():
    Fenster2 = Toplevel(neuesFenster) #Erstellt ein neues Fenster auf dem alten
    Fenster2.title("Neues Fenster") #Setzt den Titel des Fensters fest
    Fenster2.geometry("300x200") #Setzt die Größe des Fensters fest
    Label(Fenster2, text="Hallo, ich bin ein neues Fenster").pack() #Erstellt ein Label mit Text

neuesFenster = Tk()
neuesFenster.title("Name des Fensters") #Hier geben wir den Namen des Fensters ein
neuesFenster.geometry("800x600") #Hier geben wir die Größe des Fensters ein
neuesFenster.configure(bg="#f0f0f0") #Hier können wir die Hintergrundfarbe des Fensters einstellen


menu = Menu(neuesFenster)
neuesFenster.config(menu=menu)



neuesmenu = Menu(menu)
menu.add_cascade(label="Menu 1", menu=neuesmenu)
neuesmenu.add_command(label="Schaltfläche 1", command=WeiteresFensterÖffnen)

Label1 = Label(neuesFenster, font="TkDefaultFont", text="Dies ist ein Text")
Label1.pack()

Button1 = Button(neuesFenster, text="Klick mich an!", command=LabelTextÄndern)
Button1.pack()


Label(neuesFenster, font="TkDefaultFont", text="\n").pack()

Label(neuesFenster, font="TkDefaultFont", text="Geben Sie Ihren Namen ein: ").pack()
InputName = Text(neuesFenster, font="TkDefaultFont", height=1, width=20)
InputName.pack()

Button2 = Button(neuesFenster, font="TkDefaultFont", text="Eingabe abschicken", command=InputAnzeigen).pack()


neuesFenster.mainloop() 
