# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:42:49 2024

@author: Mafu
"""

import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

class BreakEvenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Break-Even Point Calculator")
        
        # Initial Investment
        self.initial_investment_label = ttk.Label(root, text="Initial Investment:")
        self.initial_investment_label.grid(row=0, column=0, padx=10, pady=10)
        self.initial_investment_entry = ttk.Entry(root)
        self.initial_investment_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Profit
        self.profit_label = ttk.Label(root, text="Profit:")
        self.profit_label.grid(row=1, column=0, padx=10, pady=10)
        self.profit_entry = ttk.Entry(root)
        self.profit_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Profit Type (Annual/Monthly)
        self.profit_type_label = ttk.Label(root, text="Profit Type:")
        self.profit_type_label.grid(row=2, column=0, padx=10, pady=10)
        self.profit_type = tk.StringVar()
        self.profit_type.set("Annual")
        self.profit_type_annual = ttk.Radiobutton(root, text="Annual", variable=self.profit_type, value="Annual")
        self.profit_type_annual.grid(row=2, column=1, padx=10, pady=10, sticky='W')
        self.profit_type_monthly = ttk.Radiobutton(root, text="Monthly", variable=self.profit_type, value="Monthly")
        self.profit_type_monthly.grid(row=2, column=1, padx=10, pady=10, sticky='E')
        
        # Calculate Button
        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_break_even)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # Break-Even Result
        self.break_even_result_label = ttk.Label(root, text="Break-Even Period: ")
        self.break_even_result_label.grid(row=4, column=0, padx=10, pady=10)
        self.break_even_result_value = ttk.Label(root, text="")
        self.break_even_result_value.grid(row=4, column=1, padx=10, pady=10)
        
        # Canvas for Matplotlib
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Toolbar for Matplotlib
        self.toolbar_frame = ttk.Frame(root)
        self.toolbar_frame.grid(row=6, column=0, columnspan=2)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def calculate_break_even(self):
        try:
            initial_investment = float(self.initial_investment_entry.get())
            profit = float(self.profit_entry.get())
            profit_type = self.profit_type.get()
            
            if profit_type == "Monthly":
                periods = initial_investment / profit
                time_unit = "Months"
                period_label = f"{periods:.2f} Months"
                x = np.arange(1, int(periods) + 12)
            else:
                periods = initial_investment / profit
                time_unit = "Years"
                period_label = f"{periods:.2f} Years"
                x = np.arange(1, int(periods) + 2)
            
            y = profit * x
            roi = y - initial_investment  # ROI calculation
            
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y, label="Accumulated Profit")
            ax.plot(x, roi, label="ROI", linestyle='-.')
            ax.axhline(y=initial_investment, color='r', linestyle='--', label="Initial Investment")
            ax.axvline(x=periods, color='g', linestyle='--', label="Break-Even Point")
            ax.set_xlabel(time_unit)
            ax.set_ylabel('Amount')
            ax.set_title('Break-Even Analysis')
            ax.legend()
            
            self.canvas.draw()
            
            # Update the break-even result label
            self.break_even_result_value.config(text=period_label)
        except ValueError:
            tk.messagebox.showerror("Input Error", "Please enter valid numbers for Initial Investment and Profit")

if __name__ == "__main__":
    root = tk.Tk()
    app = BreakEvenApp(root)
    root.mainloop()
