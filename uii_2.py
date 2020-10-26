import tkinter
from PIL import Image, ImageTk, ImageSequence

root = tkinter.Tk()
#root.wm_attributes('-type', 'splash')

class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(self.parent, width=400, height=400)
        self.parent.resizable(width=False, height=False)
        #self.window = tkinter.Toplevel(self.canvas)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'hearn.gif'))]
        self.image = self.canvas.create_image(200,200, image=self.sequence[0])
        self.animate(1)
        self.parent.resizable(False, False)
        self.parent._offsetx = 0
        self.parent._offsety = 0
        self.parent.bind('<Button-1>',self.clickwin)
        self.parent.bind('<B1-Motion>',self.dragwin)
        self.parent.update_idletasks()
        self.parent.overrideredirect(1)
        self.parent.mainloop()
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))
    def dragwin(self,event):
        x = self.parent.winfo_pointerx() - self.parent._offsetx
        y = self.parent.winfo_pointery() - self.parent._offsety
        self.parent.geometry('+{x}+{y}'.format(x=x,y=y))
    def clickwin(self,event):
        self.parent._offsetx = event.x
        self.parent._offsety = event.y
