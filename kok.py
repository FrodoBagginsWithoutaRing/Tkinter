import tkinter as tk

win = tk.Tk()

at = tk.Label(win,text="Koeficient a:")
at.pack()
a = tk.Entry(win)
a.pack()

bt = tk.Label(win,text="Koeficient b:")
bt.pack()
b = tk.Entry(win)
b.pack()

ct = tk.Label(win,text="Koeficient c:")
ct.pack()
c = tk.Entry(win)
c.pack()

def executor():
    print(a.get(),b.get(),c.get())
    ka = int(a.get())
    kb = int(b.get())
    kc = int(c.get())
    d = kb**2 - 4*ka*kc
    if d<0:
        print("Nema riesenie v R.")
        vysledok="Nema riesenie v R."
    elif d == 0:
        print("x:",-kb/(2*ka))
        vysledok=('Vysledok:',"x:",-kb/(2*ka))
    else:
        print("x1:",-kb + d ** 0.5 / (2*ka))
        print("x2:",-kb + d ** 0.5 / (2*ka))
        vysledok='Vysledok:',"x1:",-kb + d ** 0.5 / (2*ka),"x2:",-kb + d ** 0.5 / (2*ka)
    at = tk.Label(win,text=vysledok)
    at.pack()

button = tk.Button(win, text = "Daj!",command=executor)
button.pack()

# = tk.Label(win,text=vysledok)
#at.pack()

win.mainloop()
