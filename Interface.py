from tkinter import *
from jeuDeLaVie import *
from time import sleep


master = Tk()

MatSizeX = master.winfo_screenwidth()
MatSizeY = master.winfo_screenheight()
canWidth = 10
canHeight = 10


#def initialisation_jeu():



def initWindow(canWidth, canHeight):
    widthW = canWidth * MatSizeX + MatSizeX
    heightW = canHeight * MatSizeY + MatSizeY
    w = Canvas(master, width=widthW, height=heightW)
    w.pack()
    return w





def refreshGrille(w,canWidth, canHeight):
    widthW = canWidth * MatSizeX + MatSizeX
    heightW = canHeight * MatSizeY + MatSizeY

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



def color_case(t, w, canHeight):
    pas = canHeight+1
    rows, cols = t.shape
    for i in range (0,rows):
        for j in range(0, cols):
            if (t[i,j]==1):
                w.create_rectangle(pas*i,pas*j,pas*i+pas,pas*j+pas,fill='black')

def boucle(w, t, canWidth, canHeight, iter):
    for i in range(0, iter):
        w.update()
        w.delete('all')
        w.after(300, refreshGrille(w, canWidth, canHeight))
        t = iterations(t)
        color_case(t, w, canHeight)


w = initWindow(canWidth,canHeight)
refreshGrille(w, canWidth, canHeight)
color_case(t, w, canHeight)
w.update()
boucle(w, t, canWidth, canHeight, 11)

mainloop()



#w.create_line(50, 50, 100, 50, fill="#476042")


