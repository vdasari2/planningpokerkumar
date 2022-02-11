import tkinter as tk
from tkinter import * 
import turtle

a=0
root=tk.Tk()
root.title("Planning poker App")
  
root.geometry("1000x600")
addplayer=tk.StringVar() 
def click():    
   tk.messagebox.showinfo("Message",  "You have added issues")
   add_player_name=addplayer.get()
   addplayer.set("")
#def on_Clickadd():
 #  global a
  # a=a+1
   #name_label1 = tk.Label(root, text = ' Issue',bg="orange", font=('roman',15, 'bold'))
  # name_entry1 = tk.Entry(root,textvariable = addplayer, font=('roman',15,'normal'))
   #name_label1.grid(row=a,column=0)
   #name_entry1.grid(row=a,column=1)  
   #print(a)
name_label = tk.Label(root, text = ' Issue',bg="orange", font=('roman',15, 'bold'))
name_entry = tk.Entry(root,textvariable = addplayer, font=('roman',15,'normal'))
#add_btn=tk.Button(root,text = 'ADD another issue',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green",bg="blue",command = on_Clickadd)
sub_btn=tk.Button(root,text = 'ADD',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green",
bg="blue",command = click)
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
#add_btn.grid(row=0,column=2)
sub_btn.grid(row=a+2,column=1)
print("a")
print(a)
sub_btn=tk.Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="red",command=quit)
sub_btn.grid(row=a+2,column=2)
root.mainloop()