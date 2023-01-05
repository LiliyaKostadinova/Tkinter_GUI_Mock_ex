import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import json


def load_info(file_name):
    """Load info from chosen JSON file and parse it to get data about the plot"""
    json_f = open(file_name)

    info = json.load(json_f)
    plot_title = info['title']
    plot_line_label = info['label']
    y_data = info['data']['y']
    line_color = info['color']

    json_f.close()
    return json_f, info, plot_title, plot_line_label, y_data, line_color


# Tkinter interface setup
class Root(tk.Tk):
    """Handle the initial window by using Tkinter for visualization"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.geometry('800x700')
        self.text_style = ttk.Style()
        self.text_style.configure('text_style.TLabel', font=('Helvetica', 12))
        self.title('Linear plot')

        self.choose_label = ttk.Label(text='Choose a JSON file:', style='text_style.TLabel')
        self.choose_label.pack(padx=50, pady=(50, 25))

        self.br_button = self.browse_button()
        self.file_name = ''

        self.legend_pos = 'upper left'
        self.canvas = None
        self.combobox = None

    def browse_button(self):
        """Create a button that calls a browse-file functionality on click"""
        self.text_style.configure('text_style.TButton', font=('Helvetica', 10))
        self.br_button = ttk.Button(self, text='Browse', style='text_style.TButton', command=self.open_file)
        self.br_button.pack(pady=(0, 50))
        return self.br_button

    def open_file(self):
        """Handle file browsing, pass the file path by initiating an instance of PlotView class"""
        self.file_name = filedialog.askopenfile(title='Search file')
        if self.file_name:
            self.draw_plot();

    def draw_plot(self):
        """Handle embedding the matplotlib graph to the tkinter window"""
        # Get the parsed necessary data
        json_f, info, plot_title, plot_line_label, y_data, line_color = load_info(self.file_name.name)

        # Draw the matplotlib graph
        figure, axis = plt.subplots()
        self.canvas = FigureCanvasTkAgg(figure, self)

        axis.plot(y_data, label=plot_line_label, color=line_color)
        plt.title(plot_title)
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        self.draw_toolbar()

    def draw_toolbar(self):
        """Draw toolbar with matplotlib tools and a dropdown at the bottom of the window"""
        # Add a drop-down (combobox)
        self.combobox = ttk.Combobox(self, state='readonly',
                                     values=['upper left', 'upper right', 'lower left', 'lower right'])
        self.combobox.bind("<<ComboboxSelected>>", self.change_legend_pos)
        self.combobox.set('upper left')
        self.combobox.pack(side=tk.BOTTOM, pady=(0, 15))

        # Add a Toolbar to the matplotlib graph
        mat_toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        mat_toolbar.pack(side=tk.BOTTOM, fill=tk.X)

        plt.legend(loc=self.legend_pos)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.draw()

    def change_legend_pos(self, event):
        """Change the position of the legend based on the chosen option in the dropdown menu (combobox)"""
        self.legend_pos = self.combobox.get()
        plt.legend(loc=self.legend_pos)
        self.canvas.draw()


if __name__ == '__main__':
    """Run the program by starting the Tkinter interface"""
    root = Root()
    root.mainloop()
