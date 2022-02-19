import tkinter as tk
from tkinter import * 
import turtle
import json
from game import VotingSystem
root=tk.Tk()
root.title("Planning poker App")
  
root.geometry("1000x600")
addplayer=tk.StringVar()
addvalue=tk.StringVar()
def click(issue_desc):
   issue_desc=addplayer.get()
   print(issue_desc)
   with open('/Users/janardhanreddybommireddy/Desktop/delta_poker/examples/issues_list.json','r')   as openfile:
      json_object=json.load(openfile)
   length=len(json_object)+1
   issue_count= 'issue'+ str(length)
   new_dict={"title":issue_count,"description":issue_desc}
   json_object.append(new_dict)
   issue_file=json.dumps(json_object)
   print(json_object)
   with open('/Users/janardhanreddybommireddy/Desktop/delta_poker/examples/issues_list.json','w')   as outfile:
      outfile.write(issue_file)
   print(json_object)
   tk.messagebox.showinfo("Message",  "You have added issues")
   add_player_name=addplayer.get()
   addplayer.set("")
def on_click_submit(val):
   val=addvalue.get()
   print('hii')
   print(val)
def on_click_vote(issue):

   issue=menu.get()
   vote=StringVar()
   vote.set("Vote value")
   vote_entry=tk.Entry(root, textvariable=addvalue, font=('roman',15,'normal'))
   vote_sub_btn=tk.Button(root,text='Submit',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green",
   bg="blue",command = lambda:on_click_submit(addvalue))
   vote_sub_btn.grid(row=4,column=3)
   vote_entry.grid(row=4,column=2)

   
   print("After voting")

issue_label = tk.Label(root, text = ' Issue',bg="orange", font=('roman',15, 'bold'))
issue_entry = tk.Entry(root,textvariable = addplayer, font=('roman',15,'normal'))
sub_btn=tk.Button(root,text = 'ADD',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green",
bg="blue",command = lambda:click(addplayer))
issue_label.grid(row=0,column=0)
issue_entry.grid(row=0,column=1)
#add_btn.grid(row=0,column=2)
sub_btn.grid(row=2,column=1)
sub_btn=tk.Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="red",command=quit)
sub_btn.grid(row=2,column=2)
with open('/Users/janardhanreddybommireddy/Desktop/delta_poker/examples/issues_list.json','r')   as openfile:
      json_object=json.load(openfile)
length_list=len(json_object)
string_list=[]
for list_value in json_object:
   desc_list= list_value
   string_list.append(desc_list["description"])
print(string_list)   
menu=StringVar()
menu.set("select issue")
drop=OptionMenu(root,menu,*string_list)
drop.grid(row=4,column=0)
vote=tk.Button(root, text='Vote',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green", bg="blue", command=lambda:on_click_vote(menu))
vote.grid(row=4,column=1)
root.mainloop()
