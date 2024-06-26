---
layout: post
title: Footnotes and Other Scripts
tags: [farmdog, paragraphs, indie]
date: 2013-01-16 10:49:11
---

I'd like a really simple way to insert footnotes in the text. However, I'm not sure how much of that I can do with the Markdown parser that I have now, which means inserting ugly HTML, which I'd really rather not have. I could do something in the generation of the site, inserting my own marker in the text and parsing through that later, but that seems like reinventing the wheel. Surely there are better ways to go about this. 

I've also been thinking about other scripts or "plugins" for Scout. An early idea I had was to build in analytics, so you could download hit counts and other statistics from your host and Scout would build a nice report for you. Or, maybe even do some type of live updating, but I think that might be taking it a bit too far. 

[MathJax][1] would be a nice addition, but I don't think it would be appropriate for everyone. Maybe a preference pane with optional plugins you could check and uncheck and have them included in your site. That way, if you want MathJax or Google Analytics or jQuery you'd just select them and hit publish. Still so far to go to get there.

Which leads me to the next thought, when is it enough for 1.0? I need to balance two weights; on one hand, I need to actually ship the app, but on the other hand, I want Scout to be [great from day one][2]. What is it going to take for it to be great? What is the bare minimum that I *need* in 1.0 before I can ship it? These are the questions I'm asking myself.

One feature that I keep coming back to is the ability to have zero configuration publishing. For example, what if you don't have a web site or a domain name, but you'd just like to write and publish online in the easiest way possible? Scout should be able to grab your iCloud user name, have you click an in-app subscription, and let you publish to a Farmdog hosted server. That way, you can just download Scout and start writing, and Scout and Farmdog take care of all the little details. That's the dream anyway, but is that a 1.0 feature? Tough call. 

Syncing is another thing that's going to be a tough call. I'm using plain text as the data storage, so I should be able to monitor changes in the filesystem and merge them into the application. Hopefully, building on plain text and integrating with Dropbox will allow me to (eventually) build an iOS companion to Scout. Scout on the iPad with Dropbox on the backend could be fantastic for writers. 

If I only had 30 hours per day to work on this.


[1]: http://www.mathjax.org
[2]: http://www.marco.org/2010/07/04/great-since-day-one