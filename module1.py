from tkinter import *
from tkinter import messagebox as mb

def tst_psse(event):
    t=textbox.get()
    if t=="":
        mb.showwarning("T�helepanu!","On vaja sisestada numbreid!")
    else:
        pealkiri.configure(text=t,width=len(t))
        Textbox.delete(0,END)
        mb.showinfo("Aruanne","Tekst oli lisatud pealkirjasse")