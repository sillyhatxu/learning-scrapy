import scrapy

class SinaNewsSpider(scrapy.Spider):
    name = 'get-world-detail'
    start_urls = [
        'http://www.manythings.org/vocabulary/lists/l/words.php?f=ogden'
    ]

    def parse(self, response):
        title = response.css('div.main > h2::text').extract_first()
        words = list()
        for ul in response.css('div.wrapco > div.co'):
            for li in ul.css('ul > li'):
                word = li.css('li::text').extract_first()
                words.append(word)
                self.log(word)
        yield {
            'title':title,
            'words':words,
        }