import tkinter
import random
canvas = tkinter.Canvas(width = 550, height = 290, bg='black')
canvas.pack()

cisla = ['31', '62', '125', '250', '500', '1K', '2K', '4K', '8K', '16K', '[Hz]']
zoznam_y = [None]*10

def hodnoty():
    x = 25
    for i in range(10):
        canvas.create_text(x, 275, text=cisla[i], font='Arial 10 bold', fill='limegreen')
        x += 50
    canvas.create_text(x, 275, text=cisla[i+1], font='Arial 10 bold',  fill='limegreen')

def ekvalizer():
    canvas.delete('stvorce')
    x1 = 10
    y1 = 260
    for i in range(10):
        nahoda = random.randint(10, 150)
        canvas.create_rectangle(x1, y1, x1+30, y1-(100+nahoda), fill='limegreen', outline='', tags='stvorce')
        if y1-(100+nahoda)<135:
            canvas.create_rectangle(x1, y1-135, x1+30, y1-(100+nahoda), fill='yellow', outline='', tags='stvorce')
        if y1-(100+nahoda)<73:
            canvas.create_rectangle(x1, y1-(100+nahoda), x1+30, y1-197, fill='red', outline='', tags='stvorce')
        x1 += 50
    canvas.after(500, ekvalizer)

hodnoty()
ekvalizer()

