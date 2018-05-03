---
layout: post
title: Text Editing in MacVim
tags: vim blogging setup
date: 2011-08-04 10:49:11
---

The venerable BBEdit recently received a [big upgrade](http://www.barebones.com/products/bbedit/index.html), and looks poised to attract users of TextMate, which, by all accounts, has been abandoned by its developer. I tried to love BBEdit, but it always felt like trying on someone else&#8217;s clothes. They might look good, but that does not mean the clothes will be comfortable for you. Recent conversations about text editors on [Build and Analyze](http://5by5.tv/buildanalyze) led me to rethink my position, and examine in more detail how I came to choose MacVim.

Several years ago, I was sitting with a contractor as he installed a new firewall on our network. He was explaining to me how Unix systems relied on text files, and how all Unix systems came with a text editor named *vi*. I asked, in my ignorance, why anyone should bother using such ancient technology, when a modern graphical text editor was available. Pragmatically, he replied that someday I would be connected to a server through SSH or telnet and the only way to edit a file would be with vi. I took his advice to heart, and I am glad I did.

Over the years as I have dug deeper and deeper into Unix (and later Linux) systems, I accumulated a few of my favorite vi tricks which I kept in an exrc file. I had complicated macros that would do things like building the skeleton of a shell script, or insert a comment with my name and email address, or the current date. OK, maybe it was not that complicated, but every time I hit the mapped key combo, I smiled. I learned to navigate to an exact line in a file, to yank and paste text, and generally how to get along with the only text editor I could be sure was on each and every server I was responsible for. I did not realize it at the time, but I was building up valuable expertise, and, it seems, more importantly, a type of muscle memory. 

In the past, I always kept my work on the servers separate from my &#8220;work&#8221; I did on my Mac. My Mac was a hobby, but work was important. When TextMate appeared, I downloaded a copy to use for building web sites. I enjoyed TextMate, but there was never love. Love takes time, frustration, and understanding. Love was what I was building at work with vi. I simply did not understand it at the time.

In fact, for many years I kept the attitude that vi was not a modern text editor. It was simply a tool for work and that on a Mac I should be able to use a graphical text editor that did lots of fancy tricks. It was not until this summer, after years of building my vi knowledge on the server that I decided to use vi for a Python programming course on my Mac. I downloaded a copy of [MacVim](https://code.google.com/p/macvim/), spent a few days configuring it the way I liked it, and, for what feels like the first time, felt completely comfortable in my text editor.

I had already overcome the biggest obstacle to vi: the learning curve. Slowly, over years of use, I had become fluent in one of the most powerful text editors available. 

I will not go into the details of how to configure MacVim, there are several articles for that already. If you are interested, I keep my MacVim configuration in [GitHub](https://github.com/ibuys/My-MacVim-Config). What I will say is that taking the time to learn the basics of vi, and taking a few days, maybe a week, to find the magic combination of plugins and configurations that work for you, is worth the effort. MacVim is like a gateway drug. Once you get used to using it, you might find yourself attempting to navigate a new email in Mail with vi key bindings.

I am still learning new things with MacVim. There are precious few tricks that another editor can do that MacVim cannot. However, choosing MacVim is akin to choosing a partner to share your life. The more you put into the relationship, the more you get out of it. In any relationship, over time you become aware of the others shortcomings, but if the relationship is healthy, those shortcomings are very easy to overlook. If you spend serious time in text, it behooves you to spend serious time learning your tools.   

MacVim is actively developed, has a dedicated community, is easily extendible, and can fly through the biggest text files with ease. However, it does take time to understand, and I will not try to tell you that the commands you use to control MacVim are intuitive or &#8220;easy&#8221;. Nothing worth doing is ever easy. 



