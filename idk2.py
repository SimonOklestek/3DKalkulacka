import tkinter as tk

# Funkce pro zobrazení textového pole
def create_text_entry():
    # Vytvoření hlavního okna
    root = tk.Tk()
    root.title("Text Input in Tkinter")

    # Vytvoření popisku pro textové pole
    label = tk.Label(root, text="Zadejte nějaký text:")
    label.pack(pady=10)

    # Vytvoření textového pole pro vstup
    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    # Funkce pro získání hodnoty z textového pole
    def get_text():
        entered_text = entry.get()
        print("Zadaný text:", entered_text)

    # Tlačítko pro získání hodnoty z textového pole
    button = tk.Button(root, text="Získat text", command=get_text)
    button.pack(pady=10)

    # Start Tkinter event loop
    root.mainloop()

# Zavolání funkce pro zobrazení okna s textovým polem
create_text_entry()