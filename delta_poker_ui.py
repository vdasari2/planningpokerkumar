import tkinter as tk
from tkinter import * 
import turtle
import json
#from game import VotingSystem
root=tk.Tk()
root.title("Planning poker App")
root.geometry("1000x600")
addplayer=tk.StringVar()
addvalue=tk.StringVar()
username="janardhan"
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
def on_click_submit(val,vote_issue):
   val=addvalue.get()
   print(vote_issue)
   with open('/Users/janardhanreddybommireddy/Desktop/delta_poker/examples/vote.json','r') as openfile:
      vote_file=json.load(openfile)
   for i in vote_file:
      prev_vot_list=i
      print(prev_vot_list)
      if (username==prev_vot_list['username']) and (vote_issue==prev_vot_list['description']):
         tk.messagebox.showinfo("Message_already_vote",  "You have already given the vote to the issue")
      else:
         add_vote={"username":username,"description":vote_issue,"vote":val}
         vote_files.append(add_vote)
         inp_vote=json.dumps(vote_files)
         with open('/Users/janardhanreddybommireddy/Desktop/delta_poker/examples/vote.json','w') as outfile:
            outfile.write(inp_vote)
         tk.messagebox.showinfo("Message1",  "You have added vote")
         val.set("")
   print('hii')
   print(val)
def on_click_vote(issue):
   issue=menu.get()
   vote=StringVar()
   vote.set("Vote value")
   vote_entry=tk.Entry(root, textvariable=addvalue, font=('roman',15,'normal'))
   vote_sub_btn=tk.Button(root,text='Submit',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green",
   bg="blue",command = lambda:on_click_submit(addvalue,issue))
   vote_sub_btn.grid(row=4,column=3)
   vote_entry.grid(row=4,column=2)
   print("After voting")
def on_click_show_result(issue):
   issue=menu.get()
   
   with open('/Users/janardhanreddybommireddy/Desktop/delta_poker/examples/vote.json','r') as openfile:
      vote_file=json.load(openfile)
      result_vote=[]
      print(len(vote_file))
   for i in vote_file:
      print(i)
      if(issue==i['description']):
         result_vote.append(i['vote'])
   if(len(result_vote)>0):      
      print(result_vote)
      vote_result=tk.Label(root,text=result_vote,bg="black", font=('roman',15, 'bold'))
   else:
      vote_result=tk.Label(root,text="None",bg="black", font=('roman',15, 'bold'))
   vote_result.grid(row=5,column=1)
def on_click_delete_vote(delete_issue):
   delete_issue=menu.get()
   print(delete_issue)
   with open('/Users/janardhanreddybommireddy/Desktop/delta_poker/examples/vote.json','r')   as openfile:
      votes=json.load(openfile)
   for result in votes:
      if(delete_issue==result['description']):
         votes.remove(result)
         print(votes)
   final_votes=json.dumps(votes)
   with open('/Users/janardhanreddybommireddy/Desktop/delta_poker/examples/vote.json','w')   as outfile:
      outfile.write(final_votes)
issue_label = tk.Label(root, text = 'Issue',bg="orange", font=('roman',15, 'bold'))
issue_entry = tk.Entry(root,textvariable = addplayer, font=('roman',15,'normal'))
sub_btn=tk.Button(root,text = 'ADD',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green",
bg="blue",command = lambda:click(addplayer))
issue_label.grid(row=0,column=0)
issue_entry.grid(row=0,column=1)
#add_btn.grid(row=0,column=2)
sub_btn.grid(row=2,column=1)
sub_btn1=tk.Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="red",command=quit)
sub_btn1.grid(row=2,column=2)
with open('/Users/janardhanreddybommireddy/Desktop/delta_poker/examples/issues_list.json','r')   as openfile:
      json_object=json.load(openfile)
length_list=len(json_object)
string_list=[]
for list_value in json_object:
   desc_list= list_value
   string_list.append(desc_list["description"])
print(string_list)
menu=tk.StringVar()
menu.set("select issue")
drop=OptionMenu(root,menu,*string_list)
drop.grid(row=4,column=0)
vote=tk.Button(root, text='Vote',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green", bg="blue", command=lambda:on_click_vote(menu))
vote.grid(row=4,column=1)
result=tk.Button(root,text='Show result',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green",
bg="blue",command = lambda:on_click_show_result(menu))
result.grid(row=5,column=0)
delete_votes=tk.Button(root, text='Delete Votes for Selected issue',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green", bg="blue", command=lambda:on_click_delete_vote(menu))
delete_votes.grid(row=5,column=2)
root.mainloop()