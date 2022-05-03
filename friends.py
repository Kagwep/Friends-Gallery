import tkinter
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os,shutil
from tkinter.messagebox import askyesno,showinfo
from collections import OrderedDict
import random


win = tkinter.Tk()

lbl=tkinter.Label(win,text="   Action panel  ",bg='sea green')
lbl.grid(column=1,row=0,sticky = "nsew",columnspan=5)

win.title("My Friends Gallery")
win.geometry("1300x700")
frame1 = tkinter.Frame(win, padx=5, pady=(5),bg="light sky blue")
frame1.grid(row=2, column=1,columnspan=6, pady=(10,10),padx=(10,10))
frame2 = tkinter.Frame(win, padx=5, pady=(5),bg="light sky blue")
frame2.grid(row=2, column=1,columnspan=6, pady=(10,10),padx=(10,10))
labellist = []
labell = []
def ExitWindow():
    win.destroy()
def showImage(event):
    list1 = os.listdir("images")
    if len(list1) !=0:
        image_show = random.choice(list1)
        image_s = Image.open('images/'+ image_show)
        photo_s = ImageTk.PhotoImage(image_s)
        label_s = tkinter.Label(frame2, image=photo_s, text = image_show,compound='top', borderwidth=5 ,relief="ridge")
        label_s.image = photo_s
        label_s.grid(row=2,column=5,padx=(10, 10),pady = (10,10))
        labell.append(label_s)
        
    
    
def ShowGallery():

    list1 = os.listdir("images")
    print(list1)
    row_default = 2
    column_default = 1
    for element in list1:
    
        print(column_default)
        key = list1.index(element)
        image = Image.open('images/'+ element)
        photo = ImageTk.PhotoImage(image)
        label = tkinter.Label(frame1, image=photo, text = element,compound='top', borderwidth=5 ,relief="ridge")
        label.image = photo
        label.grid(row=row_default,column=column_default,padx=(10, 10),pady = (10,10))
        labelname= str(label.grid(row=row_default,column=column_default,padx=(10, 10),pady = (10,10)))
        labellist.append(label)
        
    
        column_default +=1
        check = column_default % 6
        if check == 0:
            row_default += 2
            column_default = 1
    print(labellist)
    

        
            
def AddFriend():
    filetypes = (
        ('image files', '*.JPG', '.png'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if filename != '':
        
        answer = askyesno(
           title = 'Add friend',
           message = 'Add friend '+ filename+ ' to friends Gallery'
           

           )
        if answer:
            file_name = filename
            shutil.copy(file_name, 'images')
            showinfo(
               title='Friend added',
               message=filename + ' Added to friends Gallery'
              )
    
    ShowGallery()

def DeleteFriend():
    filetypes = (
        ('image files', '*.JPG', '.png'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='images',
        filetypes=filetypes)
    if filename != '':
        answer1 = askyesno(
           title = 'Delet friend',
           message = 'Delete friend \n'+ filename

            )
        if answer1:
            os.remove(filename)
            for label in labellist:
                lab_text = label.cget("text")
                if lab_text in filename:
                    label.grid_forget()
            ShowGallery()
            showinfo(
               title='Deleted',
               message= 'friend ' + filename + 'deleted'
             )
    
    
            
def ClearGallery():
    list2 = os.listdir("images")
    for item in list2:
        os.remove('images/'+item)
        for label in labellist:
            lab_text = label.cget("text")
            if lab_text in item:
                label.grid_forget()
    ShowGallery()
   

   
b1 = tkinter.Button(win, text = "Show pictures",bg='light sky blue',command=ShowGallery)
b1.bind('<Double-1>', showImage) 
b2 = tkinter.Button(win, text = "Clear Gallery",bg='light sky blue',command=ClearGallery)
b3 = tkinter.Button(win, text = "Delete a friend",command=DeleteFriend,bg='light sky blue')
b4 = tkinter.Button(win, text = "Add New Friend", command=AddFriend,bg='light sky blue')
b5 = tkinter.Button(win, text = "Quit",bg='light sky blue',command=ExitWindow)
                    
b1.grid(row = 1, column = 1,sticky = "nsew")
b2.grid(row = 1, column = 2,sticky = "nsew")
b3.grid(row = 1, column = 3,sticky = "nsew")
b4.grid(row = 1, column = 4,sticky = "nsew")
b5.grid(row = 1, column = 5,sticky = "nsew")



ShowGallery()
win.configure(bg='blue')     
win.mainloop()
