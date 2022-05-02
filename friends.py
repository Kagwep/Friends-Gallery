import tkinter
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os,shutil
from tkinter.messagebox import askyesno,showinfo

win = tkinter.Tk()
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
            showinfo(
               title='Deleted',
               message= 'friend ' + filename + 'deleted'
             )
   
lbl=tkinter.Label(win,text="   Action panel  ")
lbl.grid(column=1,row=0,sticky = "nsew")

win.title("My Friends Gallery")
win.geometry("700x350")

b1 = tkinter.Button(win, text = "Show pictures")
b2 = tkinter.Button(win, text = "Clear Gallery")
b3 = tkinter.Button(win, text = "Delete a friend",command=DeleteFriend)
b4 = tkinter.Button(win, text = "Add New Friend", command=AddFriend)
b5 = tkinter.Button(win, text = "Quit")
                    
b1.grid(row = 1, column = 1,sticky = "nsew")
b2.grid(row = 1, column = 2,sticky = "nsew")
b3.grid(row = 1, column = 3,sticky = "nsew")
b4.grid(row = 1, column = 4,sticky = "nsew")
b5.grid(row = 1, column = 5,sticky = "nsew")



list1 = os.listdir("images")

# Run the above function and store its results in a variable.   

print(list1)
row_default = 2
column_default = 1
for element in list1:
   print(column_default)
   key = list1.index(element)
   image = Image.open('images/'+ element)
   photo = ImageTk.PhotoImage(image)
   label = tkinter.Label(win, image=photo, text = element,compound='top', borderwidth=5 )
   label.image = photo
   label.grid(row=row_default,column=column_default,padx=(10, 10),pady = (10,10))
   column_default +=1
   check = column_default % 6
   if check == 0:
      row_default += 2
      column_default = 1
      
win.mainloop()
