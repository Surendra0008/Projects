from tkinter import *
from PIL import Image,ImageTk
from random import randint

window = Tk()
window.title('Rock Paper and Scissors Game')
window.configure(background='light blue')

image_l_rock = ImageTk.PhotoImage(Image.open(r"C:\Users\surendra karaka\OneDrive\Desktop\python\Mini-projects\Rock Paper Scissor\LR.jpg"))
image_l_paper = ImageTk.PhotoImage(Image.open(r"C:\Users\surendra karaka\OneDrive\Desktop\python\Mini-projects\Rock Paper Scissor\LP.jpg"))
image_l_scissor = ImageTk.PhotoImage(Image.open(r"C:\Users\surendra karaka\OneDrive\Desktop\python\Mini-projects\Rock Paper Scissor\LS.jpg"))
image_r_rock = ImageTk.PhotoImage(Image.open(r"C:\Users\surendra karaka\OneDrive\Desktop\python\Mini-projects\Rock Paper Scissor\RR.jpg"))
image_r_paper = ImageTk.PhotoImage(Image.open(r"C:\Users\surendra karaka\OneDrive\Desktop\python\Mini-projects\Rock Paper Scissor\RP.jpg"))
image_r_scissor = ImageTk.PhotoImage(Image.open(r"C:\Users\surendra karaka\OneDrive\Desktop\python\Mini-projects\Rock Paper Scissor\RS.jpg"))

l_computer = Label(window,image=image_l_scissor)
l_player = Label(window,image=image_r_paper)
l_computer.grid(row=1,column=0)
l_player.grid(row=1,column=4)

computer_score = Label(window,text=0,font=('arial',60,'bold'),bg='black',fg='sandy brown')
player_score = Label(window,text=0,font=('arial',60,'bold'),bg='black',fg='light green')
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

computer_indicator = Label(window,text='Computer',font=('arial',40,'bold'),bg='black',fg='white').grid(row=0,column=1)
player_indicator = Label(window,text='Player',font=('arial',40,'bold'),bg='black',fg='white').grid(row=0,column=3)

def msg_display(a):
    final_message['text'] = a
def c_score_update():
    score = int(computer_score['text'])
    score+=1
    computer_score.configure(text=str(score))
def p_score_update():
    score = int(player_score['text'])
    score+=1
    player_score.configure(text= str(score))
def check_winner(c,p):
    if c==p:
        msg_display("It's a tie")
    elif c=='ROCK':
        if p=="SCISSOR":
            msg_display('Computer Wins!!')
            c_score_update()
        if p=='PAPER':
            msg_display('Player Wins!!')
            p_score_update()
    elif c=='PAPER':
        if p=="ROCK":
            msg_display('Computer Wins!!')
            c_score_update()
        if p=='SCISSOR':
            msg_display('Player Wins!!')
            p_score_update()
    elif c=="SCISSOR":
        if p=="PAPER":
            msg_display('Computer Wins!!')
            c_score_update()
        if p=='ROCK':
            msg_display('Player Wins!!')
            p_score_update()

choices = ['ROCK','PAPER','SCISSOR']
def choice_update(x):
    c_choice = choices[randint(0,2)]
    if c_choice=='ROCK':
        l_computer.configure(image=image_l_rock)
    elif c_choice=='PAPER':
        l_computer.configure(image=image_l_paper)
    else:
        l_computer.configure(image=image_l_scissor)

    if x=='ROCK':
        l_player.configure(image=image_r_rock)
    elif x=='PAPER':
        l_player.configure(image=image_r_paper)
    else:
        l_player.configure(image=image_r_scissor)

    check_winner(c_choice,x)
def reset_game():
    computer_score.configure(text=0)
    player_score.configure(text=0)
    final_message.configure(text="")

final_message = Label(window,font=('arial',25,'bold'),bg='black',fg='white')
final_message.grid(row=4,column=2)
b_rock = Button(window,text='ROCK',width=16,height=2,bg='white',fg='black',font=('arial',20,'bold'),command=lambda:choice_update("ROCK")).grid(row=3,column=1)
b_paper = Button(window,text='PAPER',width=16,height=2,bg='white',fg='black',font=('arial',20,'bold'),command=lambda:choice_update("PAPER")).grid(row=3,column=2)
b_scissor = Button(window,text='SCISSOR',width=16,height=2,bg='white',fg='black',font=('arial',20,'bold'),command=lambda:choice_update("SCISSOR")).grid(row=3,column=3)
new_game = Button(window,text="RESET",width=16,height=2,bg='red',fg='black',command=lambda:reset_game()).grid(row=5,column=2)
window.mainloop()

