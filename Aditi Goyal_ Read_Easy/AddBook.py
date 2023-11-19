
# Aditi Goyal

import pymysql
from PIL import ImageTk,Image
from tkinter import *
from tkinter import messagebox

def register_book():
    
    bookid = Info1.get()
    booktitle = Info2.get()
    bookauthor = Info3.get()
    bookstatus = Info4.get()
    bookstatus = bookstatus.lower()
    
    book_insert = "insert into " + Book_table + " values('" + bookid + "','" + booktitle + "','" + bookauthor + "','" + bookstatus + "')"
    try:
        curs.execute(book_insert)
        conn.commit()
        messagebox.showinfo("Success", "Added book successfully!")
    except:
        messagebox.showinfo("Error", "Can't add data into database")
    
    root.destroy()
    
def book_add(): 
    
    global Info1, Info2, Info3, Info4, Cnv1, conn, curs, Book_table, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width = 400, height = 400)
    root.geometry("600x500")

    conn = pymysql.connect(host = "localhost", user = "*****", password = "*****", database = "Read_Easy")
    curs = conn.cursor()

    Book_table = "books"

    Cnv1 = Canvas(root)
    Cnv1.config(bg = "skyblue")
    Cnv1.pack(expand = True, fill = BOTH)
        
    headFrame1 = Frame(root, bg = "black", bd = 1)
    headFrame1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)

    headLabel = Label(headFrame1, text = "Add Books", bg = 'lightsalmon', fg = 'black', font = ('Arial', 14))
    headLabel.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    frameLabel = Frame(root, bg = 'black')
    frameLabel.place(relx = 0.1, rely = 0.4, relwidth = 0.8, relheight = 0.4)
        
    # Book ID
    label1 = Label(frameLabel, text = "Book ID: ", bg = 'black', fg = 'white')
    label1.place(relx = 0.05, rely = 0.2, relheight = 0.08)
        
    Info1 = Entry(frameLabel)
    Info1.place(relx = 0.3, rely = 0.2, relwidth = 0.62, relheight = 0.08)
        
    # Book title
    label2 = Label(frameLabel, text = "Book Title: ", bg = 'black', fg = 'white')
    label2.place(relx = 0.05, rely = 0.35, relheight = 0.08)
        
    Info2 = Entry(frameLabel)
    Info2.place(relx = 0.3, rely = 0.35, relwidth = 0.62, relheight = 0.08)
        
    # Author
    label3 = Label(frameLabel, text = "Book Author: ", bg = 'black', fg = 'white')
    label3.place(relx = 0.05, rely = 0.50, relheight = 0.08)
        
    Info3 = Entry(frameLabel)
    Info3.place(relx = 0.3, rely = 0.50, relwidth = 0.62, relheight = 0.08)
        
    # Status
    label4 = Label(frameLabel, text = "Status(Avail/issued): ", bg = 'black', fg = 'white')
    label4.place(relx = 0.05, rely = 0.65, relheight = 0.08)
        
    Info4 = Entry(frameLabel)
    Info4.place(relx = 0.3, rely = 0.65, relwidth = 0.62, relheight = 0.08)
        
    # Submit button
    SbmtButton = Button(root, text = "SUBMIT", bg = '#f7f1e3', fg = 'black', command = register_book)
    SbmtButton.place(relx = 0.28, rely = 0.9, relwidth = 0.18, relheight = 0.08)
    
    # Quit button
    QuitButton = Button(root, text = "Quit", bg = 'white', fg = 'black', command = root.destroy)
    QuitButton.place(relx = 0.53, rely = 0.9, relwidth = 0.18, relheight = 0.08)
    
    root.mainloop()