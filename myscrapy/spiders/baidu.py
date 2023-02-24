import scrapy

from myscrapy.items import BaiduItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        hotsearch = response.css('.hotsearch-item')
        for li in hotsearch:
            item = BaiduItem()
            item['name'] = li.css('.title-content-title::text').get()
            item['link'] = li.css('a::attr(href)').get()
            yield item
