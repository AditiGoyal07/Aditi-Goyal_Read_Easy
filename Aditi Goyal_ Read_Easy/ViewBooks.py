
# Aditi Goyal

import pymysql
from PIL import ImageTk,Image
from tkinter import *
from tkinter import messagebox

conn = pymysql.connect(host="localhost",user="*****",password="*****",database="Read_Easy")
curs = conn.cursor()

Book_table = "books" 
    
def books_view(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Cnv1 = Canvas(root) 
    Cnv1.config(bg="skyblue")
    Cnv1.pack(expand=True,fill=BOTH)
        
    headFrame1 = Frame(root,bg="black",bd=1)
    headFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headLabel = Label(headFrame1, text="View Books", bg='lightsalmon', fg='black', font=('Arial',14))
    headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    frameLabel = Frame(root,bg='black')
    frameLabel.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(frameLabel, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(frameLabel, text="------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    booksget = "select * from "+Book_table
    try:
        curs.execute(booksget)
        conn.commit()
        for i in curs:
            Label(frameLabel, text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    QuitButton = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    QuitButton.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()