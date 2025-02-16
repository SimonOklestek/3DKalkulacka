from tkinter import ttk
import tkinter as tk
import pandas as pd

tabulka = pd.read_excel('filamenty.xlsx', header=0)
celkcena=0
#print(tabulka)
main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
dropdown = ttk.Combobox(main_window)
label = tk.Label(main_window, text="značka filamentu:")
label.pack(pady=10)
def create_dropdown(column_values):
    dropdown = ttk.Combobox(main_window, values=column_values)
    dropdown.set(column_values[0])
    dropdown.pack(pady=20)

column_values = tabulka['značka'].tolist()
column_values.insert(0, "Vyberte filament")
create_dropdown(column_values)
label = tk.Label(main_window, text="Hmotnost objektu:")
label.pack(pady=10)

entry = tk.Entry(main_window, width=30)
entry.pack(pady=10)

tabulka2 = pd.read_excel('mena.xlsx', header=0)
column_values2 = tabulka2['měna'].tolist()
column_values2.insert(0, "Vyberte měnu")
celkcena2=0
dropdown2 = ttk.Combobox(main_window)
def create_dropdown2(column_values2):
    dropdown2 = ttk.Combobox(main_window, values=column_values2)
    dropdown2.set(column_values2[0])
    dropdown2.pack(pady=20)
label = tk.Label(main_window, text="měna:")
label.pack(pady=10)
create_dropdown2(column_values2)

label = tk.Label(main_window, text="Hmotnost objektu:")
label.pack(pady=10)

def get_text():
    global celkcena
    entered_text = entry.get()
    if dropdown.selection_get() !="" and dropdown.selection_get() !="Vyberte filament":
        filament=dropdown.selection_get()
        print(filament)
        cena = tabulka.query("značka=='" + filament + "'")["cena/kg"]
        value = cena.values[0]
    elif dropdown2.selection_get() !="" and dropdown2.selection_get() !="Vyberte měnu":
        idk=dropdown2.selection_get()
        mena = tabulka.query("měna=='" + idk + "'")["kurz"]
        value2 = mena.values[0]

        celkcena = value * int(entered_text) * value2 / 1000
        vysledek.config(text=celkcena)
    else:
        vysledek.config(text="Nebyl vybran filament")

button = tk.Button(main_window, text="Získat text", command=get_text)
button.pack(pady=10)

vysledek=tk.Label(main_window, text="")
vysledek.pack(pady=10)

main_window.mainloop()