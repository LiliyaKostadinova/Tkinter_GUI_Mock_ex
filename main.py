import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
import json

# Set color values
LIGHT_BLUE = '#e3f8fb'


# Matplotlib logic
class PlotView:
    """Handle parsing the JSON file and visualize the graph"""
    def __init__(self, file_name):
        """Constructor"""
        self.file_name = file_name
        self.json_f = open(file_name)
        self.load_info()

    def load_info(self):
        """Load data from the file, parse it to according variables, call a method to visualize the plot"""
        info = json.load(self.json_f)
        plot_title = info['title']
        plot_line_label = info['label']
        y_data = info['data']['y']
        line_color = info['color']
        self.show_plot(plot_title, y_data, plot_line_label, line_color)

    def show_plot(self, plot_title, y_data, plot_line_label, line_color):
        """Visualize plot using matplotlib, close file"""
        plt.plot(y_data, label=plot_line_label, color=line_color)
        plt.title(plot_title)
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.legend()
        plt.show()

        self.json_f.close()


# Tkinter interface setup
class Root(tk.Tk):
    """Handle the initial window by using Tkinter for visualization"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.configure(background=LIGHT_BLUE)
        self.text_style = ttk.Style()
        self.text_style.configure('text_style.TLabel', font=('Helvetica', 12), background=LIGHT_BLUE)
        self.title('Linear plot')

        self.choose_label = ttk.Label(text='Choose a JSON file:', style='text_style.TLabel')
        self.choose_label.pack(padx=50, pady=(50, 25))

        self.br_button = self.browse_button()
        self.file_name = None

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
            new_plot = PlotView(self.file_name.name)


if __name__ == '__main__':
    """Run the program by starting the Tkinter interface"""
    root = Root()
    root.mainloop()
