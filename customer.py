from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class customerClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()
        #=========================
        #  All variables======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_cus_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_area=StringVar()
        self.var_city=StringVar()
       
        #====searchfram====
        SearchFrame=LabelFrame(self.root,text="Search customer",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
      #====options===
        cmb_search=ttk.Combobox (SearchFrame,textvariable=self.var_searchby,values=("select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_Search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_Search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        
        #=====title===
        title=Label(self.root,text=" Customer Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        
        #=====conetent======
        #====row1=====
        lbl_cuside=Label(self.root,text="Cus ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)
        
        txt_cusid=Entry(self.root,textvariable=self.var_cus_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox (self.root,textvariable=self.var_gender,values=("select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
        
        #=======row 2=======
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_area=Label(self.root,text="Area",font=("goudy old style",15),bg="white").place(x=750,y=190)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_area=Entry(self.root,textvariable=self.var_area,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
        
        #=======row 3 =======
        lbl_city=Label(self.root,text="City",font=("goudy old style",15),bg="white").place(x=50,y=230)
        
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
       
      
        #===buttons===
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)
        
        #===Customer Details===
        
        cus_frame=Frame(self.root,bd=3,relief=RIDGE)
        cus_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly=Scrollbar(cus_frame,orient=VERTICAL)
        scrollx=Scrollbar(cus_frame,orient=HORIZONTAL)
        
        self.CustomerTable=ttk.Treeview(cus_frame,columns=("cid","name","email","gender","contact","area","city",),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)
        self.CustomerTable.heading("cid",text="cus ID")
        self.CustomerTable.heading("name",text="Name")
        self.CustomerTable.heading("email",text="Email")
        self.CustomerTable.heading("gender",text="Gender")
        self.CustomerTable.heading("contact",text="Contact")
        self.CustomerTable.heading("area",text="Area")
        self.CustomerTable.heading("city",text="City")
        
        
        self.CustomerTable["show"]="headings"
        
        self.CustomerTable.column("cid",width=90)
        self.CustomerTable.column("name",width=100)
        self.CustomerTable.column("email",width=100)
        self.CustomerTable.column("gender",width=100)
        self.CustomerTable.column("contact",width=100)
        self.CustomerTable.column("area",width=100)
        self.CustomerTable.column("city",width=100)
        
        
        self.CustomerTable.pack(fill=BOTH,expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
     #==========================================================================================================================   
    
    def add(self): 
      con=sqlite3.connect(database=r'gsps.db')
      cur=con.cursor()
      try:
          if self.var_cus_id.get()=="":
            messagebox.showerror("Error","Customer ID Must be required",parent=self.root)
          else:
            cur.execute("Select * from Customer where cid=?",(self.var_cus_id.get(),))
            row=cur.fetchone()
            if row!=None:
              messagebox.showerror("Error","This Customer ID already assigned,try different",parent=self.root)
            else:
                cur.execute("Insert into Customer (cid,name,email,gender,contact,area,city) values(?,?,?,?,?,?,?)",(
                                    self.var_cus_id.get(),
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_area.get(),
                                    self.var_city.get(),
                                    
                ))  
                con.commit()
                messagebox.showinfo("Success","Customer Addedd Successfully",parent=self.root)
                self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
         
         
    def show(self):
      con=sqlite3.connect(database=r'gsps.db')
      cur=con.cursor()
      try:
        cur.execute("select * from Customer")
        rows=cur.fetchall()
        self.CustomerTable.delete(*self.CustomerTable.get_children())
        for row in rows:
          self.CustomerTable.insert('',END,values=row)
        
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def get_data(self,ev):
        f=self.CustomerTable.focus()
        content=(self.CustomerTable.item(f))
        row=content['values'] 
          
        self.var_cus_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_area.set(row[5])
        self.var_city.set(row[6])
        
        
           
    def update(self): 
      con=sqlite3.connect(database=r'gsps.db')
      cur=con.cursor()
      try:
          if self.var_cus_id.get()=="":
            messagebox.showerror("Error","Customer ID Must be required",parent=self.root)
          else:
            cur.execute("Select * from Customer where cid=?",(self.var_cus_id.get(),))
            row=cur.fetchone()
            if row==None:
              messagebox.showerror("Error","Invalide Customer ID",parent=self.root)
            else:
                cur.execute("Update Customer set name=?,email=?,gender=?,contact=?,area=?,city=? where cid=?",(
                                    
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_area.get(),
                                    self.var_city.get(),
                                    self.var_cus_id.get(),
                ))  
                con.commit()
                messagebox.showinfo("Success","Customer updated Successfully",parent=self.root)
                self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
         
    
    def delete(self):
      con=sqlite3.connect(database=r'gsps.db')
      cur=con.cursor()
      try:
          if self.var_cus_id.get()=="":
            messagebox.showerror("Error","Customer ID Must be required",parent=self.root)
          else:
            cur.execute("Select * from Customer where cid=?",(self.var_cus_id.get(),))
            row=cur.fetchone()
            if row==None:
              messagebox.showerror("Error","Invalide Customer ID",parent=self.root)
            else:
                op=messagebox.askyesno("Confirim","Do you really want to delete?",parent=self.root)
                if op==True:
                   cur.execute("delete from Customer where cid=?",(self.var_cus_id.get(),))
                   con.commit()
                   messagebox.showinfo("Delete","Customer Delete successfully",parent=self.root)
                   self.clear()
        
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
    
    def clear(self):
        self.var_cus_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_area.set("")
        self.var_city.set("")
        self.show()
    
    def search(self):
       con=sqlite3.connect(database=r'gsps.db')
       cur=con.cursor()
       try:
           if self.var_searchby.get()=="Select":
            messagebox.showerror("Error","Select Search By option",parent=self.root)
           elif self.var_searchtxt.get()=="":  
            messagebox.showerror("Error","Search input should be required",parent=self.root)
           else:
              cur.execute("select * from Customer Where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                 self.CustomerTable.delete(*self.CustomerTable.get_children())
                 for row in rows:
                    self.CustomerTable.insert('',END,values=row)
        
       except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 
        
if __name__=="__main__":
    
   root=Tk()
   obj=customerClass(root)
   root.mainloop()    