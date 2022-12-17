from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#94B49F")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_byte = base64.b64decode(decode_message)
        decrypt = base64_byte.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial",
              fg="black", bg="#94B49F").place(x=20, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("decryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("decryption", "Invalid Password")

def encrypt():
    password=code.get()
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#94B49F")
        
        message=text1.get(1.0, END)
        encode_message=message.encode("ascii")
        base64_byte=base64.b64encode(encode_message)
        encrypt=base64_byte.decode("ascii")
        
        Label(screen1, text="ENCRYPT", font="arial", fg="black", bg="#94B49F").place(x=20,y=0)
        text2=Text(screen1,font="Roboto 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)
    elif password=="":
        messagebox.showerror("encryption","Input Password")
    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password")
        

def home_screen():
    global screen
    global code
    global text1
    screen=Tk()
    screen.geometry("400x550")
    
    app_icon=PhotoImage(file="cipher.png")
    screen.iconphoto(False, app_icon)
    screen.title("Text<->Cipher")
    def reset():
        code.set("")
        text1.delete(1.0,END)
    Label(text="Enter the text to cipher or encipher: ",
          fg="#3D5656", font=("Lucida Sans", 15)).place(x=10, y=10)
    text1=Text(font="Noto 15",bg="white", relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=380,height=150)
    
    Label(text="Enter the Screte key to proceed: ",
          fg="#3D5656", font=("Lucida Sans", 13)).place(x=10, y=220)
    code=StringVar()
    Entry(textvariable=code, width=20, bd=0, font=("Noto",13),show='*').place(x=10, y=260)
    
    Button(text="ENCRYPT", height="2", width=23, bg="#68B984",
           fg="#2D033B", bd=0,command=encrypt).place(x=10, y=300)
    Button(text="DECRYPT", height="2", width=23, bg="#B09B71",
           fg="#2D033B", bd=0, command=decrypt).place(x=200, y=300)
    Button(text="RESET", height="2", width=50, bg="#D09CFA",
           fg="#461111", bd=0,command=reset).place(x=10, y=350)
    
    screen.mainloop()
    
home_screen()