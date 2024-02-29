import pykakasi
import pyperclip
import tkinter as tk

def convert(): # Convert Kanji to Hiragana
    kks = pykakasi.kakasi()
    copied_text = pyperclip.paste()
    result = kks.convert(copied_text)
    hiragana_text = ""
    for item in result:
        hiragana_text += item["hira"] + ""
    return hiragana_text

def update_label(): # Send Hiragana to the window
    converted_text = convert()
    label.config(text = converted_text, font = ("", 14))
    root.after(500, update_label)  # Update label every 0.5 second
  
root = tk.Tk()
root.title("COPIKANA beta")
root.attributes('-topmost', True)  # Set window to stay on top
frame = tk.Frame(width = 240) # Set minimum width of the window
label = tk.Label()
update_label()  # Start updating label initially
label.pack()
frame.pack()
root.mainloop()