# %%
from tkinter import *
# pip install tkcalendar
from tkcalendar import DateEntry
from datetime import date
# %%
CONF = {
    "font": 18,
    "padx": 3,
    "pady": 3, 
    "width": 3,
    "height": 3
}

def launch():
    print(db.get_dates())

class DateBetween(Frame):

    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        Label(self, text="date_start", **cnf).grid(column=0, row=0)
        Label(fen, text="date_end", **cnf).grid(column=0, row=1)

        self.date_start = DateEntry(
            fen, 
            selectmode="day",
            **cnf
        )
        self.date_start.grid(column=1, row=0)
        self.date_start.set_date(date.today())

        self.date_end = DateEntry(
            fen, 
            selectmode="day",
            **cnf
        )
        self.date_end.grid(column=1, row=1)
        self.date_end.set_date(date.today())
    
    def get_dates(self):
        return (self.date_start.get(), self.date_end.get())

# objet fenêtre
fen = Tk()
fen.geometry("1024x512")
# # ajout composant
# label_start = Label(fen, text="date_start", **CONF)
# # disposition du composant
# # label.pack()
# label_start.grid(column=0, row=0)
# date_start = DateEntry(
#     fen, 
#     selectmode="day",
#     **CONF
# )
# date_start.grid(column=1, row=0)
# date_start.set_date(date.today())

# label_end = Label(fen, text="date_end", **CONF).grid(column=0, row=1)
# date_end = DateEntry(
#     fen, 
#     selectmode="day",
#     **CONF
# )
# date_end.grid(column=1, row=1)
# date_end.set_date(date.today())
db = DateBetween(fen)
db.grid(column=0, row=0)

button_ok = Button(fen, text="GO", command=launch, **CONF)
button_ok.grid(column=0, row=2)
# lancement de la fenêtre
fen.mainloop()
# %%
# %%
