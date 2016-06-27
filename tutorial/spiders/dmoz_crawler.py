# -*- coding: utf-8 -*-

## In this example running the spider downloads the contents of the pages specified 
## defined by the urls in the class attribute 'start_urls', and writes the content to the 
## respective files.
##

from scrapy.spiders import CrawlSpider

from tutorial.items import DmozItem


class DmozSiteSpider(CrawlSpider):
	name = "dmoz-crawler"
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
		# expect 2 files to be created with the content of the respective urls;
		# Books.html & Resources.html
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
