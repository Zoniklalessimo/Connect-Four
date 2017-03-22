class Team:
	def __init__(self, color, team_size):
		self.color = color
		self.team_size = team_size
		self.chips = list(list())

	def add_chip(self, x, y):
		self.chips.append([x, y])
		if self.test_win(x, y):
			return True
		else:
			return False
	
	def test_win(self, x, y, win_count=4):
		dirs = list([list(list()), list(list()), list(list()), list(list())])
		# for chip in self.chips:
		# 	if chip in zip([x+x_ for x_ in range(1, win_count)], [y-y_ for y_ in range(1, win_count)]):
		# 		dirs[0].append(chip)
		# 	elif chip in zip([x+x_ for x_ in range(1, win_count)], y):
		# 		dirs[1].append(chip)
		# 	elif chip in zip([x+x_ for x_ in range(1, win_count)], [y+y_ for y_ in range(1, win_count)]):
		# 		dirs[2].append(chip)
		# 	elif chip in zip(x, [y+y_ for y_ in range(1, win_count)]):
		# 		dirs[3].append(chip)
		# 	elif chip in zip([x-x_ for x_ in range(1, win_count)], [y+y_ for y_ in range(1, win_count)]):
		# 		dirs[4].append(chip)
		# 	elif chip in zip([x-x_ for x_ in range(1, win_count)], y):
		# 		dirs[5].append(chip)
		# 	elif chip in zip([x-x_ for x_ in range(1, win_count)], [y-y_ for y_ in range(1, win_count)]):
		# 		dirs[6].append(chip)
		# 	elif chip in zip(x, [y-y_ for y_ in range(1, win_count)]):
		# 		dirs[7].append(chip)

		x_line_pos = [x+x_ for x_ in range(1-win_count, win_count-1) if x_ != x]
		x_line_neg = [x+x_ for x_ in range(1-win_count, win_count-1) if x_ != x]
		y_line_pos = [y+y_ for y_ in range(1-win_count, win_count-1) if y_ != y]
		y_line_neg = [y-y_ for y_ in range(1-win_count, win_count-1) if y_ != y]
		for chip in self.chips:
			if chip in zip(x_line, y_line):
				dirs[0].append(chip)
			elif chip in zip(x_line_pos, y):
				dirs[1].append(chip)
			elif chip in zip(x_line_pos, y_line_neg):
				dirs[2].append(chip)
			elif chip in zip(x, y_line_pos):
				dirs[3].append(chip)

		win = list([list(), list(), list(), list()])
		for i in range(win_count-1):
			for k in dirs[0]:
				if k in zip(x_line_pos, y_line_neg):
					win[0].append(k)
			for k in dirs[1]:
				if k in zip(x_line_pos, y):
					win[1].append(k)
			for k in dirs[2]:
				if k in zip(x_line_pos, y_line_pos):
					win[2].append(k)
			for k in dirs[3]:
				if k in zip(x, y_line_pos):
					win[3].append(k)
		for i in win:
			if len(i) >= win_count-1:
				return i
