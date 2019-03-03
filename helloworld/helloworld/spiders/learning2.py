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
        for blog in response.css('div.post-preview'):
            item = {
                'title': blog.css('h2.blog-post-title').css('a::text').extract_first(),
                'author': blog.css('p.blog-post-meta::text').extract_first().replace("Posted by ", "")[0:9],
                'date': blog.css('p.blog-post-meta::text').extract_first().replace("Posted by ", "").replace(
                    blog.css('p.blog-post-meta::text').extract_first().replace("Posted by ", "")[0:10], ""),
            }
            yield item

        # next page
        next_page_url = response.css('nav.blog-pagination > a.btn-outline-secondary::attr(href)').extract_first()
        self.log("next page url : " + str(next_page_url))
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

