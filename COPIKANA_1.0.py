import pykakasi
import pyperclip
import base64
import os
import tkinter as tk
from tkinter import ttk
import webbrowser


def to_hira():  # Convert kanji to hiragana

    kks = pykakasi.kakasi()
    clipboard_text = pyperclip.paste()  # Get text from clipboard
    result = kks.convert(clipboard_text)
    hira_text = ""
    for item in result:  # Keep hiragana only from result
        hira_text += item["hira"] + "　"
    label.config(text=hira_text)


def update_label():
    clipboard_text = str(pyperclip.paste())
    label_text = str(label.cget("text"))
    if clipboard_text != label_text:
        to_hira()
    else:
        pass
    root.after(500, update_label)


def change_size(x):
    size = int(float(x))
    label.config(font=("MS PGothic", size))


# Creat a window
root = tk.Tk()
root.title("COPIKANA 1.0")
root.geometry("+100+100")
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
except ModuleNotFoundError:

    def open_link(event):
        webbrowser.open("https://ko-fi.com/s/b8e4f06daa")

    alt = tk.Tk()
    alt.title("❤︎ COPIKANA?")
    alt.geometry("+100+10")
    alt.attributes("-topmost", True)
    shop = tk.Label(
        alt,
        font=(
            "",
            16,
        ),
        text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐦𝐞 𝐚𝐧𝐝 𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐭𝐡𝐞 𝐞𝐱𝐜𝐥𝐮𝐬𝐢𝐯𝐞 𝐥𝐨𝐠𝐨! 🎁",
    )
    shop.pack()
    kofi = tk.Label(
        alt,
        font=("", 18, "underline"),
        text="👉 𝐆𝐨 𝐭𝐨 𝐦𝐲 𝐊𝐨-𝐟𝐢 𝐬𝐡𝐨𝐩",
        fg="#F05312",
        cursor="hand2",
    )
    kofi.pack()
    kofi.bind("<Button-1>", open_link)

# Creat a scale to change size
scale = ttk.Scale(
    root, from_=17, to=51, length=225, orient="horizontal", command=change_size
)
# Create a label
label = tk.Label(root, font=("MS PGothic", 17), wraplength=720)
update_label()
# Position the widgets
scale.pack(fill="x")
label.pack()
root.mainloop()
