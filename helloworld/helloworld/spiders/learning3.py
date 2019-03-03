import scrapy


class SinaNewsSpider(scrapy.Spider):
    name = 'blog-2'
    allowed_domains = ["xushikuan.com"]
    start_urls = [
        'http://xushikuan.com/'
    ]

    def parse(self, response):
        print(response.url)
        self.log(response.url)
        for url in response.css('h2.blog-post-title > a::attr(href)').extract():
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_detail)

        # next page
        next_page_url = response.css('nav.blog-pagination > a.btn-outline-secondary::attr(href)').extract_first()
        self.log("next page url : " + str(next_page_url))
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detail(self,response):
        yield {
            'title':response.css('div.blog-main > h3::text').extract_first(),
            'tags':response.css('div.blog-main > span.badge > a::text').extract(),
        }
