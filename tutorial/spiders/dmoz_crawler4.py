# -*- coding: utf-8 -*-

## This time instead of just scraping information from Books and Resources,
## ie.
## 	"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/", 
## 	"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
## we want every sub category that is under the Python directory.
##
## This time however, we use a link extractor to get the links to follow and 
## extract the data.

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from tutorial.items import DmozItem


class DmozSiteSpider(CrawlSpider):
	name = "dmoz-crawler4"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/"]
	custom_settings = {
		'BOT_NAME': 'dmoz-scraper',
		'DEPTH_LIMIT': 2,	
		'DOWNLOAD_DELAY': 1	
		}
	rules = [
		Rule(
			LinkExtractor(allow=["/Computers/Programming/Languages/Python/"]), 
			callback='parse_category',
			follow=True
			)
		]

	def parse_category(self, response):
		for selector in response.xpath('//div[@class="title-and-desc"]'):
			title = selector.xpath('..//div[normalize-space(@class)="site-title"]/text()').extract()[0]
			link = selector.xpath('a/@href').extract()[0]
			desc = selector.xpath('div[normalize-space(@class)="site-descr"]/text()').extract()[0].strip()

			item = DmozItem()
			item['title'] = title
			item['link'] = link
			item['desc'] = desc
			yield item
