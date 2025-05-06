from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from employee import employeeClass
from customer import customerClass
from categroy1 import categoryClass
from product1  import Productclass
from vehicls  import vehicleClass
class GSP:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #===title===
        self.icon_title=PhotoImage(file="")
        title=Label(self.root,text="Gas cylinder Service Provider",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="lightblue",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #===Left Menu===
        

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        

        btn_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_customer=Button(LeftMenu,text="Customer",command=self.coustomer,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category1,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product1,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_vichel=Button(LeftMenu,text="Vehicles",command=self.vehicls,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


     #===Content===

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_customerr=Label(self.root,text="Total Customer\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_customerr.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Connection\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_vehicle=Label(self.root,text="Total vehicle\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_vehicle.place(x=650,y=300,height=150,width=300)
        
        #===footer===
        lbl_footer=Label(self.root,text="Gas cylinder Service Provider",font=("times new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
    
    #==========================================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
    def coustomer(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=customerClass(self.new_win) 
        
    def category1(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)    
    
    def product1(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Productclass(self.new_win)    
           
    def vehicls(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=vehicleClass(self.new_win)    
           
                  
        
if __name__ =="__main__":
    root=Tk()
    obj=GSP(root)
    root.mainloop()