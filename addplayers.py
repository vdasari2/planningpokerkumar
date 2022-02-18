import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import turtle


root=tk.Tk()
root.title("Planning poker App")

  
root.geometry("1000x600")
addplayer=tk.StringVar() 

def click():    
   tk.messagebox.showinfo("Message",  "You have registered as a player")
   add_player_name=addplayer.get()
   addplayer.set("")

name_label = tk.Label(root, text = 'Player Name',bg="orange", font=('roman',15, 'bold'))
name_entry = tk.Entry(root,textvariable = addplayer, font=('roman',15,'normal'))
sub_btn=tk.Button(root,text = 'ADD',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green",
bg="blue",command = click)
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)
sub_btn=tk.Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="red",command=quit)
sub_btn.grid(row=2,column=2)
root.mainloop()