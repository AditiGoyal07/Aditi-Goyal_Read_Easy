
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

def book_issue():
    
    global IssueButton,frameLabel,label1,inf1,inf2,QuitButton,root,Cnv1,bookstatus
    
    bookid = inf1.get()
    issueto = inf2.get()

    IssueButton.destroy()
    frameLabel.destroy()
    label1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    extractBid = "select book_id from "+Book_table+ ";"
    try:
        curs.execute(extractBid)
        conn.commit()
        for i in curs:
            allBookIDs.append(i[0])
        
        if bookid in allBookIDs:
            avail_check = "select book_status from "+Book_table+" where book_id = '"+bookid+"';"
            curs.execute(avail_check)
            conn.commit()
            for i in curs:
                check = i[0]
                
            if check == 'avail':
                bookstatus = True
            else:
                bookstatus = False

        else:
            messagebox.showinfo("Error","Book ID is not present")
    except Exception as e:
        print(e)
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issue_insert = "insert into "+Issue_table+" values ('"+bookid+"','"+issueto+"')"

    status_update = "update "+Book_table+" set book_status = 'issued' where book_id = '"+bookid+"'"
    try:
        if bookid in allBookIDs and bookstatus == True:
            curs.execute(issue_insert)
            conn.commit()
            curs.execute(status_update)
            conn.commit()

            messagebox.showinfo("Success","Issued book successfully!")
            root.destroy()
        else:
            allBookIDs.clear()
            messagebox.showinfo("Message","Book already issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bookid)
    print(issueto)
    
    allBookIDs.clear()
    
def issueBook(): 
    
    global IssueButton,frameLabel,label1,inf1,inf2,QuitButton,root,Cnv1,bookstatus
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Cnv1 = Canvas(root)
    Cnv1.config(bg="skyblue")
    Cnv1.pack(expand=True,fill=BOTH)

    headFrame1 = Frame(root,bg="black",bd=1)
    headFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headLabel = Label(headFrame1, text="Issue Book", bg='lightsalmon', fg='black', font=('Arial',14))
    headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    frameLabel = Frame(root,bg='black')
    frameLabel.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    label1 = Label(frameLabel,text="Book ID: ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(frameLabel)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    label2 = Label(frameLabel,text="Issued To: ", bg='black', fg='white')
    label2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(frameLabel)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    # Issue Button
    IssueButton = Button(root,text="ISSUE",bg='#f7f1e3', fg='black',command=book_issue)
    IssueButton.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    QuitButton = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    QuitButton.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
