import scrapy

class SinaNewsSpider(scrapy.Spider):

    name = 'blog-1'
    start_urls = [
        'http://xushikuan.com/2019/03/03/creating-a-new-theme/'
    ]

    def parse(self, response):
        print(response.url)
        # print(response.body)
        yield {
            'title':response.css('a.blog-header-logo::text').extract(),
            'sub-title':response.css('article.markdown-body').css('h2::text').extract(),
            'categories':response.css('nav.justify-content-between').css('a.p-2::text').extract(),
        }