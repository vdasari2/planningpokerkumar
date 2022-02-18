import tkinter
from subprocess import Popen

Freq = 2500
Dur = 150

top = tkinter.Tk()
top.title('MapAwareness')
top.geometry('400x400') # Size 200, 200

def start():
    import os
    os.system("uvicorn delta_poker:app --host=0.0.0.0")


def stop():
    print ("Stop")
    top.destroy()

startButton = tkinter.Button(top, height=2, width=20, text ="Start", 
command = start)
stopButton = tkinter.Button(top, height=2, width=20, text ="Stop", 
command = stop)

startButton.pack()
stopButton.pack()
top.mainloop()