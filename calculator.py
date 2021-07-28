from tkinter import *
import re

win = Tk()

#variables
w_width = 300
w_height = 550

pos_x = int(win.winfo_screenwidth()/2 - w_width/2)
pos_y = int(win.winfo_screenheight()/2 - w_height/2)
key_buts= [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    [".","0","="]
]
ope_buts=  ["DEL","/","*","-","+"]
text_var = StringVar()
calculated = False

#functions
def input_str(string):
    global calculated
    if calculated and (string not in ope_buts[0:]):
        delete()
    text_var.set(text_var.get()+string)
    calculated=False

def calculate():
    global calculated
    try:
        text_var.set(eval(re.sub(r'0+(.+)',r'\1',text_var.get())))
        calculated = True
    except SyntaxError:
        messagebox.showwarning("Warning","Something went wrong\nPlease check and correct your input")
def delete():
    if calculated:
        text_var.set('')
    else:
        text_var.set(text_var.get()[:-1])
    
#Setting up the graphics
win.title("Calculator")
win.resizable(width=False,height=False)
win.geometry("{}x{}+{}+{}".format(w_width,w_height,pos_x,pos_y))
buts_frame = Frame(win,width=int(w_width),height=int(w_height*3/4))
io_frame = Frame(win,width=int(w_width),height=int(w_height/4),bg="#fff")
key_buts_frame = Frame(buts_frame)
ope_buts_frame = Frame(buts_frame)
io_text = Label(io_frame,textvar = text_var,font=("Arial 18"),bg='#fff')

for i in range(4):
    Grid.rowconfigure(key_buts_frame,i,weight=1)
for i in range(3):
    Grid.columnconfigure(key_buts_frame,i,weight=1)

for x in range(4): #for digits 
    for y in range(3):
        Button(key_buts_frame,
               text=key_buts[x][y],
               bd=0,
               bg="#232323",
               fg="#fff",
               relief = FLAT,
               font=("Arial 16 bold"),
               activebackground="#fff",
               command=(lambda a=x,b=y:input_str(key_buts[a][b]),calculate)[key_buts[x][y]=="="]
        ).grid(row=x,column=y,sticky=NSEW)

Grid.columnconfigure(ope_buts_frame,0,weight=1)
for x in range(5): #for operations
    Grid.rowconfigure(ope_buts_frame,x,weight=1)
    Button(ope_buts_frame,
           text=ope_buts[x],
           bd=0,
           relief = FLAT,
           bg="#353535",
           fg="#fff",
           activebackground="#fff",
           font=("Arial 14"),
           command=(lambda a=x:input_str(ope_buts[a]),delete)[ope_buts[x]=="DEL"]
    ).grid(row=x,column=0,sticky=NSEW)




io_text.pack(pady=50,padx=5,side=RIGHT)
key_buts_frame.pack(side = LEFT,fill=BOTH,expand=1)
ope_buts_frame.pack(side = RIGHT,fill=BOTH)
io_frame.pack(side = TOP,fill=X)
buts_frame.pack(side = BOTTOM,fill=BOTH,expand=1)
text_var.set('0')

win.mainloop()
