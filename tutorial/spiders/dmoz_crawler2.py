# -*- coding: utf-8 -*-

## In this example scrape the specified data from the 2 urls defined and 
## populate the Items container.

from scrapy.spiders import CrawlSpider

from tutorial.items import DmozItem

class DmozSiteSpider(CrawlSpider):
	name = "dmoz-crawler2"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/", 
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

	def parse(self, response):
		""" This method is responsible for parsing the response data and extracting 
		the scraped data (as scraped items).
		"""
		# extracting the data (xpath return a list)
		for selector in response.xpath('//div[@class="title-and-desc"]'):
			title = selector.xpath('..//div[normalize-space(@class)="site-title"]/text()').extract()[0]
			link = selector.xpath('a/@href').extract()[0]
			desc = selector.xpath('div[normalize-space(@class)="site-descr"]/text()').extract()[0].strip()
			# print(title, "\n", link, "\n", desc, "\n")

			item = DmozItem()
			item['title'] = title
			item['link'] = link
			item['desc'] = desc
			yield item