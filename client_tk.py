# %%
from tkinter import *
from turtle import onclick
# pip install tkcalendar
from tkcalendar import DateEntry
from datetime import date
# %%
def launch():
    print("launched !")

# objet fenêtre
fen = Tk()
fen.geometry("320x210")
# ajout composant
label_start = Label(fen, text="date_start")
# disposition du composant
# label.pack()
label_start.grid(column=0, row=0)
date_start = DateEntry(
    fen, 
    selectmode="day", 
)
date_start.grid(column=1, row=0)
date_start.set_date(date.today())

label_end = Label(fen, text="date_end").grid(column=0, row=1)
date_end = DateEntry(
    fen, 
    selectmode="day",
)
date_end.grid(column=1, row=1)
date_end.set_date(date.today())


button_ok = Button(text="GO", command=launch)
button_ok.grid(column=2, row=1)
# lancement de la fenêtre
fen.mainloop()
# %%
help(DateEntry)