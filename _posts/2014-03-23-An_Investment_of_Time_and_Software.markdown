---
layout: post
title: Site Design Non-Update
date: 2014-03-23 21:41:23
footnote: sdnu
---

The site design of *jb* was very nearly upgraded tonight. Well, upgraded is not quite the word for it. Changed is more accurate. Even though I'm quite happy with the look and feel of the site, from time to time I get frustrated with one aspect of it or another. I've spent more time that I want to admit thinking about readability, fonts, font sizes, spacing, kerning, and the like, but occasionally I'll look at another site and think "that looks *good*". And then mine looks like crap for a day or so. 

The most recent bout of site envy came while reading a [recent post][1] by the brilliant Dr. Bunsen[^sdnu1]. His entire site is worth reading, some posts several times. I decided to do a bit of HTML spelunking and see what the source revealed, and saw several references to the [Pure CSS][2] framework. I hadn't heard of this one before, so I downloaded it and set up a new Jekyll powered site with the base blog layout. It looked fine, it works as advertised, but it would obviously take a lot of work to tweak it to look just the way I wanted it to. 

After running through this exercise I went back and thought about what I don't like about my site right now, and realized that it is not the overall look of the site that I'm not happy with, it is a few details that are nagging at me. For one, code syntax highlighting is not working, and for two, the Bigfoot footnotes were not lining up properly on the home page. I solved the latter problem by only showing only one post on the home page at a time, but the former is still bothering me.

The funny part of it is that one of the reasons syntax highlighting is not working is that I'm not using the default Jekyll Markdown converter. In order to get footnotes to work the way I want them to, I'm using [Kramdown][3], which doesn't use Pygments, but can be configured to use Coderay. I have the settings for Coderay, but so far they don't seem to be doing anything. None of my inserted code is rendered with anything but "code" and "pre" tags. Ah well, this site remains, as always, a work in progress. 

It's always a good exercise to try out a completely different way of doing things. Even when I decide to scrap the work and keep things the way they are, I still count it as progress made. 




[^sdnu1]: Whom, if you are not following, you certainly should.


[1]: http://www.drbunsen.org/ski-it-if-you-can-meta/
[2]: http://purecss.io
[3]: http://kramdown.gettalong.org
