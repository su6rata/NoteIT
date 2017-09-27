
import Tkinter
import tkFileDialog
import tkMessageBox
import ScrolledText
        # as Tkinter Text Area does not provide Scrolling

root = Tkinter.Tk(className=" NoteIT")
textPad = ScrolledText.ScrolledText(root, width = 95, height = 45,bg="seashell2",
                  bd=10,font="Times 18 bold",cursor="xterm", highlightthickness=5, insertborderwidth=3,
                    insertwidth=3, padx=10,pady=10, relief ="groove",
                    wrap="word")


# create a menu
def new_file():
      t=textPad.get("1.0", "end-1c")
      if t=="":
        label = tkMessageBox.showinfo("New File","   Your New File\nClick OK to Continue")
      else:
        result = tkMessageBox.askquestion("New File","You already save previous data!")
        if(result=="yes"):
          textPad.delete('1.0', "end-1c")
        else:
          t = textPad.get("1.0", "end-1c")
          savelocation=tkFileDialog.asksaveasfilename(title='Save File As',
          filetypes= (("Text Files","*.txt"),("All Files","*.*")))
          file1=open(savelocation, "w+")
          file1.write(t)
          file1.close()
          textPad.delete('1.0', "end-1c")
def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file',
          filetypes= (("Text Files","*.txt"),("All Files","*.*")))
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

def save_as_command():
    t = textPad.get("1.0", "end-1c")
    savelocation=tkFileDialog.asksaveasfilename(title='Save File As',
          filetypes= (("Text Files","*.txt"),("All Files","*.*")))
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "NoteIT v-1.0 by Subrata Pandey")


#menu = Tkinter.Menu(root,activebackground="yellow",bg="gold",activeborderwidth=3,activeforeground="magenta4",bd=2,cursor="man",disabledforeground="red",font="TkMenuFont 10 bold")

menubar = Tkinter.Menu(root)
root.config(menu=menubar)

menubar.add_command(label="New", command=new_file)
menubar.add_command(label="Open", command=open_command)
menubar.add_command(label="Save as", command=save_as_command)
menubar.add_command(label="About", command=about_command)
menubar.add_command(label="Exit", command=exit_command)

# end of menu creation

textPad.pack()
root.mainloop()