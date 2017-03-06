# coding utf-8
import os
from tkinter import *
from random import shuffle


# надо добить
# 1. Игра на время или на количество ходов
# 2. Label для показа счета игры "сколько открыто, сколько осталось, сколько шагов сделано"

print('Это игра "Запоминалка"')

SIDE = 8  # размер стороны квадрата
QSIDE = SIDE**2//2  # количество уникальных картинок
prev = None

def reset():
    pass

def cmd():
    print('Я - полезная функция')
    print('...')

def hide_all(buttons):
    '''Прячет все кнопки
    '''
    for btn in buttons:
        btn.configure(image=faq)

def hide_both(prev, btn):
    '''Спрятать две кнопки'''
    prev.configure(image=faq)
    btn.configure(image=faq)

def change(btn):
    global prev
    btn.configure(image=btn.img)
    if prev is None:
        prev = btn
    else:
        if prev.x != btn.x or prev is btn:
            main_window.after(1000, hide_both, prev, btn)
        prev = None
# def <lambda> (b=btn): change(b)

main_window = Tk()
main_window.title('Запоминалка')

faq = PhotoImage(file='FAQ.gif')

files = [os.path.join('gif', f) for f in os.listdir('gif')]
shuffle(files)
files = files[0:QSIDE] * 2
shuffle(files)
print(files)

images = [PhotoImage(file=f) for f in files]

buttons = []



for i in range(SIDE):
    for j in range(SIDE):
        btn = Button(main_window,
             #text=' ? ',
             #font=('Courier New', 12, 'normal'),
             image=images[i*SIDE+j],
             relief=FLAT)

        btn.configure(command=lambda b=btn: change(b))
        btn.img = images[i*SIDE+j]
        btn.x = files[i*SIDE+j]
        btn.grid(row=i, column=j)
        buttons.append(btn)


main_window.after(2000, hide_all, buttons)
main_window.after(10000, reset)
main_window.mainloop()

