import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
import json

# set color values
light_blue = '#b8eef5'
light_yellow = '#fcffd1'
darker_yellow = '#fcffd1'


# matplotlib logic
class PlotView:
    def __init__(self, file_name):
        self.file_name = file_name
        self.json_f = open(file_name)
        self.load_info()

    def load_info(self):
        info = json.load(self.json_f)
        plot_title = info['title']
        plot_line_label = info['label']
        y_data = info['data']['y']
        line_color = info['color']

        plt.plot(y_data, label=plot_line_label, color=line_color)
        plt.title(plot_title)
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.legend()
        plt.show()

        self.json_f.close()


# tkinter interface setup
class Root(tk.Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Linear plot")
        self.configure(background=light_blue)
        self.choose_label = tk.Label(text="Choose a JSON file:", background=light_blue, font=("MS Sans Serif", 14))
        self.choose_label.pack(padx=50, pady=(50, 25))
        self.br_button = None
        self.browse_button()
        self.file_name = None

    def browse_button(self):
        self.br_button = tk.Button(self, text="Browse", font=("MS Sans Serif", 12), command=lambda: self.open_file())
        self.br_button.configure(background=light_yellow, activebackground=darker_yellow)
        self.br_button.pack(pady=(0, 50))

    def open_file(self):
        self.file_name = filedialog.askopenfile(title='Search file')
        if self.file_name:
            new_plot = PlotView(self.file_name.name)


if __name__ == '__main__':
    root = Root()
    root.mainloop()
