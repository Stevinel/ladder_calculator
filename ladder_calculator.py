from tkinter import *  
from tkinter import messagebox

def calc():
    x = int(txt.get())
    counter = 0
    while x > 0:
        x -= 1
        counter += x + 1
    if counter > 0:
        messagebox.showinfo(message=f'Суммарно ты подтянулся - {counter} раз. А ты хорош :)')
    else:
        messagebox.showinfo(message="Ну и чего мы не подтягиваемся?")


window = Tk()
window['bg'] = '#fafafa'
window.title("Добро пожаловать в приложение 'Лесенка'")
window.wm_attributes('-alpha', 0.7)
window.geometry('600x250')
window.resizable(width=False, height=False)

frame = Frame(window)
frame.place( relwidth=1, relheight=0.7)

title = Label(frame, text="Привет! \n Введи сколько максимально раз ты подтянулся в 'лесенке'?", font=40, )  
title.pack()

txt = Entry(frame, bg='white', )  
txt.pack()

btn = Button(frame, text="Посчтитать", command=calc)
btn.pack()

window.mainloop()


