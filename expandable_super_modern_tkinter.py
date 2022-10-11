"""
What's up is that 
                there are still some part of the gui that i have not added
                i need to make these exquiste code into a class
                i need to integrate it with my save page code
                furthermore, i need to progress with my corel_draw-like software solution 

"""


from tkinter import *
#from canvasbutton import *
from PIL import ImageTk ,Image
import os
import time
from modern_tkinter import *
count=0
from functools import partial
def do():
    global count
    count+=1
    print(count)

"""
THE CLASS
"""
class SetInterface:
    def __init__(self,path,mainframe_name,master=''):
        self.path=path
        self.count=0
        self.rel_coord_dict={}
        self.image_dict={}
        self.c=master
        self.button_dict={}
        pre_image=Image.open(path+mainframe_name)
        self.place_item(mainframe_name,'',isframe=True)
        
        
        
    #@classmethod
    def prop_size(self,height=100,width=50,image_size=None,frame_size=[200,100]):
        frame_height=frame_size[1]
        frame_width=frame_size[0]
        if image_size:
            height=image_size[1]
            width=image_size[0]
        if frame_height<frame_width:
            fraction=width/height
            height=frame_height
            width=int(height*fraction)
            #print('height')
        else:
            fraction=height/width
            width=frame_width
            height=int(width*fraction)
            #print('width')
        return (width,height)
    def get_item_coord(self,name=None,r_factor=1,start_coord=(0,0),image_size=(120,120)):
        # this may cause problem in the future  >>>>name=name[:-4]
        name=name[:-4]
        y_coord_image_name=None
        x_coord_image_name=None
        for i in os.listdir(path):
            if name in i:
                if name+'_vfit' in i: 
                    y_coord_image_name=i
                if name+'_hfit' in i:
                    #print('hfit>>',i)
                    x_coord_image_name=i
                
        
        dim=(x_coord_image_name,y_coord_image_name)
        #print(y_coord_image_name,x_coord_image_name)
        if y_coord_image_name:
            y_coord_image=Image.open(path+y_coord_image_name)
            y_coord=y_coord_image.size[1]*self.r_factor
        else:
            y_coord=0
        if x_coord_image_name:
            x_coord_image=Image.open(path+x_coord_image_name)
            x_coord=x_coord_image.size[0]*self.r_factor
        else:
            x_coord=0
        d_list=[x_coord+start_coord[0]+image_size[0]/2,y_coord+start_coord[1]+image_size[1]/2]
        #print('street>> ',d_list)
        return d_list
    def place_textbox(self,name,text,frame_name='',n=3,font_detail=['batang',12]):
        global bb
        pre_image=Image.open(self.path+name)
        # proper size
        prop_size=tuple([int(i*self.r_factor) for i in pre_image.size])
        pre_image=pre_image.resize(prop_size)
        
        #pre_image=pre_image.resize(prop_size)

            # proper coord
        prop_coord=self.get_item_coord(name,self.r_factor,self.rel_coord_dict[frame_name],pre_image.size)
        bb=ImageTk.PhotoImage(pre_image)
        # frisk
        font_size=int(int(str(name.split('size_')[1].split(']')[0]))//n)
        #print('prop_coord>>>',prop_coord)
        self.c.create_text(prop_coord,text=text,font=('batang', font_size),tag=name,fill='white')
        font_detail[1]=font_size
        self.c.itemconfig(name,font=tuple(font_detail))
        # item=
        #c.create_image(prop_coord,image=bb)
        
    def place_item(self,name,frame_name='',isframe=False):
        #global pre_image
        pre_image=Image.open(path+name)
        
        if isframe:
            if 'main' in name:
                self.count+=1
                #print(self.count)
                prop_size=self.prop_size(image_size=pre_image.size,frame_size=(cw,ch))
                original_size=pre_image.size
                pre_image=pre_image.resize(prop_size)
                self.r_factor=pre_image.size[0]/original_size[0]
                self.image_dict[name]=ImageTk.PhotoImage(pre_image)
                #print('********cw,ch********',cw,ch)
                
                self.c.create_image(cw/2,ch/2,image=self.image_dict[name],tag=name)

                coord=self.c.coords(name)
                mainframe_rel_coord=[coord[i]-((pre_image.size[i])/2) for i in range(2)]
                self.rel_coord_dict.update({name:mainframe_rel_coord})
                
            else:
                prop_size=tuple([int(i*self.r_factor) for i in pre_image.size])
                pre_image=pre_image.resize(prop_size)

                    # proper coord
                prop_coord=self.get_item_coord(name,self.r_factor,self.rel_coord_dict[frame_name],pre_image.size)
                self.image_dict[name]=ImageTk.PhotoImage(pre_image)
                place_card_frame=self.c.create_image(prop_coord,image=self.image_dict[name],tag=name)

                coord=self.c.coords(place_card_frame)
                place_card_frame_rel_coord=[coord[i]-((pre_image.size[i])/2) for i in range(2)]
                self.rel_coord_dict.update({name:place_card_frame_rel_coord})
                #print("its the other frame")
           
        #name='add_to_cart_button.png'
        else:
                # proper size
            prop_size=tuple([int(i*self.r_factor) for i in pre_image.size])
            pre_image=pre_image.resize(prop_size)

                # proper coord
            prop_coord=self.get_item_coord(name,self.r_factor,self.rel_coord_dict[frame_name],pre_image.size)
            self.image_dict[name]=ImageTk.PhotoImage(pre_image)
            if 'button' in name:
                print(name)
                print('True,button')
                #self.func=partial(CButton,self.c,prop_coord,nam=name,animation='p',master=self.c,image=self.image_dict[name],command=do)
                #self.func.__name__='CButton'
                self.c.create_image(prop_coord,image=self.image_dict[name],tag=name) # item=
                #CanvasButton(self.c,self.c,name,name,do)
                CButton(self.c,prop_coord,animation='p',master=self.c,nam=name,image=self.image_dict[name],command=do)
                
            else:
                print(name)
                print('False,button')
                self.c.create_image(prop_coord,image=self.image_dict[name],tag=name) # item=
        
            #CButton()
            


if __name__=='__main__':
    # the root
    root=Tk()
    root.geometry('900x500')
    root.configure(bg='#EBEBEB',bd=0)
    #root.attributes('-alpha',1)#'#EBEBEB')
    root.attributes('-transparentcolor',"#EBEBEB")#'#EBEBEB')
    #root.attributes('-fullscreen',1)#'#EBEBEB')


    # THE CANVAS
    c_=Canvas(root,bg="#EBEBEB",bd=0,highlightthickness=0)
    c_.pack(fill=BOTH,expand=1)
    c_.update_idletasks()
    ch=root.winfo_height()
    cw=root.winfo_width()
    #c.create_rectangle(20,20,220,220)
    # path
    path=os.path.abspath(os.path.dirname(__file__))+'/gui_resource/'

    # instantiating the class
    s=SetInterface(path,'mainframe_background_picture_.png',master=c_)

    # THE GREEN PLACADE
    s.place_item('green_placade.png',frame_name="mainframe_background_picture_.png")
    # THE EXPOLRE BUTTON
    s.place_item('explore_button.png',frame_name="mainframe_background_picture_.png")
    #ACHI PSEUDO
    s.place_item('archi_pseudo.png',frame_name="mainframe_background_picture_.png")
    # PREVIOUS BUTTON
    s.place_item('prev_page_button.png',frame_name="mainframe_background_picture_.png")

    # NEXT BUTTON
    s.place_item('next_page_button.png',frame_name="mainframe_background_picture_.png")

    # # MENU BAR
    s.place_item('menu_bar_image.png',frame_name="mainframe_background_picture_.png")

    # search box
    s.place_item('search_box.png',frame_name="mainframe_background_picture_.png")
    
    #search_button    
    s.place_item('search_button.png',frame_name="mainframe_background_picture_.png")

    # bin_button
    s.place_item('bin_button.png',frame_name="mainframe_background_picture_.png")

    # avatar

    s.place_item('avatar.png',frame_name="mainframe_background_picture_.png")

    # place card frame
    s.place_item('place_card_frame.png',isframe=True,frame_name="mainframe_background_picture_.png")
                                    
    # place_card_detail
    s.place_item('place_card_detail.png',frame_name="place_card_frame.png")

    # place_card_image
    s.place_item('place_card_image.png',frame_name="place_card_frame.png")

    #add_to_cart_button
    s.place_item('add_to_cart_button.png',frame_name="place_card_frame.png")

    # page indicators
    s.place_item('page_indicator_frame.png',isframe=True,frame_name="mainframe_background_picture_.png")
    s.place_item('passive_page_indicator3.png',frame_name='page_indicator_frame.png')
    s.place_item('passive_page_indicator2.png',frame_name='page_indicator_frame.png')
    s.place_item('passive_page_indicator1.png',frame_name='page_indicator_frame.png')
    
    s.place_item('active_page_indicator.png',frame_name='page_indicator_frame.png')
    

    # TEXT PART
    #add to cart button
    s.place_textbox('add_to_basket_[in_place_card__size_17].png',
                  'Add to basket',frame_name="place_card_frame.png")
    #price
    
    s.place_textbox('price_[in_place_card__size_17].png','price:75',frame_name="place_card_frame.png",n=2)
        # details text
    text='beautiful garden flower \nfrom the verse'
    # frask
    s.place_textbox('place_card_detail_[in_place_card__size_17].png',text,frame_name="place_card_frame.png",n=2)
    # explore_more_[in_placade__size_23]
        # Explore more
    s.place_textbox('explore_more_[in_placade__size_23].png','Explore more'.upper(),frame_name="mainframe_background_picture_.png",n=2)
    
    # detail_[in_placade__size_23]
        # details_text
    text="""
Investing in good garden flower, adds 
value on the long run. a good garden
helps beautify the house. supply 
fresh oxygen,and also serve as food
crop.
"""
    s.place_textbox('detail_[in_placade__size_23].png',text,frame_name="mainframe_background_picture_.png",n=2)
    
    s.place_textbox('about_us_[in_menubar__size_21].png','about us'.title(),frame_name="mainframe_background_picture_.png",n=2.5)    

    s.place_textbox('architecture_[in_placade__size_91].png','Holticulture',frame_name="mainframe_background_picture_.png",n=2)
    
    s.place_textbox('interior_[in_placade__size_21].png','interior'.upper(),frame_name="mainframe_background_picture_.png",n=2)

    # search_[in_menubar__size_21]
    s.place_textbox('search_[in_menubar__size_21].png','Search',frame_name="mainframe_background_picture_.png",n=2.5)

    #about_us_[in_menubar__size_21]
    s.place_textbox('shop_[in_menubar__size_21].png','Shop',frame_name="mainframe_background_picture_.png",n=2.5)


    # explore_[in_menubar__size_21]
    s.place_textbox('explore_[in_menubar__size_21].png','Explore',frame_name="mainframe_background_picture_.png",n=2.5)

    # home_[in_menubar__size_21]
    s.place_textbox('home_[in_menubar__size_21].png','Home',frame_name="mainframe_background_picture_.png",n=2.5, font_detail=['batang',12,'bold'])

    # agroville_[in_text__size_18]
    s.place_textbox('agroville_[in_text__size_18].png','Agro\n&Agroville',frame_name="mainframe_background_picture_.png",n=2, font_detail=['Calisto MT',12,'bold'])

    c_.delete('page_indicator_frame.png')
    root.overrideredirect(True)
    root.mainloop()




"""
 THE RESULT >>> still in production ... thANKS for watching, 
"""

