import nltk
import re
from urllib import urlopen


def process(urllist):
	rawdata_tokens_imp = []
	tokens_total = []
	for url in urllist:
		'''url = "http://www.indianexpress.com/news/tongue-chopped-off-docs-say \
		-pratapgarh-gangrape-victim-will-be-able-to-speak/1141589/"'''
		raw = urlopen(url).read()
		rawdata = nltk.clean_html(raw)
		re.findall(r'[\r\n]{4,}', rawdata)
		rawdata_tokens = nltk.word_tokenize(rawdata)
		rawdata_tokens_imp = [word.lower() for word in rawdata_tokens if len(word) > 2]
		rawdata_tokens_imp = rawdata_tokens_imp[200:700]
		rawdata_tokens_imp = filter(is_content_word, rawdata_tokens_imp)
		tokens_total += rawdata_tokens_imp
		print len(tokens_total)
		'''print rawdata_tokens_imp'''
	
	return tokens_total
	
def is_content_word(word):
	return word.lower() not in ['a', 'of', 'the', 'and', 'is', 'are', 'will', 'be' , 'to', 'so']
	
def clean_word(word):
	return word.strip('.')
	
		
		
		
	
	

	
