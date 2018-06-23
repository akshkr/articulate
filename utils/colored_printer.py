class ColorPrinter:
	
	def __init__(self):
		pass
	
	@staticmethod
	def print_colored(input_text):
		color_iter = 31
		iter_num = 0
		change_color = int(len(input_text) / 7)
		for i in input_text:
			if iter_num == change_color:
				iter_num = 0
				color_iter += 1
			print("\033[1;%d;48m %s" %(color_iter, i), end = '')
			iter_num += 1
