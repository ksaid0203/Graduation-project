import cv2 as cv
import numpy as np
from tkinter import Tk, filedialog

win_name ='Image Recovery'

penThick=10

def onChange(value):
    global penThick
    penThick = cv.getTrackbarPos('penThick', win_name)

    print(penThick)

def mouse_callback(event, x, y, flags, param):
    global srcImage, maskLayer, paintingImage

    if event == cv.EVENT_MOUSEMOVE :
        if flags & cv.EVENT_LBUTTONDOWN :
            cv.circle(maskLayer, (x,y), penThick, (0, 0, 0), -1);
            cv.circle(paintingImage, (x, y), penThick, (0, 0, 0), -1);

    if event == cv.EVENT_RBUTTONDBLCLK :
        maskLayer = (255,255,255)
        paintingImage = cv.imread(image_path, cv.IMREAD_ANYCOLOR)

    cv.imshow(win_name, paintingImage)


if __name__ == '__main__':
    global srcImage, maskLayer, paintingImage

    gui_root = Tk()
    image_path = filedialog.askopenfilename(initialdir="/", title="Pick an Image", filetypes=(("ImageFiles", "*.jpg"),(" AllFiles", "*.*")))
    gui_root.destroy()

    srcImage = cv.imread(image_path, cv.IMREAD_ANYCOLOR)
    paintingImage = cv.imread(image_path, cv.IMREAD_ANYCOLOR)

    maskLayer = np.zeros((srcImage.shape[0], srcImage.shape[1] , 3), np.uint8)
    maskLayer[:] = (255,255,255)

    cv.namedWindow(win_name, cv.WINDOW_GUI_EXPANDED)
    cv.imshow(win_name, paintingImage)
    cv.setMouseCallback(win_name,mouse_callback, (paintingImage, maskLayer))
    cv.createTrackbar('penThick',win_name, 10, 15, onChange)

    cv.waitKey(0)
    cv.imwrite("outMask.png", maskLayer)
    cv.destroyAllWindows()   