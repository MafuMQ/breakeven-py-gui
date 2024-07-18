# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:22:14 2024

@author: Mafu
"""

import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


def show(x,y):
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Matplotlib in Tkinter")
    
    # Create a Matplotlib figure
    fig = Figure(figsize=(5, 4), dpi=100)
    t = fig.add_subplot(111)
    t.plot(x, y)
    
    # Create a canvas to draw the figure on
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    
    # Place the canvas on the Tkinter window
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    # Create a toolbar for the canvas
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    # Start the Tkinter main loop
    tk.mainloop()

#toplot = np.array([[0, 1, 2, 3, 4], [10, 1, 20, 3, 40]])
#show(toplot[0],toplot[1])