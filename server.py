from http import server
from re import T
import threading
import tkinter

Freq = 2500
Dur = 150

top = tkinter.Tk()
top.title('Planning Poker App')
top.geometry('400x400') # Size 200, 200

def poker_server():
    global server
    def starter():
        import os
        os.system("uvicorn delta_poker:app --host=0.0.0.0")
<<<<<<< US-12/TSK-41/pkallam_server_integration
=======

    server = threading.Thread(target=starter, daemon=True)
    server.start()
>>>>>>> main

    server = threading.Thread(target=starter, daemon=True)
    server.start()

def stop():
    print ("Stop")
    top.destroy()

<<<<<<< US-12/TSK-41/pkallam_server_integration
def view_players():
    players = []
    players_window= tkinter.Tk()
    players_window.title("Current List of Players")
    players_window.geometry('1000x600')
    players_window.configure(bg='gray')
    view_players_window_label = tkinter.Label (players_window, text = "List of players",font=('arial', 10, 'bold'), relief="groove", fg="green",)
    view_players_window_label.grid(row = 100, column = 100)
            
    print(players)
    a = len(players)
    et = ''
    for i in range(a):
        et = et + players[i]+'\n' 
        EOF_lbl1 = tkinter.Label(players_window, text = et,font=('arial', 12, 'bold'), relief="groove", fg="green")
        EOF_lbl1.grid(column = 100, row = 300)

        print(et)
           

    btn12=tkinter.Button(players_window,text = 'CLOSE',font=('arial', 12, 'bold'), relief="groove", fg="red",command=quit)
    btn12.grid(row=400,column=500)

    players_window.mainloop()

startButton = tkinter.Button(top, height=2, width=20, text ="Start", command = poker_server)
stopButton = tkinter.Button(top, height=2, width=20, text ="Stop", command = stop)
btn5= tkinter.Button(top, height=2, width=20, text = 'VIEW CURRENT PLAYERS', command = view_players)
=======
startButton = tkinter.Button(top, height=2, width=20, text ="Start", command = poker_server)
stopButton = tkinter.Button(top, height=2, width=20, text ="Stop", command = stop)
>>>>>>> main

startButton.pack()
stopButton.pack()
btn5.pack()
top.mainloop()
