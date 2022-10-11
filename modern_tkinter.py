from tkinter import *
from PIL import ImageTk ,Image
import time
from canvasbutton import *
from functools import partial

class CButton(Button):
    def __init__(self,canvas,coord,animation=None,master=None,nam='current',**kwargs):
        super().__init__(**kwargs)
        #super().invoke()
        #global name
        self.name=nam
        self.c=canvas
        self.master=master
        self.c.create_image(coord,image=self.cget('image'),tag=self.name)
        #self.c.tag_bind(name,"<Enter>",self.bind_invoke)
        #self.c.tag_bind(name,"<Leave>",self.unbind_invoke)
        
        self.c.tag_bind(self.name,'<Button-1>',self._invoke)
        self.animation=animation
    def unbind_invoke(self,event):
        print('unbind_invoke')
        self.c.tag_unbind(self.name,'<Button-1>')
    def bind_invoke(self,event):
        print('bind_invoke')
        self.c.tag_bind(self.name,'<Button-1>',self._invoke)
    def _invoke(self,event):
        self.animate()
        print(self.cget('image'))
        print(self.name)
        #partial(self.invoke,self.name)
        self.invoke()
    def animate(self):
        if self.animation=='p':
            self.c.move(self.name,1,1)
            self.c.update_idletasks()
            time.sleep(0.1)
            self.c.move(self.name,-1,-1)
        elif self.animation=='s':
            self.c.scale(self.name,self.c.coords(self.name)[0],self.c.coords(self.name)[1],30/2,30/2)
            self.c.update_idletasks()
            time.sleep(0.1)
            self.c.scale(self.name,self.c.coords(self.name)[0],self.c.coords(self.name)[1],2/30,2/30)
count=0        
def do():
    global count
    count+=1
    print(count)
    
if __name__=='__main__':
    root=Tk()
    c=Canvas(root,bg='pink')
    c.pack(fill=BOTH,expand=1)
    #
    pre_img=Image.open('C:/codes/PostScript_problem/button.png')
    pre_img2=Image.open('C:/codes/PostScript_problem/save.png')
    
    size=tuple([i//8 for i in pre_img.size])
    size2=tuple([i//8 for i in pre_img2.size])
    
    img=ImageTk.PhotoImage(pre_img.resize(size))
    img2=ImageTk.PhotoImage(pre_img2.resize(size2))
    
    #img=ImageTk.PhotoImage(Image.open(img))
    #print(img.zoom(3,2))
    root.update_idletasks()
    w=root.winfo_width()
    h=root.winfo_height()
    b1=CButton(c,(w/1.5,h/1.5),image=img,command=do,state='normal',animation='p',master=root,nam='b1')
    b2=CButton(c,(w/3.5,h/3.5),image=img2,command=do,state='normal',animation='p',master=root,nam='b2')
    
    #c.image=ImageTk.PhotoImage(img)
    
    #b.pack()
