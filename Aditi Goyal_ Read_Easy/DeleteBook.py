
# Aditi Goyal

import pymysql
from PIL import ImageTk,Image
from tkinter import *
from tkinter import messagebox

conn = pymysql.connect(host="localhost",user="*****",password="*****",database="Read_Easy")
curs = conn.cursor()

Issue_table = "books_issued" 
Book_table = "books"

def delete_book():
    
    bookid = Info1.get()
    print(bookid)

    book_delete = "delete from "+Book_table+" where book_id = '"+bookid+"'"
    issue_delete = "delete from "+Issue_table+" where book_id = '"+bookid+"'"
    try:
        curs.execute(book_delete)
        conn.commit()
        curs.execute(issue_delete)
        conn.commit()
        messagebox.showinfo("Success","Deleted book data successfully!")
    except:
        messagebox.showinfo("Error", "Please check Book ID")

    Info1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global Info1,Cnv1,conn,curs,Book_table,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Cnv1 = Canvas(root)
    
    Cnv1.config(bg="skyblue")
    Cnv1.pack(expand=True,fill=BOTH)
        
    headFrame1 = Frame(root,bg="black",bd=1)
    headFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headLabel = Label(headFrame1, text="Delete Book", bg='lightsalmon', fg='black', font=('Arial',14))
    headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    frameLabel = Frame(root,bg='black')
    frameLabel.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    label2 = Label(frameLabel,text="Book ID : ", bg='black', fg='white')
    label2.place(relx=0.05,rely=0.5)
        
    Info1 = Entry(frameLabel)
    Info1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    SbmtButton = Button(root,text="SUBMIT",bg='#f7f1e3', fg='black',command=delete_book)
    SbmtButton.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    QuitButton = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    QuitButton.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()