import tkinter as tk
from tkinter import Radiobutton, IntVar, Entry, Button, Label, messagebox
import matplotlib.pyplot as plt
import numpy as np

graf = False

def lahendada_kvadraatiline():
    global graf, d
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

def prillid():
    x1 = np.arange(-9,-1.5,0.5)
    y1 = (-1/16)*(x1+5)**2 + 2
    x2 = np.arange(1,9.5,0.5)
    y2 = (-1/16)*(x2-5)**2 + 2
    x3 = np.arange(-9,-1.5,0.5)
    y3 = (1/4)*(x3+5)**2 - 3
    x4 = np.arange(1,9.5,0.5)
    y4 = (1/4)*(x4-5)**2 - 3
    x5 = np.arange(-9,-6.5,0.5)
    y5 = -(x5+7)**2 + 5
    x6 = np.arange(6,9.5,0.5)
    y6 = -(x6-7)**2 + 5
    x7 = np.arange(-1,1.5,0.5)
    y7 = -0.5*x7**2 + 1.5
    plt.figure()
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7)
    plt.title("Prillid")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def vihmavari():
    x1 = np.arange(-12,12.5,0.5)
    y1 = -(1/18*x1)**2 + 12
    x2 = np.arange(-4,4.5,0.5)
    y2 = -(1/8)*x2**2 + 6
    x3 = np.arange(-12,-4.5,0.5)
    y3 = -(1/8)*(x3+8)**2 + 6
    x4 = np.arange(4,12.5,0.5)
    y4 = -(1/8)*(x4-8)**2 + 6
    x5 = np.arange(-4,-0.8,0.5)
    y5 = 2*(x5+3)**2 - 9
    x6 = np.arange(-4,0.7,0.5)
    y6 = 1.5*(x6+3)**2 - 10
    plt.figure()
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6)
    plt.title("Vihmavari")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def vaal():
    x1 = np.arange(0,9.5,0.5)
    y1 = (2/27)*x1**2 - 3
    x2 = np.arange(-10,0.5,0.5)
    y2 = 0.04*x2**2 - 3
    x3 = np.arange(-9,-3.5,0.5)
    y3 = (2/9)*(x3+6)**2 + 1
    x4 = np.arange(-3,-9.5,0.5)
    y4 = (-1/12)*(x4-3)**2 + 6
    x5 = np.arange(5,8.8,0.5)
    y5 = (1/9)*(x5-5)**2 + 2
    x6 = np.arange(5,9,0.5)
    y6 = (1/8)*(x6-7)**2 + 1.5
    x7 = np.arange(-13,-9.5,0.5)
    y7 = -0.75*(x7+11)**2 + 6
    x8 = np.arange(-15,13.5,0.5)
    y8 = -(0.5)*(x8+13)**2 + 3
    x9 = np.arange(-15,-10.5,0.5)
    y9 = [1]*len(x9)
    x10 = np.arange(3,4.5,0.5)
    y10 = [3]*len(x10)
    plt.figure()
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10)
    plt.title("Vaal")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def toggle_window_size():
    if veel_button.cget("text") == "Suurenda akent":
        root.geometry("700x500")
        veel_button.config(text="Vähenda akent")
    else:
        root.geometry("400x250")
        veel_button.config(text="Suurenda akent")
    

root = tk.Tk()
root.title("Ruutvõrrandi lahendamine")
root.geometry("400x250")

võrrand_label = tk.Label(root, text="Ruutvõrrandi lahendamine", fg="green", bg="#cfebf7", wraplength=300)
võrrand_label.grid(row=0, column=0, columnspan=6, padx=10, pady=5)

a_entry = Entry(root, width=5, bg="#cfebf7")
a_entry.grid(row=1, column=0, padx=5, pady=5)
a_label = Label(root, text="x^2", fg="green", bg="#cfebf7")
a_label.grid(row=1, column=1, padx=5, pady=5)

b_entry = Entry(root, width=5, bg="#cfebf7",)
b_entry.grid(row=1, column=2, padx=5, pady=5)
b_label = Label(root, text="x", fg="green", bg="#cfebf7")
b_label.grid(row=1, column=3, padx=5, pady=5)

c_entry = Entry(root, width=5, bg="#cfebf7")
c_entry.grid(row=1, column=4, padx=5, pady=5)
c_label = Label(root, text="= 0", fg="green", bg="#cfebf7")
c_label.grid(row=1, column=5, padx=5, pady=5)

lahendada_button = Button(root, text="Lahenda", command=lahendada_kvadraatiline)
lahendada_button.grid(row=2, column=0, columnspan=6, padx=10, pady=5)

result_label = Label(root, text="", padx=10, pady=5, bg="#fca103")
result_label.grid(row=3, column=0, columnspan=6, sticky="nsew")

graf_button = Button(root, text="Graafik", command=lambda: graafik(graf, d))
graf_button.grid(row=4, column=0, columnspan=6, padx=10, pady=5)

veel_button = Button(root, text="Suurenda akent", bg="#cfebf7", command=toggle_window_size)
veel_button.grid(row=5, column=0, columnspan=6, padx=10, pady=5)

var = IntVar()
v1 = Radiobutton(root, text="Prillid", variable=var, value=1, command=prillid)
v2 = Radiobutton(root, text="Vihmavari", variable=var, value=2, command=vihmavari)
v3 = Radiobutton(root, text="Vaal", variable=var, value=3, command=vaal)
v1.grid(row=6, column=0, padx=5, pady=5, sticky="w")
v2.grid(row=6, column=1, padx=5, pady=5, sticky="w")
v3.grid(row=6, column=2, padx=5, pady=5, sticky="w")

root.mainloop()
