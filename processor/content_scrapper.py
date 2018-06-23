import requests
import wikipedia


class ContentScrapper:
	
	def __init__(self):
		self.return_json = {}
	
	def get_content(self, topics):
		
		all_topics = topics.split(",")
		for each_topic in all_topics:
			try:
				para = wikipedia.summary(each_topic, sentences=100)
			except wikipedia.exceptions.DisambiguationError as e:
				para = wikipedia.summary(e.options[0], sentences=100)
			except requests.exceptions.ConnectionError as e:
				return 0
			self.return_json[each_topic] = para
			
		return self.return_json
