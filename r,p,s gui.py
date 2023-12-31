from tkinter import *
from tkinter import messagebox
import random
options=['rock','paper','scissors']
computer=random.choice(options)

root=Tk()
def whenclicked(choice):
  player_choice=choice
  if player_choice== computer :
     messagebox.showinfo ('Result','it is a tie')
  elif (player_choice=='rock' and computer=='scissors') or (player_choice=='paper' and computer=='rock') or (player_choice=='scissors' and computer=='paper'):
    messagebox.showinfo ('Result','it is a tie')
  else:
    
        messagebox.showinfo('Reesult','you lost,computer chose' +computer)



root.title('Rock,paper,scissors')
rock=Button(root,text='Rock',padx=100,pady=100,command=lambda:whenclicked('rock'),bg='yellow')
paper=Button(root,text='paper',padx=100,pady=100,command=lambda: whenclicked('paper'),bg='yellow')
scissors=Button(root,text='scissors',padx=100,pady=100,command=lambda:whenclicked('scissors'),bg='yellow')
rock.pack()
paper.pack()
scissors.pack()

root.mainloop()