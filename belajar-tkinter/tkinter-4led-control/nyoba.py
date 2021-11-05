from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk(theme="blue")
ttk.Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()
