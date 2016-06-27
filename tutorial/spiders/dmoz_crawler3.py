# -*- coding: utf-8 -*-

## This time instead of just scraping information from Books and Resources,
## ie.
## 	"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/", 
## 	"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
## we want everything that is under the Python directory.
##
## In order to do that, retrieve the links and follow them to extract the data.

from scrapy.spiders import CrawlSpider
from scrapy import Request as scrapy_request

from tutorial.items import DmozItem


class DmozSiteSpider(CrawlSpider):
	name = "dmoz-crawler3"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/"]

	def parse(self, response):
		""" This method only extracts the specified links from the page, 
		builds a full absolute URL using the response.urljoin method 
		(since the links can be relative) and yields new requests to be sent later. 
		Registering as callback the method parse_dir_contents() will ultimately 
		scrape the data we want.
		"""

		# specify on the page where the reuqired urls can be found using css selectors,
		# for sake ofexample, only interested in the 'Computers' sub-directory.
		for href in response.css("div.cat-item > a::attr('href')").extract():
			if href.startswith('/Computers'):
				url = response.urljoin(href)
				# print(url)

				# Scrapy’s mechanism of following links: when you yield a Request 
				# in a callback method, Scrapy will schedule that request to be sent 
				# and register a callback method to be executed when that request 
				# finishes.
				yield scrapy_request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		# extracting the data (xpath returns a list)
		for selector in response.xpath('//div[@class="title-and-desc"]'):
			title = selector.xpath('..//div[normalize-space(@class)="site-title"]/text()').extract()[0]
			link = selector.xpath('a/@href').extract()[0]
			desc = selector.xpath('div[normalize-space(@class)="site-descr"]/text()').extract()[0].strip()

			item = DmozItem()
			item['title'] = title
			item['link'] = link
			item['desc'] = desc
			yield item
