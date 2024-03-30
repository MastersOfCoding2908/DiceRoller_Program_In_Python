
# Master's Of Coding
# @mastersofcoding2908
# Please Don't Forget To Like And Subscribe.
# Source Code is available on GitHub.

# Dice Rolling Program.
# This program has higher probablity of getting 6 number on dice.
# Display Images using tkinter GUI.
# Modules
from tkinter import *
import random
# Random Number Selector And randNum value changer.
"""If you want to make this dice roller probablity. 
equal to other number probablity the remove this code."""
randNum = random.randint(1,6)
rand_num_higher_probablity = random.randint(1,6)

if rand_num_higher_probablity ==random.randint(1,6) or rand_num_higher_probablity ==random.randint(1,6):
 randNum = 6
###################################################################################
def randnumber(x):
 k = Tk()
 k.geometry("500x500")
 photo = PhotoImage(file= fr"dice {x}.png")

 img_label = Label(image=photo)
 img_label.pack()
 k.after(800, lambda: k.destroy())
 k.mainloop()

randnumber(randNum)

# Thank You For Watching This Video