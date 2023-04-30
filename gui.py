import tkinter as tk


# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Mein GUI")


# Erstellen der Kontrollleuchten
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()

checkbox1 = tk.Checkbutton(root, text="Auto Clicker an", variable=var1)
checkbox1.pack()
checkbox2 = tk.Checkbutton(root, text="Box", variable=var2)
checkbox2.pack()
checkbox3 = tk.Checkbutton(root, text="Chest Hunt", variable=var3)
checkbox3.pack()
checkbox4 = tk.Checkbutton(root, text="Bonus Level", variable=var4)
checkbox4.pack()


root.mainloop()
