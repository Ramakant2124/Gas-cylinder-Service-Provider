from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class vehicleClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()
       
        self.var_vehicl_name=StringVar()
        self.var_vehicl_no=StringVar()
        self.var_driver_name=StringVar()
       
       
        title=Label(self.root,text="Vehicls Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=10,y=10,width=1100,height=50)
 
        lbl_vehicl_name=Label(self.root,text="Vehicls Name",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_vehicl_no=Label(self.root,text="Vehicls No",font=("goudy old style",15),bg="white").place(x=50,y=200)
        lbl_driver_name=Label(self.root,text="Driver Name",font=("goudy old style",15),bg="white").place(x=50,y=250)
        
        txt_vehicl_name=Entry(self.root,textvariable=self.var_vehicl_name,font=("goudy old style",15),bg="lightyellow").place(x=250,y=150,width=180)
        txt_vehicl_no=Entry(self.root,textvariable=self.var_vehicl_no,font=("goudy old style",15),bg="lightyellow").place(x=250,y=200,width=180)
        txt_driver_name=Entry (self.root,textvariable=self.var_driver_name,font=("goudy old style",15),bg="lightyellow").place(x=250,y=250,width=180)
        
        
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=50,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=250,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=50,y=350,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=250,y=350,width=110,height=28)
        
         #=========product detels
        
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)
        
        self.vehiclTable=ttk.Treeview(p_frame,columns=("vehicl_name","vehicl_no","driver_name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.vehiclTable.xview)
        scrolly.config(command=self.vehiclTable.yview)
        self.vehiclTable.heading("vehicl_name",text="Vehicl Name")
        self.vehiclTable.heading("vehicl_no",text="Vehicl No")
        self.vehiclTable.heading("driver_name",text="Driver Name")
        
        self.vehiclTable["show"]="headings"
        
        self.vehiclTable.column("vehicl_name",width=90)
        self.vehiclTable.column("vehicl_no",width=100)
        self.vehiclTable.column("driver_name",width=100)
       
       
        
        self.vehiclTable.pack(fill=BOTH,expand=1)
        self.vehiclTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
        
        
        
        
        #=================================================================================================
    def add(self): 
         con=sqlite3.connect(database=r'gsps.db')
         cur=con.cursor()
         try:
          if self.var_vehicl_no.get()=="":
            messagebox.showerror("Error","Vehicl NO  Must be required",parent=self.root)
          else:
            cur.execute("Select * from vehicl where vehicl_no=?",(self.var_vehicl_no.get(),))
            row=cur.fetchone()
            if row!=None:
              messagebox.showerror("Error","This Vehicl No already assigned,try different",parent=self.root)
            else:
                cur.execute("Insert into vehicl (vehicl_name,vehicl_no,driver_name) values(?,?,?)",(
                                    self.var_vehicl_name.get(),
                                    self.var_vehicl_no.get(),
                                    self.var_driver_name.get(),
                                    
                ))  
                con.commit()
                messagebox.showinfo("Success","Vehicl Addedd Successfully",parent=self.root)
                self.show()
         except Exception as ex:
              messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
         
         
    def show(self):
      con=sqlite3.connect(database=r'gsps.db')
      cur=con.cursor()
      try:
        cur.execute("select * from vehicl")
        rows=cur.fetchall()
        self.vehiclTable.delete(*self.vehiclTable.get_children())
        for row in rows:
          self.vehiclTable.insert('',END,values=row)
        
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def get_data(self,ev):
        f=self.vehiclTable.focus()
        content=(self.vehiclTable.item(f))
        row=content['values'] 
          
        self.var_vehicl_name.set(row[0])
        self.var_vehicl_no.set(row[1])
        self.var_vehicl_name.set(row[2])
        
        
           
    def update(self): 
      con=sqlite3.connect(database=r'gsps.db')
      cur=con.cursor()
      try:
          if self.var_vehicl_no.get()=="":
            messagebox.showerror("Error","Vehicl No Must be required",parent=self.root)
          else:
            cur.execute("Select * from vehicl where vihicl_no=?",(self.var_vehicl_no.get(),))
            row=cur.fetchone()
            if row==None:
              messagebox.showerror("Error","Invalide Vehicls No",parent=self.root)
            else:
                cur.execute("Update vehicl set vehicl_name=?,driver_name=? where vihicl_no=?=?",(
                                    
                                    self.var_vehicl_name.get(),
                                    self.var_driver_name.get(),
                                    self.var_vehicl_no.get(),
                ))  
                con.commit()
                messagebox.showinfo("Success","Vehicl updated Successfully",parent=self.root)
                self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
         
    
    def delete(self):
      con=sqlite3.connect(database=r'gsps.db')
      cur=con.cursor()
      try:
          if self.var_vehicl_no.get()=="":
            messagebox.showerror("Error","Vehicl No Must be required",parent=self.root)
          else:
            cur.execute("Select * from vehicl where vihicl_no=?",(self.var_vehicl_no.get(),))
            row=cur.fetchone()
            if row==None:
              messagebox.showerror("Error","Invalide Vehicl No",parent=self.root)
            else:
                op=messagebox.askyesno("Confirim","Do you really want to delete?",parent=self.root)
                if op==True:
                   cur.execute("delete from vehicl where vihicl_no=?",(self.var_vehicl_no.get(),))
                   con.commit()
                   messagebox.showinfo("Delete","Vehicl Delete successfully",parent=self.root)
                   self.clear()
        
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
    
    def clear(self):
        self.var_vehicl_no.set("")
        self.var_vehicl_name.set("")
        self.var_driver_name.set("")
       
        self.show()
    
    
              
        
if __name__=="__main__":
    
   root=Tk()
   obj=vehicleClass(root)
   root.mainloop()           