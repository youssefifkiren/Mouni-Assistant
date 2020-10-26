import tkinter
from PIL import Image, ImageTk, ImageSequence
import threading

#root = tkinter.Tk()

class App(threading.Thread):
    def __init__(self):
        self.parent = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.parent, width=400, height=400)
        self.parent.resizable(width=False, height=False)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'hearn.gif'))]
        self.image = self.canvas.create_image(200,200, image=self.sequence[0])
        self.animate(1)
        self.parent.mainloop()
        threading.Thread.__init__(self)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

