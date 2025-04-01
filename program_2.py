# Programmer: Austin Long
# Date: 2025-04-01
# Program: Show info

import tkinter
import tkinter.messagebox

NAME = "Austin Long"
ADDRESS = "1234 April Fools Road Austin, TX"


class GUIProgram:
    def __init__(self) -> None:
        # create window
        self.main_window = tkinter.Tk()

        # create content frame
        self.main_frame = tkinter.Frame()

        # create button
        self.button = tkinter.Button(
            self.main_frame, text="Show info", command=self.show_info
        )
        self.button.pack()

        # create quit button
        self.button = tkinter.Button(
            self.main_frame, text="Quit", command=self.main_window.quit
        )
        self.button.pack()

        self.main_frame.pack(padx=100, pady=100)

        # set window title
        self.main_window.title("Show info program")

        # set minimum window size
        self.main_window.minsize(400, 300)

        # run program
        tkinter.mainloop()

    def show_info(self):
        tkinter.messagebox.showinfo("Info", f"Name: {NAME}\nAddress: {ADDRESS}")


if __name__ == "__main__":
    program = GUIProgram()
