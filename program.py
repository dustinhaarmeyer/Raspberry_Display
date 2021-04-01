from tkinter import *
from tkinter import ttk

fullscreen = True

def start():
    print('Start')

def ToggleFullscreen():
    global fullscreen
    if fullscreen == True:
        window.attributes("-fullscreen", False)
        fullscreen = False
    elif fullscreen == False:
        window.attributes("-fullscreen", True)
        fullscreen = True

window = Tk()
window.title("Control")
mainframe = ttk.Frame(window)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

Exit = ttk.Button(mainframe, text="Exit").grid(column=1, row=1, sticky=W)
ToggleFullscreen = ttk.Button(mainframe, text="Toggle Fullscreen", command=ToggleFullscreen).grid(column=3, row=1, sticky=W)
Option1 = ttk.Button(mainframe, text="Richtig", command=start).grid(column=2, row=2, sticky=W)
Option2 = ttk.Button(mainframe, text="Richtig", command=start).grid(column=2, row=3, sticky=W)
Option3 = ttk.Button(mainframe, text="Richtig", command=start).grid(column=2, row=4, sticky=W)
Option4 = ttk.Button(mainframe, text="Richtig", command=start).grid(column=2, row=5, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
window.bind("<Return>")
window.attributes("-fullscreen", True)
window.mainloop()