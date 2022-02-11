from tkinter import *
from tkinter.ttk import *
master = Tk()
master.geometry("400x400")
def openNewWindow():
	newWindow = Toplevel(master)
	newWindow.title("New Window")
	newWindow.geometry("400x400")
	Label(newWindow,
		text ="Team Members: \n Vishnu Preetham Reddy Dasari \n Sai Teja Reddy Cheela \n Praneeth Sai Reddy Kallam \n Janardhan Reddy Bommireddy").pack()
	
label = Label(master,
			text =" Welcome to the Project PlanningPoker\n This is the basic GUI HomeScreen for our project")
label.pack(pady = 10)

btn = Button(master,
			text ="Click here to see the Collaboraters ",
			command = openNewWindow)
btn.pack(pady = 10)

btn = Button(master,
			text ="Click here to see the Collaboraters ",
			command = openNewWindow)
btn.pack(pady = 10)


mainloop()
