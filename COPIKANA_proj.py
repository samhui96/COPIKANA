import pykakasi
import pyperclip
import base64
import os
import tkinter as tk
from tkinter import ttk


def to_hira():  # Convert kanji to hiragana
    kks = pykakasi.kakasi()
    clipboard_text = pyperclip.paste()  # Get text from clipboard
    result = kks.convert(clipboard_text)
    hira_text = ""
    for item in result:  # Keep hiragana only from result
        hira_text += item["hira"] + "　"
    label.config(text=hira_text)


def to_hepburn():  # Convert kanji to hiragana
    kks = pykakasi.kakasi()
    clipboard_text = pyperclip.paste()  # Get text from clipboard
    result = kks.convert(clipboard_text)
    hepburn_text = ""
    for item in result:  # Keep hiragana only from result
        hepburn_text += item["hepburn"] + " "
    label.config(text=hepburn_text)


def to_mode(x=None):  # Mode switch
    if int(toggle.get()) == 0:
        to_hira()  # Convert to hiragana
    elif int(toggle.get()) == 1:
        to_hepburn()  # Convert to Hepburn romanization
    return


def update_label():
    clipboard_text = str(pyperclip.paste())
    label_text = str(label.cget("text"))
    if clipboard_text != label_text:
        to_mode()
    else:
        pass
    root.after(500, update_label)


def change_size(x):
    size = int(float(x))
    label.config(font=("MS PGothic", size))


# Creat a window
root = tk.Tk()
root.title("COPIKANA 1.0")
root.attributes("-topmost", True)
style = ttk.Style()
style.theme_use("winnative")
style.configure("Horizontal.TScale")

try:
    from COPIKANA_logo import img

    temp = open("temp.ico", "wb+")  # Create a temp file to hold icon
    temp.write(base64.b64decode(img))
    temp.close()
    root.iconbitmap("temp.ico")
    os.remove("temp.ico")
except:
    pyperclip.copy("Logo missing")

# Creat frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Creat a scale to change mode
toggle = ttk.Scale(frame1, to=1, length=15, orient="horizontal", command=to_mode)

# Creat a scale to change size
scale = ttk.Scale(
    frame1, from_=17, to=51, length=225, orient="horizontal", command=change_size
)

# Create a label
label = tk.Label(frame2, font=("MS PGothic", 17), wraplength=720)
update_label()

# Position the widgets
frame1.pack(fill="x")
toggle.pack(side="left")
scale.pack(fill="x")
frame2.pack()
label.pack()

root.mainloop()
