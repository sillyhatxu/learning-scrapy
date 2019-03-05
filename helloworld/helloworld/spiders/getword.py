import scrapy

class SinaNewsSpider(scrapy.Spider):
    name = 'get-world'
    start_urls = [
        'http://www.manythings.org/vocabulary/lists/l/'
    ]

    def parse(self, response):
        for ul in response.css('div.main > ul'):
            # for url in ul.css('li > a::attr(href)').extract_first():
            for url in ul.css('li > a::attr(href)').extract():
                url = response.urljoin(url)
                yield scrapy.Request(url=url, callback=self.parse_detail)


    def parse_detail(self,response):
        title = response.css('div.main > h2::text').extract_first()
        words = list()
        for ul in response.css('div.wrapco > div.co'):
            word = ul.css('ul > li').extract_first()
            yield {
                'word':word,
            }
