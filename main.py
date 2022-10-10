from tkinter import Tk, Canvas, messagebox, NW
from PIL import Image, ImageTk

import time

window = Tk()
window.title("Un titre pour ma super fenêtre")
window.geometry("1200x800")
canvas = Canvas(window, bg="#000000")
canvas.pack(fill="both", expand=True)
x = 0
y = 0
radius = 50
stepX = 4
stepY = 4
#myCircle = canvas.create_oval(x, y, radius*2, radius*2, fil="red", outline="red")
img = ImageTk.PhotoImage(Image.open("JADT.jpg"))
myCircle = canvas.create_image(x, y, anchor=NW, image=img)
window.update()
while True:
    if x + 150 + stepX >= 1200 or x + stepX <= 0:
        stepX = -stepX

    if y + 200 + stepY >= 800 or y + stepY <= 0:
        stepY = -stepY
    x += stepX
    y += stepY

    canvas.coords(myCircle, x, y)
    window.update()
    time.sleep(0.001)

window.mainloop()
