from tkinter import filedialog,messagebox
from tkinter import *
import smtplib,ssl
import os,sys
import hashlib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from PIL import Image,ImageTk
tk = Tk()
import requests
tk.geometry("1000x650")
tk.title("Desktop Mail")

class Login:
    def __init__(self):
        self.drawLogin()
        
    def drawLogin(self):
        maintext = Label(tk,text = "LOGIN",font=("COURIER",40))
        maintext.pack()
        frame1 = Frame(tk)
        label1 = Label(frame1,text="EMAIL",font=("COURIER",20))
        self.email = Text(frame1,font=("COURIER",20),height=1,width=50)
        label2 = Label(frame1,text="PASSWORD",font=("COURIER",20))
        self.password = Text(frame1,font=("COURIER",20),height=1,width=50)
        label1.grid(row=0,column = 0,pady=20)
        self.email.grid(row=0,column = 1)
        label2.grid(row=1,column = 0)
        self.password.grid(row=1,column = 1)
        frame2 = Frame(tk)
        button = Button(frame2,text="LOGIN" ,font=("COURIER",20),command=self.createFile)
        button.grid( )
        frame1.pack(padx = 30 ,pady=100)
        frame2.pack(pady = 0)
    def createFile(self):
        a = (self.email.get("1.0","end-1c"))
           
            
            
        b = (self.password.get("1.0","end-1c"))
        
        
        with open("login.txt","a") as w:
            w.write(f"{a}\n")
            w.write(b)
            
            
            
        # os.remove("login.txt")
        python = sys.executable
        os.execl(python, python, * sys.argv)
            
           
            
        
    
