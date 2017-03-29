#Liguster meine Freunde

import tkinter as tk
dimens = [None, None]

class Grid(tk.Frame):
	def __init__(self, rows, columns, master=None):
		super().__init__(master)
		self.master.title("Connect Four!")
		dimens[0] = rows 
		dimens[1] = columns
		self.init_widgets(dimens)
		self.pack()

	def init_widgets(self, dimens):
		c_height = dimens[0] * 80
		c_width = dimens[1] * 80
		canvas = tk.Canvas(self, width=c_width, height=c_height)
		canvas.pack()
		for i in range(dimens[0]):
			vert_lines = canvas.create_line(0, c_height / dimens[1], c_width, c_height / dimens[1])
			if dimens[1] >= 2:
				dimens[1] -= 1
			
                                
