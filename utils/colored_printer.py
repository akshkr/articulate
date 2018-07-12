class ColorPrinter:
	
	def __init__(self):
		pass
	
	@staticmethod
	def print_colored(input_text):
		color_iter = 31
		for i in input_text:
			color_iter = color_iter + 1
			if color_iter == 38:
				color_iter = 31
			print("\033[1;%d;48m %s" %(color_iter, i), end = '')
			# iter_num += 1