class Send:
    def __init__(self):
      self.pickedfiletypes = (('HTML files', '*.html'),('HTM files',"*.htm"))
      self.pickedImagetypes = (('Jpeg', '*.jpeg'),('Jpg',"*.jpg"),("PNG",'*.png'))
      self.message = MIMEMultipart("alternative")
      self.port = 465
      self.context = ssl.create_default_context()
      self.list = []
      self.imageList = []
      self.sendFile()
      self.value = 0
      self.imageValue = 0
        
        
        
    def sendFile(self):
        frame1 = Frame(tk)
        label1 = Label(frame1,text="TO",font=("COURIER",20))
        self.email = Text(frame1,font=("COURIER",20),height=1,width=50)
        label2= Label(frame1,text="Subject",font=("COURIER",20))
        self.subject = Text(frame1,font=("COURIER",20),height=1,width=50)
        label1.grid(row=0,column = 0)
        self.email.grid(row=0,column = 1)
        label2.grid(row=1,column = 0)
        self.subject.grid(row = 1,column = 1)
        label3= Label(frame1,text="Message",font=("COURIER",20))
        self.textmessage = Text(frame1,font=("COURIER",20),height=8,width=50)
        label3.grid(row = 2,column = 0,pady=20)
        self.textmessage.grid(row= 2,column = 1,pady = 20)
        self.AttachedFile = Frame(tk)
        ButtonWorks = Frame(tk)
        self.sendHtml = Button(ButtonWorks,text = "ADD HTML",font=("Courier",10,"bold"),bg="#292A9E",command = self.readHtml)
        self.sendHtml.grid(padx = 10,row = 3,column = 0,ipadx=20,ipady=10)
        sendFile = Button(ButtonWorks,text = "Attach FIle",font=("Courier",10,"bold"),bg="#292A9E",command=self.attach)
        # clearMessage = Button(ButtonWorks,text = "Clear Messsage",font=("Courier",10,"bold"),bg="white",command=self.clearMessage)
        # clearMessage.grid(padx = 10,row = 3,column = 3,ipadx=20,ipady=10)

        sendFile.grid(padx = 10,row = 3,column = 1,ipadx=20,ipady=10)
        self.sendImage= Button(ButtonWorks,text = "Add Image",font=("Courier",10,"bold"),bg="#292A9E",command=self.readImage)
        self.sendImage.grid(row = 3,column = 2,ipadx=10,ipady=10)
        sendAll= Button(ButtonWorks,text = "Send Email!",font=("Courier",10,"bold"),bg="#992222",command=self.send)
        sendAll.grid(padx= 70,row = 3,column = 4,ipadx=10,ipady=10)
        frame1.pack()
        attached = Label(self.AttachedFile,text="Attached Files",font=("Courier",20,"bold"))
        attached.grid()
        changeInfo= Button(tk,text = "Change Login",font=("Courier",10,"bold"),bg="#992222",command=self.back)

        
        
            
        self.insideFIle = Label(self.AttachedFile)
        self.AttachedFile.pack()
        self.insideFIle.grid(row=2)
        ButtonWorks.pack()
        changeInfo.pack(pady=10)
            
        
        # self.imageFile = Frame(tk,width = 300,height=300)
        # self.imageFile.pack()
        
    def back(self):
        
    # """Restarts the current program.
    # Note: this function does not return. Any cleanup action (like
    # saving data) must be done before calling this function."""
        os.remove("login.txt")
        python = sys.executable
        os.execl(python, python, * sys.argv)
           
    def readImage(self):


        try:
        
        
            fmage = filedialog.askopenfilename(initialdir="/User/lenovo/Desktop",title= "Select Html Files",filetypes= self.pickedImagetypes)   
            if fmage != None and len(fmage) >1:
                self.imageList.append(fmage)
                
                
                
            with open(fmage, "rb") as attachment:

            
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                self.message.attach(part)
                    
            if len(self.imageList) ==1:
                self.sendImage["state"]="disabled"
                self.sendImage.config(bg="white")
 
            self.showImage(fmage)
        except FileNotFoundError:
            pass

                
            
        
        
        # file = Label(lk,image=img)
        # file.pack()
    

    def readHtml(self):

        try:
            html = filedialog.askopenfilename(initialdir="/User/lenovo/Desktop",
                                            title= "Select Html Files",
                                            filetypes= self.pickedfiletypes)
            d = html.split("/")
            title = d[-1]
            with open(html,"r") as file:
                j = file.read()
                htmlMsg = MIMEText(j,"html")
                self.message.attach(htmlMsg)
            while len(title) >=1:
                self.list.append(title)
                title = ""
                
            self.fileLister()
            if len(self.list) ==1:
                self.sendHtml["state"] = "disabled"
            self.sendHtml.config(bg="white")
        except Exception as e:
            self.error(e)
            
        
        
            
    def send(self):
        
        try:
            self.message["Subject"] = self.subject.get('1.0',"end-1c")
            # self.message["From"] = self.email.get("1.0","end-1c")
            self.message["To"] = self.email.get("1.0","end-1c")
            mainMsg = MIMEText(self.textmessage.get("1.0","end-1c"), "plain")
            self.message.attach(mainMsg)
            with open("login.txt","r") as r:
                a,b = r.readlines()
                
            with smtplib.SMTP_SSL("smtp.gmail.com", self.port) as server:
                server.login(a, b.strip())
                server.sendmail(a ,self.email.get("1.0","end-1c"),self.message.as_string())
            # def removeFile(self):
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror(title="Error",message="Authentication Error")

           
        except Exception:    
            messagebox.showerror(title="Error",message="Message can't be send")


        
             
        #     file = Label(self.AttachedFile,text=f"{self.list[self.value]}",font=("Courier",15),bg="#03dbfc")
        #     remove = Button(self.AttachedFile,text="-")
            
        #     file.grid(row=0,column=self.value,padx=10,pady=10,command=self.removeFile)
        #     remove.grid(row = 0,column = self.value,padx =10)
        #     self.value +=1
    def fileLister(self):
            
            
        file = Label(self.AttachedFile,text=f"{self.list[self.value]}",font=("Courier",15),bg="#03dbfc")
            
            
        file.grid(row=1,column=self.value,padx=10,pady=10)
            # remove.grid(row = 0,column = self.value,padx =10)
        self.value +=1
                
    def showImage(self,i):

        

            
        size = Image.open(i)
        size = size.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(size)
        file = self.insideFIle.configure(image=img)
        file.grid()
    def attach(self):
        try:
            document = filedialog.askopenfilename(initialdir="/User/lenovo/Desktop",
                                                title= "Select Documents",
                                                filetypes= (("All files","*.*"),("Pdf","*.pdf")))
            with open(document, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            d = document.split("/")
            title = d[-1]
            while len(title) >=1:
                self.list.append(title)
                title = ""
            self.fileLister()
    # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
            part.add_header("Content-Disposition",f"attachment; filename= {document}",)
            self.message.attach(part)
        except Exception as e:
            self.error(e)
    def error(self,e):
        messagebox.showerror(title="ERROR", message=e)

        


          
                
            
    # def clearMessage(self):
    #     if len(self.message) >1:
    #         self.message =MIMEMultipart() 
    #         self.list = []
    #         # self.clearMessage["state"]="disabled"                      
value = True           
def main():
   
    a = os.getcwd()
    
    b = os.listdir(a)
    
    if "login.txt" in b :
        Send()
    else:
        Login()
main()      
tk.mainloop()        
        
            

    
