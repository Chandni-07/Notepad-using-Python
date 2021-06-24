from tkinter import *
from tkinter.messagebox import  showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def  newfile():
    global file
    root.title("Untitled - Notepad")
    file= None
    #delete complete text from 1 line 0 th index till end
    TextArea.delete(1.0,END)

def  openfile():
    global file
    file= askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.*")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) +"- Notepad")
        TextArea.delete(1.0, END)
        f= open(file , "r")
        #reading from file and opening it into notepad
        TextArea.insert(1.0, f.read())
        f.close()

def  savefile():
    global file
    if file == None:
        file= asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.*")])

        if file=="":
            file=None

        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+ "- Notepad")
            showinfo("Notepad", "Your file is saved now!")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def  quitapp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def  copy():
    TextArea.event_generate(("<<Copy>>"))

def  paste():
    TextArea.event_generate(("<<Paste>>"))

def  about():
    showinfo("Notepad","Notepad  designed using python !")


if __name__ == '__main__':
    # basic setup
    root= Tk()
    root.title("Untitled-Notepad")
    root.geometry("644x555")

    #text area
    TextArea = Text(root, font="lucinda 15")
    file = None
    TextArea.pack(fill=BOTH,expand=True)

    #menu bar
    MenuBar= Menu(root)
    #filemenu starts
    FileMenu = Menu(MenuBar , tearoff=0)
    FileMenu.add_command(label="New", command=newfile)
    FileMenu.add_command(label="Open", command=openfile)
    FileMenu.add_command(label="Save", command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitapp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    #filemenu ends

    #editmenu starts
    EditMenu= Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    #editmenu ends

    #helpmenu starts
    HelpMenu= Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # helpmenu ends
    root.config(menu=MenuBar)

    #adding scrollbar using rules from tkinter
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()