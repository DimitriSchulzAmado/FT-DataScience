from tkinter import *
import tkintermapview

root = Tk()
root.title('Inatel View Map')
root.geometry('900x700')
my_lable = LabelFrame(root)
my_lable.pack(pady=50)
map_widget = tkintermapview.TkinterMapView(my_lable, width=800, height=600, corner_radius=0)
map_widget.set_position(-22.25670, -45.69725)
map_widget. set_zoom(17)
map_widget.pack()
root.mainloop()
