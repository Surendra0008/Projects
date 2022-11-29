import tkinter as tk
calculation = ''
def add_to_calculator(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = result
        text_result.delete(1.0,'end')
        text_result.insert(1.0,result)
    except:
        clear_field()
        text_result.insert(1.0,'Error -_-')
        
def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0,'end')

root = tk.Tk()
root.title('Calculator')
root.geometry('440x400')

text_result = tk.Text(root,height=2,width=16,font=('arial',24),bg='light green')
text_result.grid(columnspan=5)

b1 = tk.Button(root,text='1',command=lambda:add_to_calculator(1),width=5,font=('arial',24),bg='grey')
b1.grid(row=2,column=1)
b2 = tk.Button(root,text='2',command=lambda:add_to_calculator(2),width=5,font=('arial',24),bg='grey')
b2.grid(row=2,column=2)
b3 = tk.Button(root,text='3',command=lambda:add_to_calculator(3),width=5,font=('arial',24),bg='grey')
b3.grid(row=2,column=3)
b4 = tk.Button(root,text='4',command=lambda:add_to_calculator(4),width=5,font=('arial',24),bg='grey')
b4.grid(row=3,column=1)
b5 = tk.Button(root,text='5',command=lambda:add_to_calculator(5),width=5,font=('arial',24),bg='grey')
b5.grid(row=3,column=2)
b6 = tk.Button(root,text='6',command=lambda:add_to_calculator(6),width=5,font=('arial',24),bg='grey')
b6.grid(row=3,column=3)
b7 = tk.Button(root,text='7',command=lambda:add_to_calculator(7),width=5,font=('arial',24),bg='grey')
b7.grid(row=4,column=1)
b8 = tk.Button(root,text='8',command=lambda:add_to_calculator(8),width=5,font=('arial',24),bg='grey')
b8.grid(row=4,column=2)
b9 = tk.Button(root,text='9',command=lambda:add_to_calculator(9),width=5,font=('arial',24),bg='grey')
b9.grid(row=4,column=3)
b0 = tk.Button(root,text='0',command=lambda:add_to_calculator(0),width=5,font=('arial',24),bg='grey')
b0.grid(row=5,column=2)
b_plus = tk.Button(root,text='+',command=lambda:add_to_calculator('+'),width=5,font=('arial',24),bg='grey')
b_plus.grid(row=2,column=4)
b_minus = tk.Button(root,text='-',command=lambda:add_to_calculator('-'),width=5,font=('arial',24),bg='grey')
b_minus.grid(row=3,column=4)
b_mul = tk.Button(root,text='x',command=lambda:add_to_calculator('*'),width=5,font=('arial',24),bg='grey')
b_mul.grid(row=4,column=4)
b_div = tk.Button(root,text='/',command=lambda:add_to_calculator('/'),width=5,font=('arial',24),bg='grey')
b_div.grid(row=5,column=4)
b_equal = tk.Button(root,text='=',command=lambda:evaluate_calculation(),width=11,font=('arial',24),bg='green')
b_equal.grid(row=6,column=3,columnspan=2)
b_open = tk.Button(root,text='(',command=lambda:add_to_calculator('('),width=5,font=('arial',24),bg='grey')
b_open.grid(row=5,column=1)
b_close = tk.Button(root,text=')',command=lambda:add_to_calculator(')'),width=5,font=('arial',24),bg='grey')
b_close.grid(row=5,column=3)
b_clear = tk.Button(root,text='C',command=lambda:clear_field(),width=11,font=('arial',24),bg='red')
b_clear.grid(row=6,column=1,columnspan=2)
root.mainloop()