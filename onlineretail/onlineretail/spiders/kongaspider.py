import scrapy


class KongaspiderSpider(scrapy.Spider):
    name = "kongaspider"
    allowed_domains = ["konga.com"]
    start_urls = ["https://konga.com"]

    def parse(self, response):
        pass
