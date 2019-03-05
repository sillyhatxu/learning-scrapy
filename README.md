# learning-scrapy

> install
```
pip install scrapy
```

> create project
```
scrapy startproject helloworld
```

> start
```
cd helloworld
scrapy crawl sina_news
scrapy runspider learning2.py
scrapy runspider learning3.py -o learning3.json
```

> parse
```
BeautifulSoup
```

```
scrapy shell http://xushikuan.com/2019/03/03/creating-a-new-theme/

print(response.text)

response.css('div.main-nav')

response.css('div.main-nav').extract()
response.css('div.main-nav').extract_first()
response.css('div.main-nav::text').extract_first()
```

> response.css('{label}.{class}')
```
>>> response.css('div.p-3')
[<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' p-3 ')]" data='<div class="p-3">\n    <h4 class="font-it'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' p-3 ')]" data='<div class="p-3">\n    <h4 class="font-it'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' p-3 ')]" data='<div class="p-3 mb-3 bg-light rounded">\n'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' p-3 ')]" data='<div class="p-3">\n        <h4 class="fon'>]
>>> response.css('div.p-3').extract()
['<div class="p-3">\n    <h4 class="font-italic">Tags</h4>\n    <ol class="list-unstyled mb-0">\n        \n        <li><a href="http://xushikuan.com/tags/algorithm">algorithm</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/blog">blog</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/consul">consul</a>(2)</li>\n        \n        <li><a href="http://xushikuan.com/tags/docker">docker</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/elasticsearch">elasticsearch</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/elk">elk</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/english">english</a>(7)</li>\n        \n        <li><a href="http://xushikuan.com/tags/git">git</a>(2)</li>\n        \n        <li><a href="http://xushikuan.com/tags/gitlab">gitlab</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/golang">golang</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/html">html</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/hugo">hugo</a>(2)</li>\n        \n        <li><a href="http://xushikuan.com/tags/java">java</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/markdown">markdown</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/movie">movie</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/mysql">mysql</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/nginx">nginx</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/operation">operation</a>(2)</li>\n        \n        <li><a href="http://xushikuan.com/tags/python">python</a>(19)</li>\n        \n        <li><a href="http://xushikuan.com/tags/record">record</a>(2)</li>\n        \n        <li><a href="http://xushikuan.com/tags/redis">redis</a>(1)</li>\n        \n        <li><a href="http://xushikuan.com/tags/scjp">scjp</a>(1)</li>\n        \n    </ol>\n</div>', '<div class="p-3">\n    <h4 class="font-italic">Archives</h4>\n    <ol class="list-unstyled mb-0">\n        \n        <a href="http://xushikuan.com/archives/2019">2019</a> (24)<br>\n        \n        <a href="http://xushikuan.com/archives/2018">2018</a> (12)<br>\n        \n        <a href="http://xushikuan.com/archives/2017">2017</a> (8)<br>\n        \n        <a href="http://xushikuan.com/archives/2016">2016</a> (1)<br>\n        \n    </ol>\n</div>', '<div class="p-3 mb-3 bg-light rounded">\n    <h4 class="font-italic">About</h4>\n    <p class="mb-0">Etiam porta <em>sem malesuada magna</em> mollis euismod. Cras mattis consectetur purus\n        sit amet fermentum. Aenean lacinia bibendum nulla sed consectetur.</p>\n</div>', '<div class="p-3">\n        <h4 class="font-italic">Elsewhere</h4>\n        <ol class="list-unstyled">\n            <li><a href="#">GitHub</a></li>\n            <li><a href="#">Twitter</a></li>\n            <li><a href="#">Facebook</a></li>\n        </ol>\n    </div>']
```
> response.css('{label}.{class}::text')
```
>>> response.css('div.p-3').css('a::text').extract()
['algorithm', 'blog', 'consul', 'docker', 'elasticsearch', 'elk', 'english', 'git', 'gitlab', 'golang', 'html', 'hugo', 'java', 'markdown', 'movie', 'mysql', 'nginx', 'operation', 'python', 'record', 'redis', 'scjp', '2019', '2018', '2017', '2016', 'GitHub', 'Twitter', 'Facebook']
```
> out to file

```
scrapy crawl blog -o items.json
```

> get url
```
<h2 class="blog-post-title">
    <a href="http://xushikuan.com/2019/03/01/learning-python-02/">Learning Python 02</a>
</h2>
```

```
>>> response.css('h2.blog-post-title > a::attr(href)').extract()
'http://xushikuan.com/2019/03/01/learning-python-02/'
>>> 
```

> json.loads
```
data = json.loads(response.text)
```
