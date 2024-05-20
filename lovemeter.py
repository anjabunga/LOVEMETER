
#PROJEK UAS LOVEMETER
#ANJA BUNGA ADITYA
#2210511161 - S1 IF - D
from tkinter import *
from random import random

love = Tk()
love.geometry('400x260')
love.title('Love Meter')

#FUNCTION
def calculate():
    ranInt = random() * 100
    percent = round(ranInt)
    text = Text(love,  bg = "black", fg = "white", font = ("arial", 24, "bold"))
    text.insert(INSERT, percent, END, "%")
    text.pack()


# YOUR NAME
kolom1 = Label(love, text="Masukan nama Anda:")
kolom1.pack()
name1 = Entry(love, border=3, bg = "purple", font = ("Times New Roman", 10, "bold"), fg = "white")
name1.pack()

# PARTNER NAME
kolom2 = Label(love, text="Masukan nama pasangan Anda:")
kolom2.pack()
name2 = Entry(love, border=3, bg = "green",font = ("Times New Roman", 10, "bold"), fg = "white" )
name2.pack()

# CALCULATING BUTTON
button = Button(love, text="HITUNG!", height=1, width=9, command = calculate)
button.pack()

# TEXT RESULT
result = Label(love, text='\nLove percentage between both of you is:\n')
result.pack()


love.mainloop()
