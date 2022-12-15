import tkinter as tk
import numpy as np
import random
p = tk.Tk()
p.title('Password Generator')
p.configure(bg='black')

t = tk.Label(p,text='Generated password',bg='slateblue1',fg='white',font='bold')
t.grid(column=4,row=1)

password_l = tk.Label(p,text='',fg='slateblue1',bg='WHITE',width=17,font='bold')
password_l.grid(column=4,row=2)

fake_l = tk.Label(p,text='',bg='black',width=17)
fake_l.grid(column=7,row=9)

fake_l2 = tk.Label(p,text='',bg='black',width=17)
fake_l2.grid(column=0,row=0)

fake_l3 = tk.Label(p,text='',bg='black',width=17)
fake_l3.grid(column=4,row=3)

def increaser(l):
    count = int(l['text'])
    count+=1
    l.configure(text=str(count))
def decreaser(l):
    count = int(l['text'])
    if count-1>=0:
        count-=1
    l.configure(text=str(count))

b_number = tk.Label(p,text='Numbers',bg='white',fg='black',width=17,font='bold')
b_number.grid(column=4,row=4)
b_number_plus = tk.Button(p,text='+',bg='palegreen1',fg='black',command=lambda:increaser(b_nl),font='bold')
b_number_plus.grid(column=3,row=4)
b_number_minus = tk.Button(p,text='-',bg='indianred1',fg='black',command=lambda:decreaser(b_nl),font='bold')
b_number_minus.grid(column=5,row=4)
b_nl = tk.Label(p,text=0,fg='black',bg='white',width=2,font='bold')
b_nl.grid(column=6,row=4)

b_letter = tk.Label(p,text='Alphabets',bg='white',fg='black',width=17,font='bold')
b_letter.grid(column=4,row=5)
b_letter_plus = tk.Button(p,text='+',bg='palegreen1',fg='black',command=lambda:increaser(b_ll),font='bold')
b_letter_plus.grid(column=3,row=5)
b_letter_minus = tk.Button(p,text='-',bg='indianred1',fg='black',command=lambda:decreaser(b_ll),font='bold')
b_letter_minus.grid(column=5,row=5)
b_ll = tk.Label(p,text=0,fg='black',bg='white',width=2,font='bold')
b_ll.grid(column=6,row=5)

b_char = tk.Label(p,text='Symbols',bg='white',fg='black',width=17,font='bold')
b_char.grid(column=4,row=6)
b_char_plus = tk.Button(p,text='+',bg='palegreen1',fg='black',command=lambda:increaser(b_cl),font='bold')
b_char_plus.grid(column=3,row=6)
b_char_minus = tk.Button(p,text='-',bg='indianred1',fg='black',command=lambda:decreaser(b_cl),font='bold')
b_char_minus.grid(column=5,row=6)
b_cl = tk.Label(p,text=0,fg='black',bg='white',width=2,font='bold')
b_cl.grid(column=6,row=6)

b_generate = tk.Button(p,text='Generate',bg='slateblue1',fg='black',command=lambda:password_generator(),font='bold')
b_generate.grid(column=4,row=7)

b_reset = tk.Button(p,text='Reset',fg='black',bg='red',command=lambda:resetter(),font='bold')
b_reset.grid(column=4,row=8)

password = ''
def password_generator():
    global password
    n = [0,1,2,3,4,5,6,7,8,9]
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s = ['~','@','#','$','%','^','&','*']
    i = int(b_nl['text'])
    j = int(b_ll['text'])
    k = int(b_cl['text'])
    for x in range(i):
        password+=str(np.random.choice(n))
    for y in range(j):
        password+=str(np.random.choice(a))
    for z in range(k):
        password+=str(np.random.choice(s))
    new = []
    for l in password:
        new.append(l)
    random.shuffle(new)
    password=''
    for m in new:
        password+=m
    password_l.configure(text=password)
    if len(password)>17:
        password_l.configure(width=len(password))
    password = ''
def resetter():
    password_l.configure(text='')
    b_nl.configure(text=0)
    b_ll.configure(text=0)
    b_cl.configure(text=0)
    password_l.configure(width=17)
p.mainloop()