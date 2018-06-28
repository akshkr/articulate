"""HELP WANTED ISSUE ON GITHUB FILE"""
import os
import comtypes
from utils.save_doc import DocSavar


class PdfSaver:
	
	def __init__(self):
		self.docsaver = DocSavar()
	
	def save_to_pdf(self, input_json):
		try:
			wdFormatPDF = 17
			doc_name = self.docsaver.save_to_doc(input_json, True)
			word = comtypes.client.CreateObject('Word.Application')
			doc_object = word.Documents.Open(doc_name)
			doc_object.SaveAs("mypdf.pdf", FileFormat=wdFormatPDF)
			doc_object.close()
			word.Quit()
			os.remove(doc_name)
			
		except Exception as ex:
			print("Error")
