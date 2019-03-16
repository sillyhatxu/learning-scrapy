from scrapy.selector import Selector

body = """
<html>
   <head>
      <title>Scrapy Tutorial By Cookie</title>
   </head>
   <body>
      <div class='links-div' name='div-name1'>This is div</div>
      <p>This is PPPPPPPP</p>
      <div class='links' name='div-name2'>
         <a href='one.html'>Link 1<img src='image1.jpg'/></a>
         <a href='two.html'>Link 2<img src='image2.jpg'/></a>
         <a href='three.html'>Link 3<img src='image3.jpg'/></a>
         <div class='div-1'>This is div1 div1 div1</div>
      </div>
      <ul class='test-ul'>
         <li><a href='four.html'>Link 4</a></li>
         <li><a href='five.html'>Link 5</a></li>
      </ul>
      <div class='links' name='div-name3'>
         <a href='six.html'>Link 6</a>
         <a href='seven.html' name='a-h-name'>Link 7</a>
         <a href='eight.html'>Link 8</a>
         <li><a href='nine.html'>Link 9</a></li>
      </div>
   </body>
</html>
"""

# nodename	Selects all nodes with the name "nodename"
# /	        Selects from the root node
# //	    Selects nodes in the document from the current node that match the selection no matter where they are
# .	        Selects the current node
# ..	    Selects the parent of the current node
# @	        Selects attributes
# *	        匹配任何元素节点
# *@	    匹配任何属性节点
# |	        //book/title | //book/price 选取book所有title和price元素
selector = Selector(text=body)

# 1. 从根节点搜索html
# 2. 以html为根节点,搜索body
# 3. 以body为根节点搜索div
tag_value = selector.xpath("/html/body/div").extract()  # 返回数组长度为 2  有两个div
print('selector.xpath("/html/body/div").extract() : ')
print(tag_value)  # print -> ['<div class="links-div" name="haha">...', '<div class="links" name="haha">\n...</div>']
print("--------------------------------------------------------------------------------------------------------------")

tag_value = selector.xpath("/html/body/div/text()").extract()[0]  # 数组中第一个div的内容  This is div
print('selector.xpath("/html/body/div/text()").extract()[0]')
print(tag_value)  # print -> This is div
print("--------------------------------------------------------------------------------------------------------------")

# 从根节点搜索 <a> 标签,因为根节点只有<html>这个标签，所以搜索结果为空
tag_value = selector.xpath("/a").extract()  # 返回 []
print('selector.xpath("/a").extract()')
print(tag_value)  # print -> []
print("--------------------------------------------------------------------------------------------------------------")

# 获取 <div> 下的 <a> 和 <li> 下的 <a>
tag_value = selector.xpath("//div/a | //li/a").extract()
print('selector.xpath("//div/a | //li/a").extract()')
for index, tag in enumerate(tag_value):
    print(index, tag)
print("--------------------------------------------------------------------------------------------------------------")

# 从全文搜索 <a> 标签，查询到3个结果
tag_value = selector.xpath("//a").extract()  # 返回 [<a>,<a>,<a>] 3个结果
print('selector.xpath("//a").extract()')
print(tag_value)  # print -> ['<a href="one.html">', '<a href="two.html">', '<a href="three.html">']
print("--------------------------------------------------------------------------------------------------------------")

# 获取全文 <a> 中 href 的 属性值
print('for loop : selector.xpath("//a/@href").extract()')
for index, tag in enumerate(selector.xpath("//a/@href").extract()):
    print(index, tag)
# 0 one.html
# 1 two.html
# 2 three.html
# 3 four.html
# 4 five.html
# 5 six.html
# 6 seven.html
# 7 eight.html
# 8 nine.html
print("--------------------------------------------------------------------------------------------------------------")

# 从整个页面中搜索 <title> 标签，并取其中内容
tag_value = selector.xpath("//title/text()").extract()
print(tag_value)  # print -> ['Scrapy Tutorial By Cookie']
print("--------------------------------------------------------------------------------------------------------------")

# 从整个页面中搜索 <title> 标签，并取其中内容，并只取第一个元素
tag_value = selector.xpath("//title/text()").extract_first()
print(tag_value)  # print -> Scrapy Tutorial By Cookie
print("--------------------------------------------------------------------------------------------------------------")

# 从所有 <div> 中寻找 <a href="six.html"> 并取出内容
tag_value = selector.xpath('//div/a[@href="six.html"]/text()')
print(tag_value)    # print -> [<Selector xpath='//div/a[@href="six.html"]/text()' data='Link 6'>]
print(tag_value[0].extract())   # print -> Link 6
print("--------------------------------------------------------------------------------------------------------------")


# 取出最后一个 <div> 这一层子节点中所有 <a> 的href值
tag_value = selector.xpath('//div[last()]/a/@href').extract()
print(tag_value)    # print -> ['six.html', 'seven.html', 'eight.html']

# 取出最后一个 <div> 下所有 <a> 的href值
tag_value = selector.xpath('//div[last()]//a/@href').extract()
print(tag_value)    # print -> ['six.html', 'seven.html', 'eight.html', 'nine.html']

# 取出最后一个 <div> 下所有 <a> 的内容
tag_value = selector.xpath('//div[last()]//a/text()').extract()
print(tag_value)    # print -> ['Link 6', 'Link 7', 'Link 8', 'Link 9']
print("--------------------------------------------------------------------------------------------------------------")

# 取出最后一个 <div> 下所有最后一个 <a> 的内容和所有子标签中最后一个 <a> 的内容
tag_value = selector.xpath('//div[last()]//a[last()]/text()').extract()
print(tag_value)    # print -> ['Link 8', 'Link 9']
print("--------------------------------------------------------------------------------------------------------------")

# 取出最后一个 <div> 下最后一个 <a> 的内容
tag_value = selector.xpath('//div[last()]/a[last()]/text()').extract()
print(tag_value)    # print -> ['Link 8']
print("--------------------------------------------------------------------------------------------------------------")

# 取出最后一个 <div> 下最后一个 <a> 的父节点
tag_value = selector.xpath('//div[last()]/a[last()]/..').extract()
print(tag_value)    # print -> ['<div class="links" name="div-name3">\n   ...  </div>']
print("--------------------------------------------------------------------------------------------------------------")