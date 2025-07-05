import scrapy


class AmazonspiderSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://amazon.com"]

    def parse(self, response):
        pass
