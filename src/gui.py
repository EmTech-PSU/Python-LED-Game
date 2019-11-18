import tkinter as tk

frame = tk.Tk()
frame.title("Python LED Game")

label1 = tk.Label(frame, text = "Enter Player 1 Name:", font = ("Raleway Light",20))
label1.grid(column = 0, row = 0)

label2 = tk.Label(frame, text = "Enter Player 2 Name:", font = ("Raleway Light",20))
label2.grid(column = 0, row = 1)

entry1 = tk.Entry(frame)
entry1.focus_set
entry1.grid(column = 1, row = 0)

entry2 = tk.Entry(frame)
entry2.focus_set
entry2.grid(column  = 1, row = 1)

def quitProgram():
    pass
def sendText():
    pass
def getStats():
    pass
def startGame():
    pass

def getText():
    player1Name = entry1.get()
    player2Name = entry1.get()

sendBtn = tk.Button(frame, text='Submit Names')
sendBtn.grid(column = 0, row = 2)
startBtn = tk.Button(frame, text='Start Game')
startBtn.grid(column = 1, row = 2)
statsBtn = tk.Button(frame, text='Stats')
statsBtn.grid(column = 2, row = 2)
quitBtn = tk.Button(frame, text='Quit')
quitBtn.grid(column = 3, row = 2)


frame.mainloop()