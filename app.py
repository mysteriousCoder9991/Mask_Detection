import os
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk

# Main Window
window = Tk()
window.geometry("960x550")
window.title('Face Mask Detector 2.0')
window.resizable(False, False)


# funtion to call chatbot gui

def chatGuiFun():
    os.system('python gui_chatbot.py')


def start():
    messagebox.showinfo("Thank You!", "Please Stay Connected For The Result.")
    messagebox.showinfo("Info", "Loading the main application")
    os.system("python main.py --img-mode 0 --video-path 0")
    messagebox.showinfo("Alert","The application suspended successfully")


def exit1():
    messagebox.showinfo("Thank you for using!", "This project has been developed by Group 5B")
    window.destroy()


# Background image
background_image = ImageTk.PhotoImage(file="background.jpg")
background = Label(window, image=background_image, bd=0)
background.place(x=0, y=0)

l = Label(window, text='Welcome \nTo \nFace Mask\nDetector 2.0 ', bg="black", fg="white")
l.config(font=("Courier", 24), justify=LEFT)
l.place(x=10, y=200)

btn1 = Button(window, text=' START HERE ', background="white", fg="black", activebackground="green",
              activeforeground="red", font=("Courier", 12), command=start)
btn1.place(x=750, y=230)

btn2 = Button(window, text='    EXIT    ', background="white", fg="black", activebackground="green",
              activeforeground="red", font=("Courier", 12), command=exit1)
btn2.place(x=750, y=280)

btn2 = Button(window, text=' Help? ', background="black", fg="white", activebackground="green", activeforeground="red",
              borderwidth=0, font=("Courier", 13), command=chatGuiFun)
btn2.place(x=870, y=30)

window.mainloop()
