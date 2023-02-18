from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg=Sor_txt.get(1.0,END)
    textget=change(text=masg, src=s, dest=d)
    des_txt.delete(1.0,END)
    des_txt.insert(END,textget)



root=Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='black')

lab_txt=Label(root,text="Translator", font=("Time New roman", 40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source text", font=("Time New roman", 20,"bold"),fg="Black",bg="red")
lab_txt.place(x=100,y=100,height=20,width=300)

Sor_txt=Text(frame, font=("Time New roman", 20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=100)
comb_sor.set("English")

button_change=Button(frame,text="Translate", relief=RAISED, command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("English")

lab_txt=Label(root,text="Dest text", font=("Time New roman", 20,"bold"),fg="Black",bg="red")
lab_txt.place(x=100,y=360,height=20,width=300)

des_txt=Text(frame, font=("Time New roman", 20,"bold"),wrap=WORD)
des_txt.place(x=10,y=400,height=150,width=480)
root.mainloop()
