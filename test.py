from tkinter import *
from tkinter import ttk

def up(event):
    print("up")
def down(event):
    print("down")
def left(event):
    print("left")
def right(event):
    print("right")
def stopV(event):
    print("stopV")
def stopH(event):
    print("stopH")

root = Tk()
root.title("Telescope Controller")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

Bup = ttk.Button(mainframe, text="Up")
Bup.grid(column=2, row=1, sticky=(W, E))
Bup.bind("<ButtonPress>",up)
Bup.bind("<ButtonRelease>",stopV)
Bdwn = ttk.Button(mainframe, text="Down")
Bdwn.grid(column=2, row=3, sticky=W)
Bdwn.bind("<ButtonPress>",down)
Bdwn.bind("<ButtonRelease>",stopV)
Bl = ttk.Button(mainframe, text="Left")
Bl.grid(column=1, row=2, sticky=E)
Bl.bind("<ButtonPress>",left)
Bl.bind("<ButtonRelease>",stopH)
Br = ttk.Button(mainframe, text="Right")
Br.grid(column=3, row=2, sticky=W)
Br.bind("<ButtonPress>",right)
Br.bind("<ButtonRelease>",stopH)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()