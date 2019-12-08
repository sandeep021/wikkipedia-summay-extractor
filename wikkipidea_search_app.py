from tkinter import *
import wikipedia

def search_me():
    entery_value=e.get()
    text.delete(1.0,END)
    try:
        answer_value=wikipedia.summary(entery_value)
        text.insert(INSERT,answer_value)
    except:
        text.insert(INSERT,'please check your input or internet connection')





scr=Tk()
scr.title('wikipedia summary applicaton')
scr.config(bg='blue')


frametop=Frame(scr,bg="blue")
e=Entry(frametop,bg='yellow')
e.pack()
b=Button(frametop,text='search',command=search_me,bg='red',font=('times',10,'bold'))
b.pack()








frametop.pack(side=TOP)
framebottom=Frame(scr)
scroll=Scrollbar(framebottom)
scroll.pack(side=RIGHT,fill=Y)

text=Text(framebottom,height=20,width=40,wrap='word',yscrollcommand=scroll.set,bg='yellow')
text.pack()
scroll.config(command=text.yview)

framebottom.pack()
scr.mainloop()
