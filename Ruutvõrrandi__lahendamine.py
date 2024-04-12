import tkinter as tk
from tkinter import messagebox

def solve_quadratic(a, b, c):
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            messagebox.showinfo("Tulemus", "Tegelikke juuri pole".)
        elif discriminant == 0:
            x = -b / (2*a)
            messagebox.showinfo("Tulemus", f"Üks juur: x = {x}")
        else:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            messagebox.showinfo("Tulemus", f"Kaks juurt: x1 = {x1}, x2 = {x2}")
    except ValueError:
        messagebox.showerror("Tähelepanu", "On vaja sisestada numbreid!")

root = tk.Tk()
root.title("Ruutvõrrandi lahendamine")

a_label = tk.Label(root, text="a:", bg=)
a_label.grid(row=0, column=0, padx=10, pady=5)
a_entry = tk.Entry(root, bg=)
a_entry.grid(row=0, column=1, padx=10, pady=5)

b_label = tk.Label(root, text="b:", bg=)
b_label.grid(row=1, column=0, padx=10, pady=5)
b_entry = tk.Entry(root, bg=)
b_entry.grid(row=1, column=1, padx=10, pady=5)

c_label = tk.Label(root, text="c:", bg=)
c_label.grid(row=2, column=0, padx=10, pady=5)
c_entry = tk.Entry(root, bg=)
c_entry.grid(row=2, column=1, padx=10, pady=5)

solve_button = tk.Button(root, text="Otsusta", command=lambda: solve_quadratic(a_entry.get(), b_entry.get(), c_entry.get()), bg=)
solve_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()