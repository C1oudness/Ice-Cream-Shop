from tkinter import *


def btn_click():
    if choice.get() == 1 and choice1.get() == 4:
        lab2["text"]='Ви вибрали ванільне морозиво у маленькому ріжку'
    if choice.get() == 1 and choice1.get() == 5:
        lab2["text"]='Ви вибрали ванільне морозиво у середньому ріжку'
    if choice.get() == 1 and choice1.get() == 6:
        lab2["text"]='Ви вибрали ванільне морозиво у великому ріжку'
    if choice.get() == 2 and choice1.get() == 4:
        lab2["text"]='Ви вибрали шоколадне морозиво у маленькому ріжку'
    if choice.get() == 2 and choice1.get() == 5:
        lab2["text"]='Ви вибрали шоколадне морозиво у середньому ріжку'
    if choice.get() == 2 and choice1.get() == 6:
        lab2["text"]='Ви вибрали шоколадне морозиво у великому ріжку'
    if choice.get() == 3 and choice1.get() == 4:
        lab2["text"]='Ви вибрали фруктове морозиво у маленькому ріжку'
    if choice.get() == 3 and choice1.get() == 5:
        lab2["text"]='Ви вибрали фруктове морозиво у середньому ріжку'
    if choice.get() == 3 and choice1.get() == 6:
        lab2["text"]='Ви вибрали фруктове морозиво у великому ріжку'


root = Tk()
root.geometry('400x400')
root.title('Магазин морозива')

lab = Label(text='Оберіть тип морозива:', font='Calibri 11 bold')
lab.pack(pady=5)

choice = IntVar()
switch1 = Radiobutton(text='Ванільне', variable=choice, value=1, command=btn_click)
switch1.pack(pady=5)
switch2 = Radiobutton(text='Шоколадне', variable=choice, value=2, command=btn_click)
switch2.pack(pady=5)
switch3 = Radiobutton(text='Фруктове', variable=choice, value=3, command=btn_click)
switch3.pack(pady=5)

lab1 = Label(text='Оберіть розмір ріжку:', font='Calibri 11 bold')
lab1.pack(pady=5)

choice1 = IntVar()
switch4 = Radiobutton(text='Маленький', variable=choice1, value=4, command=btn_click)
switch4.pack(pady=5)
switch5 = Radiobutton(text='Середній', variable=choice1, value=5, command=btn_click)
switch5.pack(pady=5)
switch6 = Radiobutton(text='Великий', variable=choice1, value=6, command=btn_click)
switch6.pack(pady=5)

lab2 = Label(text='')
lab2.pack(pady=5)

root.mainloop()
