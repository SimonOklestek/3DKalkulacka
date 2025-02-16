from tkinter import ttk
import tkinter as tk
import pandas as pd

# Načtení tabulek
tabulka = pd.read_excel('filamenty.xlsx', header=0)
tabulka2 = pd.read_excel('mena.xlsx', header=0)
tabulka3 = pd.read_excel('material.xlsx', header=0)

celkcena = 0

# Hlavní okno
main_window = tk.Tk()
main_window.title("Výpočet ceny filamentu")
main_window.config()  # Set the main window background to gray

# Funkce pro vytvoření dropdown menu
def create_dropdown(parent, column_values, label_text, grid_column):
    label = tk.Label(parent, text=label_text)  # Set label background to gray
    label.grid(row=0, column=grid_column, pady=10, padx=10)
    dropdown = ttk.Combobox(parent, values=column_values, state="readonly")
    dropdown.set(column_values[0])  # Nastaví výchozí hodnotu
    dropdown.grid(row=1, column=grid_column, pady=10, padx=10)
    dropdown.config(style="Custom.TCombobox")  # Custom style for the dropdown
    return dropdown

filament_frame = tk.Frame(main_window)
filament_frame.grid(row=0, column=0)

# Výběr filamentu
column_values_filament = tabulka['značka'].tolist()
column_values_filament.insert(0, "Vyberte filament")
dropdown_filament = create_dropdown(filament_frame, column_values_filament, "Značka filamentu:", 0)

# Hmotnost objektu
label_weight = tk.Label(main_window, text="Hmotnost objektu:")
label_weight.grid(row=2, column=0, pady=10, padx=10)
entry_weight = tk.Entry(main_window, width=20)
entry_weight.grid(row=3, column=0, pady=10, padx=10)

currency_frame = tk.Frame(main_window)
currency_frame.grid(row=0, column=1)

#dropdown pro výběr měny
column_values_currency = tabulka2['měna'].tolist()
column_values_currency.insert(0, "Vyberte měnu")
dropdown_currency = create_dropdown(currency_frame, column_values_currency, "Měna:", 1)

# Přirážka 10%
label_priraska = tk.Label(main_window, text="Přirážka 10%")
label_priraska.grid(row=2, column=1, pady=10, padx=10)
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(main_window, variable=checkbox_var)
checkbox.grid(row=3, column=1, pady=10, padx=10)

# Funkce pro získání textu a výpočet ceny
def get_text():
    global celkcena
    entered_text = entry_weight.get()

    # Kontrola výběru filamentu
    if dropdown_filament.get() != "Vyberte filament":
        filament = dropdown_filament.get()
        cena = tabulka.query("značka=='" + filament + "'")["cena/kg"]
        value = cena.values[0]  # Získání ceny za kilogram filamentu

        # Kontrola výběru měny
        if dropdown_currency.get() != "Vyberte měnu":
            mena = dropdown_currency.get()
            kurz = tabulka2.query("měna=='" + mena + "'")["kurz"]
            value2 = kurz.values[0]  # Získání kurzu měny

            # Zpracování hmotnosti
            try:
                hmotnost = float(entered_text)
                celkcena = value * hmotnost * value2 / 1000

                if checkbox_var.get():
                    celkcena *= 1.10  #Zvyšujeme cenu o 10%

                vysledek.config(text=f"Cena: {celkcena:.2f} {mena}")
            except ValueError:
                vysledek.config(text="Zadejte platnou hmotnost")
        else:
            vysledek.config(text="Nebyla vybrána měna")
    else:
        vysledek.config(text="Nebyl vybrán filament")


# Tlačítko pro výpočet ceny
button = tk.Button(main_window, text="Získat cenu", command=get_text)
button.config(width=15, height=2)
button.grid(row=7, column=0, columnspan=2, pady=10)

# Zobrazení výsledku
vysledek = tk.Label(main_window, text="")
vysledek.grid(row=8, column=0, columnspan=2, pady=10)

main_window.mainloop()
