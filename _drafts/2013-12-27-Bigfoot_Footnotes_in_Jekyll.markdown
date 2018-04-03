---
layout: post
title: Bigfoot Footnotes in Jekyll
date: 2013-12-27 07:33:33
tags: tech jekyll blogging
---

Like the [good doctor][1], I knew as soon as I saw [Bigfoot][2] that I would be adding it to this site. [^1] I've avoided footnotes up till now because the HTML formatting for them seemed far too *fiddley*, and the Jekyll Markdown processor I was using did not support them. 

It turns out that adding support for footnotes in Markdown was as simple as replacing redcarpet with kramdown in the Jekyll configuration. Now, instead of mucking about with HTML that looks like this:

~~~ html
    <sup id="fnref:1">
        <a href="#fn:1" rel="footnote">1</a>
    </sup>

<div class="footnotes"><ol>
    <li class="footnote" id="fn:1">
        <p>footnote.<a href="#fnref:1" title="return to article"> ↩</a><p>
    </li>
</ol></div>

~~~

I can have nicely formatted Markdown footnotes in my text, like this:

~~~ html
Footnote inline [^1]

[^1]: The footnote text

~~~

It may not amount to much, bit I think it's a nice addition to the site. 




[^1]: I've always liked footnotes. 


[1]: http://www.leancrew.com/all-this/2013/12/tweaking-bigfoot-footnotes/
[2]: http://cmsauve.com/labs/bigfoot/
