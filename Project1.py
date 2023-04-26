import os
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root=Tk()
root.title("HOME PAGE!")
root.geometry("2500x150")
def mai():
    os.system('python Project.py')
 
label11=Label(root, text="WELCOME TO\nLANGUAGE TRANSLATION PLATFORM\n Language is the road map of a culture. It tells you where its people come from and where they are going\n",
              font=("Algerian"),fg="white",bg="black")
label11.place(x=630,y=130,height=20,width=300)
label11.pack()

root.configure(bg='purple')

b1=Button(root, text="Let's translate buddy!", command=mai)
b1.pack(side=BOTTOM)


root.mainloop()
