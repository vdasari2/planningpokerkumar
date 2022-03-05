from tkinter import *
import tkinter.ttk as ttk
import csv

class EpicData(Tk):
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Display Epics Data")
        self.width = 700
        self.height = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2)
        self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))
        self.userStoryDataLabel = "Display UserStory Data"
        self.button = Button(self.root, text=self.userStoryDataLabel, command=self.printSomething)
        self.button1 = Button(self.root, text="Display Epic Data", command=self.epics)
        self.button.pack(side=TOP)
        self.button1.pack(side=TOP)
        self.frame = Frame(self.root, width=500)
        self.root.mainloop()

    def printSomething(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        TableMargin = self.frame
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
        print("Helloe")
        with open('/Users/vishnupreethamreddydasari/Downloads/userstories.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                firstname = row['id']
                lastname = row['subject']
                address = row['description']
                tree1.insert("", 0, values=(firstname, lastname, address))


    def epics(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        TableMargin = self.frame
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
        print("HelloEpic")
        with open('/Users/vishnupreethamreddydasari/Downloads/epics.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                firstname = row['id']
                lastname = row['subject']
                address = row['description']
                tree.insert("", 0, values=(firstname, lastname, address))
        self.userStoryDataLabel = "Changed Label"

 
    # if __name__ == '__main__':
    #     self.root.mainloop()

epicData = EpicData()
epicData.mainloop()
