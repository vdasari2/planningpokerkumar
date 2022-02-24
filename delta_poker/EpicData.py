from tkinter import *
import tkinter.ttk as ttk
import csv
def printSomething():
    
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree1 = ttk.Treeview(TableMargin, columns=("id", "subject", "description"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree1.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree1.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree1.heading('id', text="id", anchor=W)
    tree1.heading('subject', text="subject", anchor=W)
    tree1.heading('description', text="description", anchor=W)
    tree1.column('#0', stretch=NO, minwidth=0, width=0)
    tree1.column('#1', stretch=NO, minwidth=0, width=100)
    tree1.column('#2', stretch=NO, minwidth=0, width=200)
    tree1.column('#3', stretch=NO, minwidth=0, width=900)
    tree1.pack()

    with open('/Users/vishnupreethamreddydasari/Downloads/userstories.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            firstname = row['id']
            lastname = row['subject']
            address = row['description']
            tree1.insert("", 0, values=(firstname, lastname, address))


def epics():
    
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("id", "subject", "description"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('id', text="id", anchor=W)
    tree.heading('subject', text="subject", anchor=W)
    tree.heading('description', text="description", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=900)
    tree.pack()

   

root = Tk()
root.title("Display Epics Data")
width = 700
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
button = Button(root, text="Display UserStory Data")
button1 = Button(root, text="Display Epic Data", command=epics)
button.pack(side=TOP)
button1.pack(side=TOP)


      
if __name__ == '__main__':
    root.mainloop()