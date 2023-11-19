
# Aditi Goyal
# Read_Easy: Library Manager

import pymysql
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

conn = pymysql.connect(host = "localhost", user = "*****", password = "*****", database = "Read_Easy")
curs = conn.cursor()

root = Tk()
root.title("Read Easy: Aditi Goyal")
root.minsize(width = 400, height = 400)
root.geometry("600x500")

same = True
n = 0.52

# For Adding a Background Image
backg_image = Image.open("read_easy_lib.jpg")
[ImageSizeWidth, ImageSizeHeight] = backg_image.size

ImageSizeWidth_new = int(ImageSizeWidth*n)
if same:
    ImageSizeHeight_new = int(ImageSizeHeight*n) 
else:
    ImageSizeHeight_new = int(ImageSizeHeight/n) 
    
backg_image = backg_image.resize((ImageSizeWidth_new, ImageSizeHeight_new),Image.Resampling.LANCZOS)
imag = ImageTk.PhotoImage(backg_image)

Cnv1 = Canvas(root)

Cnv1.create_image(340, 340, image = imag)      
Cnv1.config(bg = "white", width = ImageSizeWidth_new, height = ImageSizeHeight_new)
Cnv1.pack(expand = True, fill = BOTH)

headFrame1 = Frame(root, bg = "#FFBB00", bd = 3)
headFrame1.place(relx = 0.2, rely = 0.1, relwidth = 0.6, relheight = 0.16)

headLabel = Label(headFrame1, text = "Welcome to \n Read Easy \n Library", bg = 'lightsalmon', fg = 'black', font = ('Arial', 14))
headLabel.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

button1 = Button(root, text = "Add Book Details", bg = 'aliceblue', fg = 'black', command = book_add)
button1.place(relx = 0.65, rely = 0.4, relwidth = 0.3, relheight = 0.08)
    
button2 = Button(root, text = "Delete Book", bg = 'aliceblue', fg = 'black', command = delete)
button2.place(relx = 0.65, rely = 0.5, relwidth = 0.3, relheight = 0.08)
    
button3 = Button(root, text = "View Books", bg = 'aliceblue', fg = 'black', command = books_view)
button3.place(relx = 0.65, rely = 0.6, relwidth = 0.3, relheight = 0.08)
    
button4 = Button(root, text = "Issue Book to Patron", bg = 'aliceblue', fg = 'black', command = issueBook)
button4.place(relx = 0.65, rely = 0.7, relwidth = 0.3, relheight = 0.08)
    
button5 = Button(root, text = "Return Book to Library", bg = 'aliceblue', fg = 'black', command = returnBook)
button5.place(relx = 0.65, rely = 0.8, relwidth = 0.3, relheight = 0.08)

root.mainloop()

# End of Main Module
