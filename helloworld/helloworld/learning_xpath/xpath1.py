from scrapy.selector import Selector

body = """
<html>
   <head>
      <title>Scrapy Tutorial By Cookie</title>
   </head>
   <body>
      <div class='links-div' name='haha'>This is div</div>
      <p>This is PPPPPPPP</p>
      <div class='links' name='haha'>
         <a href='one.html'>Link 1<img src='image1.jpg'/></a>
         <a href='two.html'>Link 2<img src='image2.jpg'/></a>
         <a href='three.html'>Link 3<img src='image3.jpg'/></a>
         <div class='div-1'>This is div1 div1 div1</div>
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
selector = Selector(text=body)

# 1. 从根节点搜索html
# 2. 以html为根节点,搜索body
# 3. 以body为根节点搜索div
tag_value = selector.xpath("/html/body/div").extract()  # 返回数组长度为 2  有两个div
print('selector.xpath("/html/body/div").extract() : ')
print(tag_value)

tag_value = selector.xpath("/html/body/div/text()").extract()[0]  # 数组中第一个div的内容  This is div
print('selector.xpath("/html/body/div/text()").extract()[0]')
print(tag_value)

# 从根节点搜索 <a> 标签,因为根节点只有<html>这个标签，所以搜索结果为空
tag_value = selector.xpath("/a").extract()  # 返回 []
print('selector.xpath("/a").extract()')
print(tag_value)

# 从全文搜索 <a> 标签，查询到3个结果
tag_value = selector.xpath("//a").extract()  # 返回 [<a>,<a>,<a>] 3个结果
print('selector.xpath("//a").extract()')
print(tag_value)





print('xxxxxxxx')
print('xxxxxxxx')
print('xxxxxxxx')
tag_value = selector.xpath("/a").extract()  # 返回数组长度为 2  有两个div
print(tag_value)

tag_value = selector.xpath("//ahtml/body/div").extract()[1]  # 从整个页面中搜索
print(tag_value)  # Get <title>Scrapy Tutorial By Cookie</title>

tag_value = selector.xpath("//title/text()").extract()  # 从整个页面中搜索
print(tag_value)  # Get <title>Scrapy Tutorial By Cookie</title>
