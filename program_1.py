import tkinter


class GUIProgram:
    def __init__(self) -> None:
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text="Learn Vim!")
        self.label.pack(padx=100, pady=100)
        self.main_window.title("Tk GUI")
        tkinter.mainloop()


if __name__ == "__main__":
    program = GUIProgram()
