import tkinter as tk
from tkinter import ttk

import pyjokes
m = tk.Tk()
m.title('Nerd Jokes!')


messageVar = tk.Message(m)

def show_joke(category, language):
    ourMessage = pyjokes.get_joke(language, category)
    messageVar.config(text=ourMessage)
    messageVar.update()

# Create a label
category_label = tk.Label(m, text="Selected Category: ")
category_label.pack(pady=10)

# Create a Combobox widget
combo_box_cat = ttk.Combobox(m, values=list(pyjokes.CATEGORY_VALUES))
combo_box_cat.pack(pady=5)

# Set default value
combo_box_cat.set('neutral')

# Create a label
language_label = tk.Label(m, text="Selected Language: ")
language_label.pack(pady=10)

# Create a Combobox widget
combo_box_lan = ttk.Combobox(m, values=list(pyjokes.LANGUAGE_VALUES))
combo_box_lan.pack(pady=5)

# Set default value
combo_box_lan.set('en')

button = tk.Button(m, text='Get me a joke', width=25, command=lambda: show_joke(combo_box_cat.get(),combo_box_lan.get()))
button.pack()

messageVar.pack()

m.mainloop()