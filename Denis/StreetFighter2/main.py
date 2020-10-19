# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *

def createWindow():
    tk = Tk()
    background = tk.PhotoImage("assets/start.png")
    background_label = tk.Label(background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    tk.mainloop()


def main():
    createWindow()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
