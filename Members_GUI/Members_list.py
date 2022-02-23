# Import Module
from tkinter import *
from turtle import width

# Function will remove selected Listbox items
def remove_item():
	selected_checkboxs = listbox.curselection()

	for selected_checkbox in selected_checkboxs[::-1]:
		listbox.delete(selected_checkbox)

# Create Object
root = Tk()

# Set Geometry
root.geometry("500x500")

# Add Listbox
listbox = Listbox(root,height = 20, width = 20, selectmode=MULTIPLE)
listbox.pack()

# Listbox Items List
items = ["Vishnu", "Praneeth", "Saiteja", "Janardhan"]

# Iterate Through Items list
for item in items:
	listbox.insert(END, item)

Button(root, text="delete",bg="green",command=remove_item).pack()

# Execute Tkinter
root.mainloop()
