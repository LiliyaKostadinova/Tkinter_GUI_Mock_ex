import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
import json

# Set color values
LIGHT_BLUE = '#e3f8fb'


# Matplotlib logic
class PlotView:
    """A class that handles parsing the JSON file and visualizing the graph"""
    def __init__(self, file_name):
        """Getting the file path, opening it and calling a method to load the information"""
        self.file_name = file_name
        self.json_f = open(file_name)
        self.load_info()

    def load_info(self):
        """Loading data from the file, parsing it to according variables, calling а method to visualize the plot"""
        info = json.load(self.json_f)
        plot_title = info['title']
        plot_line_label = info['label']
        y_data = info['data']['y']
        line_color = info['color']
        self.show_plot(plot_title, y_data, plot_line_label, line_color)

    def show_plot(self, plot_title, y_data, plot_line_label, line_color):
        """Visualizing plot using matplotlib, closing file"""
        plt.plot(y_data, label=plot_line_label, color=line_color)
        plt.title(plot_title)
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.legend()
        plt.show()

        self.json_f.close()


# Tkinter interface setup
class Root(tk.Tk):
    """A class that handles the initial window by using Tkinter for visualizing"""
    def __init__(self):
        """Setting up font styles, titles and elements"""
        super(Root, self).__init__()
        self.configure(background=LIGHT_BLUE)
        self.lab_text_style = ttk.Style()
        self.lab_text_style.configure('text_style.TLabel', font=('Helvetica', 12), background=LIGHT_BLUE)
        self.btn_text_style = ttk.Style()
        self.btn_text_style.configure('text_style.TButton', font=('Helvetica', 10))
        self.title('Linear plot')
        self.choose_label = ttk.Label(text='Choose a JSON file:', style='text_style.TLabel')
        self.choose_label.pack(padx=50, pady=(50, 25))
        self.br_button = self.browse_button()
        self.file_name = None

    def browse_button(self):
        """Creating a button that calls a browse-file functionality on click"""
        self.br_button = ttk.Button(self, text='Browse', style='text_style.TButton', command=self.open_file)
        self.br_button.pack(pady=(0, 50))
        return self.br_button

    def open_file(self):
        """Handling file browsing, passing the file path by initiating an instance of PlotView class"""
        self.file_name = filedialog.askopenfile(title='Search file')
        if self.file_name:
            new_plot = PlotView(self.file_name.name)


if __name__ == '__main__':
    """Running the program by starting the Tkinter interface"""
    root = Root()
    root.mainloop()
