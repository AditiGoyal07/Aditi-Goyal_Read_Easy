
# Aditi Goyal

import pymysql
from PIL import ImageTk,Image
from tkinter import *
from tkinter import messagebox

conn = pymysql.connect(host="localhost",user="*****",password="*****",database="Read_Easy")
curs = conn.cursor()

Issue_table = "books_issued"
Book_table = "books"

allBookIDs = []

def book_return():
    
    global SbmtButton,frameLabel,label1,Info1,QuitButton,root,Cnv1,bookstatus
    
    bookid = Info1.get()

    BookID_extract = "select book_id from "+Issue_table

    try:
        curs.execute(BookID_extract)
        conn.commit()
        for i in curs:
            allBookIDs.append(i[0])
        
        if bookid in allBookIDs:
            avail_check = "select book_status from "+Book_table+" where book_id = '"+bookid+"'"
            curs.execute(avail_check)
            conn.commit()
            for i in curs:
                check = i[0]
                
            if check == 'issued':
                bookstatus = True
            else:
                bookstatus = False

        else:
            messagebox.showinfo("Error","Book ID is not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
    issue_delete = "delete from "+Issue_table+" where book_id = '"+bookid+"'"
  
    print(bookid in allBookIDs)
    print(bookstatus)

    status_update = "update "+Book_table+" set book_status = 'avail' where book_id = '"+bookid+"'"
    try:
        if bookid in allBookIDs and bookstatus == True:
            curs.execute(issue_delete)
            conn.commit()
            curs.execute(status_update)
            conn.commit()
            messagebox.showinfo('Success',"Returned book successfully!")
        else:
            allBookIDs.clear()
            messagebox.showinfo('Message',"Please check Book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, try again")
    
    
    allBookIDs.clear()
    root.destroy()
    
def returnBook(): 
    
    global Info1,SbmtButton,QuitButton,Cnv1,conn,curs,root,frameLabel, label1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Cnv1 = Canvas(root)
    
    Cnv1.config(bg="skyblue")
    Cnv1.pack(expand=True,fill=BOTH)
        
    headFrame1 = Frame(root,bg="black",bd=1)
    headFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headLabel = Label(headFrame1, text="Return Book", bg='lightsalmon', fg='black', font=('Arial',14))
    headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    frameLabel = Frame(root,bg='black')
    frameLabel.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    label1 = Label(frameLabel,text="Book ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.5)
        
    Info1 = Entry(frameLabel)
    Info1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    SbmtButton = Button(root,text="Return",bg='#f7f1e3', fg='black',command=book_return)
    SbmtButton.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    QuitButton = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    QuitButton.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()