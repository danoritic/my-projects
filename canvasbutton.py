# making canvas button
from PIL import ImageTk,Image
#from PIL.ImageTk import *
import os
import time
class CanvasButton:
    def __init__(self,master,canvas,image_name,ref,function):
        self.master=master
        self.canvas=canvas
        self.path='C:/codes/Fancy frames/'
        self.function=function
        self.name=image_name
        #self.coord=coord
        self.ref=ref
        self.function=function
        self.canvas.tag_bind(self.ref,'<Button-1>',self.button)
    def button(self,event):
        if not self.check_button_image():
            #print("*************")
            img=Image.open(self.path+self.name)
            img=img.convert('RGBA')
            new_data=[]
            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    pix=img.getpixel((i,j))
                    #print(type(pix))\
                    '''
                    if  pix[3]!=255:
                        print('changing color')
                    '''
                    img.putpixel((i,j),(255,255,255,img.getpixel((i,j))[3]))
                    '''
                    else:
                        print(' color')
                        img.putpixel((i,j),(img.getpixel((i,j))))
                    '''
            name=self.name[:-4]+'_pressed.png'
            img2=Image.new('RGBA',img.size)
            new_data=img.getdata()
            img2.putdata(new_data)
            img2.save(self.path+name,'PNG')
        #print("fooing********")
        for i in os.listdir(self.path):
            if self.name[:-4] and 'pressed' in i:
                imgr=ImageTk.PhotoImage(Image.open(self.path+i).
                                        resize((int(300/2.847090663058187)-5,int(300/2.847090663058187)-4)))
        former_image=self.canvas.itemcget(self.ref,'image')
        #print(former_image)
        #print(imgr)
        #imgr_size=(height(former_image),width(former_image))
        self.canvas.itemconfig(self.ref,image=imgr)
        self.master.update_idletasks()
        time.sleep(0.1)
        self.canvas.itemconfig(self.ref,image=former_image)
        self.function()
    def check_button_image(self):
        #print("type i>>>>",type(i))
        for i in os.listdir(self.path):
            #print("type i>>>>",type(i))
            if self.name[:-4] and 'pressed' in i:
                return True
        return False
        
