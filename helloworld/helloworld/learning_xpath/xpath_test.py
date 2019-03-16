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
      <ul class="postList">
        <li name="aaa-aaa" id="aaa">writers cannot be starved</li>
        <li name="bbb-bbb" id="bbb">readers cannot be starved</li>
        <li name="ccc-ccc" id="ccc">no thread shall be allowed to starve</li>
        <li><a href='xxx1.html'>xxx-content-1</a></li>
        <li><a href='xxx2.html'>xxx-content-2</a></li>
        <div class='links' name='div-name3'>
            <a href='six.html'>Link 6</a>
            <a href='seven.html' name='a-h-name'>Link 7</a>
            <a href='eight.html'>Link 8</a>
            <li><a href='nine.html'>Link 9</a></li>
        </div>
        <li><a href='xxx3.html'>xxx-content-3</a></li>
        <li><a href='xxx4.html'>xxx-content-4</a></li>
        <li><a href='xxx5.html'>xxx-content-5</a></li>
        <li><a href='xxx6.html'>xxx-content-6</a></li>
        <li><a href='xxx7.html'>xxx-content-7</a></li>
      </ul>
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


# 找出 <div name='div-name2'> 下所有的 子元素,包括 换行符

# 取出 <div name='div-name2'> 这个元素的name -> div
tag_value = selector.xpath("//div[@name='div-name2']")
print(tag_value.xpath("name()").extract())  # print ['div']


# print -> ['\n         Link 1\n         Link 2\n         Link 3\n         This is div1 div1 div1\n      ']

# tag_value = selector.xpath("//div[@name='div-name2']/string(.)").extract()
# print(tag_value)

# for index, tag in enumerate(tag_value):
#     print(index, tag)
# 0   这里其实有换行符
# 1 <a href="one.html">Link 1<img src="image1.jpg"></a>
# 2   这里其实有换行符
# 3 <a href="two.html">Link 2<img src="image2.jpg"></a>
# 4   这里其实有换行符
# 5 <a href="three.html">Link 3<img src="image3.jpg"></a>
# 6   这里其实有换行符
# 7 <div class="div-1">This is div1 div1 div1</div>
# 8   这里其实有换行符
print("--------------------------------------------------------------------------------------------------------------")





tag_value = selector.xpath("//ul/child::*")
for index, tag in enumerate(tag_value):
    # print(index, tag)
    print(tag.xpath('node()/text()').extract())
    # print(tag.xpath('..'))
# 0 <li name="aaa-aaa" id="aaa">writers cannot be starved</li>
# 1 <li name="bbb-bbb" id="bbb">readers cannot be starved</li>
# 2 <li name="ccc-ccc" id="ccc">no thread shall be allowed to starve</li>
# 3 <li><a href="xxx1.html">xxx-content-1</a></li>
# 4 <li><a href="xxx2.html">xxx-content-2</a></li>
# 5 <div class="links" name="div-name3">
#             <a href="six.html">Link 6</a>
#             <a href="seven.html" name="a-h-name">Link 7</a>
#             <a href="eight.html">Link 8</a>
#             <li><a href="nine.html">Link 9</a></li>
#         </div>
# 6 <li><a href="xxx3.html">xxx-content-3</a></li>
# 7 <li><a href="xxx4.html">xxx-content-4</a></li>
# 8 <li><a href="xxx5.html">xxx-content-5</a></li>
# 9 <li><a href="xxx6.html">xxx-content-6</a></li>
# 10 <li><a href="xxx7.html">xxx-content-7</a></li>
print("--------------------------------------------------------------------------------------------------------------")
