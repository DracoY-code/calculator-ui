import tkinter as tk

from modules.calculator import Calculator


class App(tk.Frame):
    def __init__(self, master: tk.Tk | None = None) -> None:
        super(App, self).__init__(master)
        self.calculator: Calculator = Calculator()

        self.master: tk.Tk | None = master
        if self.master is not None:
            self.master.title('Calulator: tkinter')

        self.screen: tk.Label | None = None
        self.button: tk.Button | None = None
        self.button_clr: tk.Button | None = None
        self.button_eq: tk.Button | None = None
        self.frames: list[tk.Frame] = [
            tk.Frame(master=self.master)
            for _ in range(5)
        ]
        self.pack()
        self.create_widgets()

    def create_widgets(self) -> None:
        self.screen = tk.Label(
            master=self.frames[0],
            width=27,
            height=2,
            foreground='white',
            background='black',
            anchor='e',
            font=('Arial', 20),
		)
        self.screen.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.button_clr = tk.Button(
            master=self.frames[0],
            text='Clear',
            width=5,
            height=9,
            fg='black',
            bg='white',
        )
        self.button_clr.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.button_clr.bind('<Button-1>', self.handle_keypress)

        for key in self.calculator.keys:
            if key in '0147':
                self.button = tk.Button(master=self.frames[1])
            elif key in '.258':
                self.button = tk.Button(master=self.frames[2])
            elif key in '=369':
                self.button = tk.Button(master=self.frames[3])
            elif key in '+-*/':
                self.button = tk.Button(master=self.frames[4])
            else:
                continue
            self.button['text'] = key
            self.button['width'] = 4
            self.button['height'] = 2
            self.button['fg'] = 'black'
            self.button['bg'] = 'white'
            self.button.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
            self.button.bind('<Button-1>', self.handle_keypress)

        for frame in self.frames:
            frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    def handle_keypress(self, event: tk.Event) -> None:
        if self.screen is None:
            return
        
        if event.widget == self.button_clr:
            self.calculator.clear()
        elif event.widget['text'] == '=':
            self.calculator.solve()
        else:
            self.calculator.display(event.widget['text'])
        self.screen['text'] = self.calculator.result


if __name__ == '__main__':
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
