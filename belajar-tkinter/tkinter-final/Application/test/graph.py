from tkinter import Tk, Entry
from tk_tools import ToolTip
root = Tk()

entry = Entry(root)
entry.grid()

# createst a tooltip
ToolTip(entry, 'enter a value between 1 and 10')

root.mainloop()
