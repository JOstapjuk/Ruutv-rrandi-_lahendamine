import tkinter as tk
from tkinter import messagebox
from tkinter import font
import matplotlib.pyplot as plt
import numpy as np

graf = False

def lahendada_kvadraatiline():
    global graf
    global d
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        
        d = b**2 - 4*a*c
        if d < 0:
            messagebox.showinfo("Tulemus", "Tegelikke juuri pole")
            graf = False
        elif d == 0:
            x = -b / (2*a)
            messagebox.showinfo("Tulemus", f"Tekst oli lisatud pealkirjasse")
            graf = True
        else:
            x1 = (-b + d**0.5) / (2*a)
            x2 = (-b - d**0.5) / (2*a)
            messagebox.showinfo("Tulemus", f"Tekst oli lisatud pealkirjasse")
            graf = True
        result_label.configure(text=f"D = {d}\nx1 = {x1}, x2 = {x2}")
    except ValueError:
        messagebox.showerror("Tähelepanu", "On vaja sisestada numbreid!")

def graafik(graf, d):
    if graf==True:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        
        x0 = -b / (2*a)
        y0 = a*x0*x0 + b*x0 + c
        x1 = np.arange(x0-10, x0+10, 0.5)
        y1 = a*x1**2 + b*x1 + c
        
        plt.plot(x1, y1, 'b-d')
        plt.title("Ruudu võrrand")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        
        text = f"Parabooli tipp ({x0:.2f}, {y0:.2f})"
    else:
        text = "Graafikut ei saa ehitada"
    
    result_label.configure(text=f"D = {d}\n{text}")

root = tk.Tk()
root.title("Ruutvõrrandi lahendamine")
root.geometry("400x250")

võrrand_label = tk.Label(root, text="Ruutvõrrandi lahendamine", fg="green", bg="#cfebf7")
võrrand_label.grid(row=0, column=0, columnspan=6, padx=10, pady=5)

a_entry = tk.Entry(root, width=5, bg="#cfebf7")
a_entry.grid(row=1, column=0, padx=5, pady=5)
a_label = tk.Label(root, text="x^2", fg="green", bg="#cfebf7")
a_label.grid(row=1, column=1, padx=5, pady=5)

b_entry = tk.Entry(root, width=5, bg="#cfebf7",)
b_entry.grid(row=1, column=2, padx=5, pady=5)
b_label = tk.Label(root, text="x", fg="green", bg="#cfebf7")
b_label.grid(row=1, column=3, padx=5, pady=5)

c_entry = tk.Entry(root, width=5, bg="#cfebf7")
c_entry.grid(row=1, column=4, padx=5, pady=5)
c_label = tk.Label(root, text="= 0", fg="green", bg="#cfebf7")
c_label.grid(row=1, column=5, padx=5, pady=5)

lahendada_button = tk.Button(root, text="Lahenda", command=lahendada_kvadraatiline)
lahendada_button.grid(row=2, column=0, columnspan=6, padx=10, pady=5)

result_label = tk.Label(root, text="", padx=10, pady=5, bg="#fca103")
result_label.grid(row=3, column=0, columnspan=6, sticky="nsew")

graf_button = tk.Button(root, text="Graafik", command=lambda: graafik(graf, d))
graf_button.grid(row=4, column=0, columnspan=6, padx=10, pady=5)

root.mainloop()