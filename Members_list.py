# Import Module
# from asyncio.windows_events import NULL
from asyncio.windows_events import NULL
from tkinter import *
import delta_cli

object = delta_cli.MyPrompt()
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
items = object.do_show_players(inp="current_players")

# Iterate Through Items list
if items == NULL:
    items = []
else:
    for item in items:
        listbox.insert(END, item)


photo = PhotoImage(file = r"/Users/praneethkallam/SER-516-Project/delta_poker/reloading.png")
photoimage = photo.subsample(3, 3)
a = Button(root, text="Refresh", image = photoimage, compound = LEFT).pack()
b = Button(root, text="delete",command=remove_item).pack()

# Execute Tkinter
root.mainloop()
