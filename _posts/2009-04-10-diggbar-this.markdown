--- 
layout: post
title: DiggBar This
tags: online programming php
---

I've put a lot of work into this site.  I've put thought into how I want the URLs to look, how the layout should feel, and since the site has my name on it, I wanted it to be good.  I created a custom theme for the site which will purposefully only work here, and I've even done a bit of personal "branding" I suppose with the jb{ logo. 
 
So, when I saw that Digg had decided to take a page out of 1999's web play book and start framing sites inside of their DiggBar, I was more than a little annoyed.  There may be only six people who read this site on a regular basis (Thanks guys!), but this site is entirely mine.  The DiggBar removes the URL from the site you are reading and adds it's own custom shortened URL, making it hard to bookmark, or really even remember where you are.  

John Gruber, from Daring Fireball fame and who's work I admire, evidently shares the same feelings I have about the DiggBar, and posted some [php code to block it][1].  I have taken his example code, and created a tiny Wordpress plugin that places his code in the correct spot in the site.  The goal is to make it super easy for the thousands of wordpress installs to remove this particular menace.  

Please let me know in the comments if you have any problems.

UPDATE 04/14/2011 - Since I no longer use PHP for this blog, I've dropped support for the DiggBar block. However, there are several great alternatives out there. Also, is the DiggBar even a *thing* anymore? I'm not sure.

[1]: http://daringfireball.net/2009/04/how_to_block_the_diggbar
