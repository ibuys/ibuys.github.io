---
layout: post
title: Small Site Update
date: 2014-07-11 15:11:51
---

I've been publishing this site with Jekyll for several years. I'm not sure exactly when I switched over from Wordpress, but it's long enough ago that I've forgotten when I started.[^footer] Over the past few weeks I've run into a few issues with Jekyll that have caused me to reevaluate if it was still the right choice for me. The short answer is no, the long answer is that this site is now published with my own Python script. 

*List of Grievances*

Jekyll is popular enough with the geek crowd that there are probably reasonable solutions to everything listed below. However, that would assume that I'm reasonable, which I think we've established is not always the case. And besides, something [Dr. Drang said][1] the other day has been stuck in my head:

> the great advantage of making your own software is that you can customize it to match your own idiosyncrasies. 

Thus, 370 lines of Python. On to the motivation to move. 

* Dependencies

Strictly speaking, there are not *that* many Ruby [dependencies for Jekyll][2], and the are all automatically installed when running `gem install jekyll`. To be able to compile the gems, you need to have either the full Xcode IDE installed, or at a minimum the Xcode command line tools. Not much, still more than I thought necessary to parse text and move files.  

* Lost Pages

One of the ways I used Jekyll was to build an internal site where I work. I use the site to keep coworkers updated with what I'm working on, but more importantly I use the site to publish reports. The reports are kept in a separate "/reports" directory under the site root, and Jekyll used to automatically compile the markdown to html in that directory along with the rest of the site. I'm not sure what happened, but at some point that stopped working, and when I rsync'd my site using the "--delete" flag, all my reports were gone. Luckily, I had a backup so I was able to quickly restore the reports, but once I realized what had happened I had to rethink my "modern living document". [^footer2] A process I was in the middle of when I encountered the next grievance. 

* Failure to Build Site

Jekyll failed to build my site last week because of a UTF-8 error; it was all I needed to start looking for something else. Apparently there was a special character in the title of one of my posts. Again, this wasn't anything new, that post must have been built before because I wasn't building anything new at the time. Something changed, I don't know what, and troubleshooting this error led me down a rabbit hole of Ruby bugs I didn't want to go down. 

*Options*

I evaluated, and discarded, several options.

* Wordpress.com
* Self-Hosted Wordpress
* Squarespace
* Ghost
* Hakyll
* Hyde
* Hugo

I briefly looked at a few others, but these were the ones that received the most thought. 


















[^footer]: There was, of course, Paragraphs, but I'm content to let that go. Making peace with your past, learning from your mistakes, and moving on older and wiser is the only way to live in peace. 

[^footer2]: My term for an internal, corporate blog. I maintain it as a way to avoid emailing Word documents and PowerPoint presentations to each other. When someone wants something like that from me, they get a link to an HTML document.


[1]: http://www.leancrew.com/all-this/2014/07/displaying-multiple-images-in-twitter/
[2]: https://gemnasium.com/jekyll/jekyll
