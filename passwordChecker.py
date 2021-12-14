
import re
from tkinter import *

root = Tk()
root.title('Password Check')
root.geometry("400x400")

#functions
def myClick():
    characterRegex = re.compile(r'\w{8,}')
    mo1 = characterRegex.findall(e.get())
    if mo1 == []:
        global myLable1
        myLable1 = Label(root, text='Not enough characters')
        myLable1.grid(row=4, column=0)
    else:
        uppercaseRegex = re.compile(r'[A-Z]+')
        mo2 = uppercaseRegex.findall(e.get())
        if mo2 == []:
            global myLable2
            myLable1.destroy()
            myLable2 = Label(root, text='Needs at least one uppercase')
            myLable2.grid(row=4, column=0)
        else:
            numberRegex = re.compile(r'[0-9]+')
            mo3 = numberRegex.findall(e.get())
            if mo3 == []:
                global myLable3
                myLable2.destroy()
                myLable3 = Label(root, text='Needs at least one number')
                myLable3.grid(row=4, column=0)
            else:
                myLable3.destroy()
                myLable4 = Label(root, text="Good password!")
                myLable4.grid(row=4, column=0)


# Created a label widget
header = Label(root, text="Password:")
e = Entry(root, width=30, font=('arial', 12))
b = Button(root, text='Enter', command=myClick)



# griding it into the screen
header.grid(row=0, column=0)
e.grid(row=1, column=0, padx=68, pady=10)
b.grid(row=2, column=0)

root.mainloop()
