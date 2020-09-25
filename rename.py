from tkinter import *

master = Tk()

MatSizeX = 11
MatSizeY = 11


def initWindow(canWidth, canHeight):
    widthW = canWidth * MatSizeX + MatSizeX
    heightW = canHeight * MatSizeY + MatSizeY
    w = Canvas(master, width=widthW, height=heightW)
    w.pack()

    for i in range(0, MatSizeY):
        begX = 0
        Y = i * canHeight + i
        endX = widthW
        w.create_line(begX, Y, endX, Y, fill="#476042")
    for i in range(0, MatSizeX):
        X = i * canWidth + i
        begY = 0
        endY = heightW
        w.create_line(X, begY, X, endY, fill="#476042")


initWindow(60, 60)
mainloop()
