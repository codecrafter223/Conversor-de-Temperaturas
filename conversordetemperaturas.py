from tkinter import *

root = Tk()
root.title("Conversor de Temperaturas")
root.geometry("600x300")
frame = Frame(root)
frame.pack()

def fahrenheit():
    try:
        temperatura = float(fahrenheit_entry.get())
        temperatura_celsius = (temperatura - 32) * 5 / 9
        temperatura_kelvin = temperatura_celsius + 273.15

        celsius_entry.delete(0, END)
        celsius_entry.insert(0, str(round(temperatura_celsius, 2)))

        kelvin_entry.delete(0, END)
        kelvin_entry.insert(0, str(round(temperatura_kelvin, 2)))
    except ValueError:
        clear_entries()

def celsius():
    try:
        temperatura = float(celsius_entry.get())
        temperatura_fahrenheit = (9/5) * temperatura + 32
        temperatura_kelvin = temperatura + 273.15

        fahrenheit_entry.delete(0, END)
        fahrenheit_entry.insert(0, str(round(temperatura_fahrenheit, 2)))

        kelvin_entry.delete(0, END)
        kelvin_entry.insert(0, str(round(temperatura_kelvin, 2)))
    except ValueError:
        clear_entries()

def kelvin():
    try:
        temperatura = float(kelvin_entry.get())
        temperatura_fahrenheit = (9/5) * (temperatura - 273.15) + 32
        temperatura_celsius = temperatura - 273.15

        fahrenheit_entry.delete(0, END)
        fahrenheit_entry.insert(0, str(round(temperatura_fahrenheit, 2)))

        celsius_entry.delete(0, END)
        celsius_entry.insert(0, str(round(temperatura_celsius, 2)))
    except ValueError:
        clear_entries()

def clear_entries():
    fahrenheit_entry.delete(0, END)
    celsius_entry.delete(0, END)
    kelvin_entry.delete(0, END)
    fahrenheit_entry.insert(0, "Ingrese un número válido")

# Entries
fahrenheit_entry = Entry(frame)
fahrenheit_entry.grid(row=1, column=1)

celsius_entry = Entry(frame)
celsius_entry.grid(row=1, column=2)

kelvin_entry = Entry(frame)
kelvin_entry.grid(row=1, column=3)

# Botones
fahrenheit_button = Button(frame, text="Convertir a Celsius y Kelvin", command=fahrenheit)
fahrenheit_button.grid(row=2, column=1)

celsius_button = Button(frame, text="Convertir a Fahrenheit y Kelvin", command=celsius)
celsius_button.grid(row=2, column=2)

kelvin_button = Button(frame, text="Convertir a Fahrenheit y Celsius", command=kelvin)
kelvin_button.grid(row=2, column=3)

# Etiquetas
Label(frame, text="Fahrenheit").grid(row=0, column=1)
Label(frame, text="Celsius").grid(row=0, column=2)
Label(frame, text="Kelvin").grid(row=0, column=3)

root.mainloop()
