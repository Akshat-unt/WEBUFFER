# Importing application:

from WEBUFFER import application_

# ImportLibraryHere
from tkinter import *
from PIL import ImageTk, Image

# SplashScreen


sroot = Tk()
sroot.overrideredirect(1)

sroot.minsize(height=388, width=520)

sroot.title("Splash window")

sroot.configure()

spath = 'Images\\splash.gif'

simg = ImageTk.PhotoImage(Image.open(spath))

my = Label(sroot, image=simg)

my.image = simg

my.place(x=-2, y=-1.5)

Frame(sroot, height=500, width=900, bg='black').place(x=520, y=500)


# MainScreen


def mainroot():
    application_()


# calling the main window here


def call_mainroot():
    sroot.destroy()

    mainroot()


sroot.after(3000, call_mainroot)  # TimeOfSplashScreen

mainloop()
