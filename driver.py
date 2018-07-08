from utils.save_doc import DocSavar
# from utils.save_pdf import PdfSaver
from processor.content_scrapper import ContentScrapper
from utils.colored_printer import ColorPrinter
import warnings

warnings.filterwarnings("ignore")


class MainDriver:
	
	def __init__(self):
		self.start_screen_file = open('prompts/start_screen.txt', 'r+')
		self.connect_error_file = open('prompts/connection_error.txt', 'r+')
		self.user_text_input = ''
		self.content_sc = ContentScrapper()
		self.doc = DocSavar()
		# self.pdf_saver = PdfSaver()

		# Remove the comment below to start user input
		# self.article_maker()
	
	def user_input(self):
		try:
			start_screen_text = self.start_screen_file.readlines()
			ColorPrinter.print_colored(start_screen_text)
			print("\n\033[0;30;48m Enter the topics separated by commas : \n")
			user_text_input = input()
			return user_text_input
		except Exception as ex:
			print("Error Encountered while taking user input")
			print(ex)
			
	def article_maker(self, input_string = ""):
		try:
			if input_string == "":
				self.user_text_input = self.user_input()
			else:
				self.user_text_input = input_string
			result_json = self.content_sc.get_content(self.user_text_input)
			if result_json == 0:
				connection_error_txt = self.connect_error_file.readlines()
				ColorPrinter.print_colored(connection_error_txt)
				return
			f = self.doc.save_to_doc(result_json)
			return f
			# FIXME find another module to convert word to pdf as this module doesn't work in Linux
			# This is the help wanted issue raised on Github
			# self.pdf_saver.save_to_pdf(result_json)
		except Exception as ex:
			print("Error encountered while making article")
			print(ex)


if __name__ == "__main__":
	c = MainDriver()
