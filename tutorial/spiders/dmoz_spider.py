import scrapy

from tutorial.items import DmozItem

class DmozSiteSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]

	# scrapy creates scrapy.Request object for each url in the start_urls attribute
	# and assigns them the parse method as the callback function.
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/", 
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

	def parse(self, response):
		""" This method is responsible for parsing the response data and extracting 
		the scraped data (as scraped items).
		"""
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)

