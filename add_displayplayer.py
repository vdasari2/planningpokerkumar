import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import turtle


root=tk.Tk()
root.title("Planning poker App")

root.geometry("1000x600")
root.configure(bg='gray')
addplayer=tk.StringVar() 
players = []

def click():    
   tk.messagebox.showinfo("Message",  "You have registered as a player "+addplayer.get())
   add_player_name=addplayer.get()
   players.append(add_player_name)
   print(players)
   showNames()

def showNames():
    for i in range(len(players)):
        txt = tk.Text(root,height="1",width="20", bd=8, relief="groove",font=('arial', 15, 'bold'))
        txt.grid(row=5,column=i)
        txt.insert(tk.END,players[i])

name_label = tk.Label(root, text = 'Player Name', fg="white", bg="orange",relief="groove", font=('arial',15, 'bold'))
name_label.grid(row=0,column=0)

name_entry = tk.Entry(root,textvariable = addplayer, font=('roman',15,'normal'))
name_entry.grid(row=0,column=1)

sub_btn=tk.Button(root,text = 'ADD',height="1",width="20", bd=8, font=('arial', 15, 'bold'), relief="groove", fg="green",
bg="blue",command = click)
sub_btn.grid(row=2,column=0)

exit_btn1=tk.Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 15, 'bold'), relief="groove", fg="red",command=quit)
exit_btn1.grid(row=2,column=1)

root.mainloop()