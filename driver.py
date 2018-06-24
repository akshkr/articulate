from utils.save_doc import DocSavar
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
		self.article_maker()
	
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
			
	def article_maker(self):
		try:
			self.user_text_input = self.user_input()
			result_json = self.content_sc.get_content(self.user_text_input)
			if result_json == 0:
				connection_error_txt = self.connect_error_file.readlines()
				ColorPrinter.print_colored(connection_error_txt)
				return
			self.doc.save_to_doc(result_json)
		except Exception as ex:
			print("Error encountered while making article")
			print(ex)


if __name__ == "__main__":
	c = MainDriver()
