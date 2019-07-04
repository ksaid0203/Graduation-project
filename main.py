import tkinter
from tkinter import filedialog, Canvas
from tkinter import *
from PIL import ImageTk, Image

ImageName = 'earth.jpg'

def UploadAction(event=None):
    global ImageName
    ImageName = filedialog.askopenfilename()
    print('Selected:', ImageName)

    im = Image.open(ImageName)
    canvasLeft.image = ImageTk.PhotoImage(im)
    canvasLeft.create_image(0, 0, image=canvasLeft.image, anchor='nw')

    canvasRight.image = ImageTk.PhotoImage(im)
    canvasRight.create_image(0, 0, image=canvasRight.image, anchor='nw')

window = tkinter.Tk()
window.title("Photo Recover")
window.geometry("1280x720+300+300")
window.resizable(False, False)
button = tkinter.Button(window, text='이미지 불러오기', command=UploadAction)
print('Selected2:', ImageName)
button.pack()

canvasLeft = Canvas(window, width=400, height=300)
canvasLeft.pack()

canvasRight = Canvas(window, width=400, height=300)
canvasRight.pack()

window.mainloop()

