import tk_tools
import tkinter

root = tkinter.Tk()
root.title("nyoba")
root.geometry('600x600')

# graph = tk_tools.Graph(
#     parent=root,
#     x_min=-1.0,
#     x_max=1.0,
#     y_min=0.0,
#     y_max=2.0,
#     x_tick=0.2,
#     y_tick=0.2,
#     width=500,
#     height=400
# )

led = tk_tools.Led(root, size=50)
led.pack()

led.to_red()
led.to_green(on=True)

# graph.grid(row=0, column=0)
# # create an initial line
# line_0 = [(x/10, x/10) for x in range(10)]
# graph.plot_line(line_0)

root.mainloop()
