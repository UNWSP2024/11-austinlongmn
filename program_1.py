# Programmer: Austin Long
# Date: 2025-04-01
# Program: GUI Message

import tkinter


class GUIProgram:
    def __init__(self) -> None:
        # create window
        self.main_window = tkinter.Tk()

        # create label
        self.label = tkinter.Label(self.main_window, text="Learn Vim!")
        self.label.pack(ipadx=100, ipady=100)

        # set window title
        self.main_window.title("Inspirational Message")

        # run program
        tkinter.mainloop()


if __name__ == "__main__":
    program = GUIProgram()
