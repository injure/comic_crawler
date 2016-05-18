import scrapy

class InfinityComicSpider(scrapy.Spider):
    name = '8comic'
    allowed_domains = ['comicbus.com', '8comic.com']
    start_urls = ['http://www.comicbus.com/comic/h-1.html']

    def parse(self, response):
        results = response.xpath('//a[@class="blue"]/b/text()').extract()
        for result in results:
            print result.encode('utf-8')