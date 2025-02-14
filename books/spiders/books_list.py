import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksListSpider(CrawlSpider):
    name = "books_list"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    rules = (Rule(LinkExtractor(restrict_xpaths= "//article[@class= 'product_pod']/h3/a"), callback="parse_item", follow=True),
             (Rule(LinkExtractor(restrict_xpaths= "///li[@class= 'next']/a")))
    )
    

    def parse_item(self, response):
        yield{
            'title': response.xpath("//div[@class= 'col-sm-6 product_main']/h1/text()").get(),
            'price': response.xpath("//div[@class= 'col-sm-6 product_main']/p[@class='price_color']/text()").get()

        }