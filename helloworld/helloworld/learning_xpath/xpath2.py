from scrapy.selector import Selector

body = """
<html>
   <head>
      <title>Scrapy Tutorial By Cookie</title>
   </head>
   <body>
      <div class='links'>
         <a href='one.html'>Link 1<img src='image1.jpg'/></a>
         <a href='two.html'>Link 2<img src='image2.jpg'/></a>
         <a href='three.html'>Link 3<img src='image3.jpg'/></a>
      </div>
      <div class="body">
        <figure name="content-name" id="content-id" class="content content--figure">
            <div class="div1">
                <div class="div1-1"></div>
                <div class="div1-2">
                    <img src="https://cdn-images-1.medium.com/freeze/max/30/1*qmHZVxZmPP9w5iMqN7GWMw.jpeg?q=20">
                    <canvas class="canvas"></canvas>
                    <img src="https://cdn-images-1.medium.com/max/800/1*qmHZVxZmPP9w5iMqN7GWMw.jpeg">
                    <noscript src="https://cdn-images-1.medium.com/max/800/1*qmHZVxZmPP9w5iMqN7GWMw.jpeg"></noscript>
                </div>
            </div>
        </figure>
        <h1 name="content-title-name" id="content-title-id" class="content content-h1">sync.RWMutex</h1>
        <h2 name="content-subtitle-id" id="content-subtitle-id" class="content content-h2">Solving readers-writers problems</h2>
        <div class="div2">
            <div class="div-author">
    
            </div>
        </div>
        <p name="content-p-name" id="content-p-id" class="content content-p-graf">Readers-writers problems (plural since there’re some
            variations) occur when shared piece of data needs to be accessed by multiple threads. There’re two types of
            threads accessing data&#8202;—&#8202;readers and writers. Readers only read data and writers modify it. When
            writer has access to data then none other thread (reader or writer) can share such access. This constraint takes
            place in real life when e.g writer cannot modify data (like database) in atomic way so reading incomplete
            changes must be blocked to prevent loading corrupted data. There’re many modifications of the core problem
            like:</p>
        <pre name="content-pre1-name" id="content-pre1-id" class="content content-pre">W</pre>
        <pre name="content-pre2-name" id="content-pre2-id" class="content content-pre">R<br>RR<br>RRR<br>RRRR<br>RRRRR<br>RRRR<br>RRR<br>RRRR<br>RRR<br>RR<br>R</pre>
        <ul class="content content-ul">
            <li name="88b2" id="88b2" class="content content-li">writers cannot be starved (waiting indefinitely for their turn)</li>
            <li name="bc29" id="bc29" class="content content-li">readers cannot be starved</li>
            <li name="15de" id="15de" class="content content-li">no thread shall be allowed to starve</li>
        </ul>
        <h3 name="dbbd" id="dbbd" class="graf graf--h3 graf-after--p">Usage</h3>
        <blockquote name="blockquote" id="blockquote" class="content content-blockquote">Environment of programs launched on
            play.golang.org is deterministic (e.g. when time begins) so <code class="markup--code markup--blockquote-code">rand.Seed(time.Now().Unix())</code>
            will provide the same seed value and the program’s output will be most likely the same. Either put different
            seed each time or run program on your machine.
        </blockquote>
        <figure name="b01c" id="b01c" class="graf graf--figure graf-after--h3">
            <div class="aspectRatioPlaceholder is-locked" style="max-width: 700px; max-height: 328px;">
                <div class="aspectRatioPlaceholder-fill" style="padding-bottom: 46.9%;"></div>
                <div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded"
                     data-image-id="1*Gg_vmyWlU35r3w_L4r4SYw.jpeg" data-width="1280" data-height="600" data-action="zoom"
                     data-action-value="1*Gg_vmyWlU35r3w_L4r4SYw.jpeg" data-scroll="native"><img
                        src="https://cdn-images-1.medium.com/freeze/max/30/1*Gg_vmyWlU35r3w_L4r4SYw.jpeg?q=20"
                        crossorigin="anonymous" class="progressiveMedia-thumbnail js-progressiveMedia-thumbnail">
                    <canvas class="progressiveMedia-canvas js-progressiveMedia-canvas" width="75" height="35"></canvas>
                    <img class="progressiveMedia-image js-progressiveMedia-image"
                         data-src="https://cdn-images-1.medium.com/max/800/1*Gg_vmyWlU35r3w_L4r4SYw.jpeg">
                    <noscript class="js-progressiveMedia-inner"><img
                            class="progressiveMedia-noscript js-progressiveMedia-inner"
                            src="https://cdn-images-1.medium.com/max/800/1*Gg_vmyWlU35r3w_L4r4SYw.jpeg"></noscript>
                </div>
            </div>
        </figure>
    </div>
   </body>
</html>
"""

selector = Selector(text=body)

tag_value = selector.xpath("//title/text()").extract()  # 从整个页面中搜索
print(tag_value) # Get <title>Scrapy Tutorial By Cookie</title>

