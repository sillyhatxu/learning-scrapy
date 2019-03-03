import scrapy
import lxml.html

class SinaNewsSpider(scrapy.Spider):

    name = 'sina_news'
    start_urls = [
        'https://news.sina.com.cn/'
    ]

    def parse(self, response):
        print("-------")
        root = lxml.html.fromstring(response)
        print(root)
        print("-------")
        # print(response.url)
        # print(response.body)
        # tags = response.selector.xpath('//a').get()
        # for tag in tags:
        #     print(tag)