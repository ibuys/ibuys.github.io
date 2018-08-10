---
layout: post
title: Mac Power Tools
date: 2016-01-26 15:00:09
tags: unix, hci, mac
---

My brief experiment with mutt ended mostly how I expected it would. With me turning on my email in Mail.app again and carrying on as normal. I try to understand the draw to using such an archaic tool as mutt, but there’s simply nothing about it that appeals to me. Not at this stage of my life anyway. 

This time someone emailed me a PDF that I needed to sign and send back to her. A simple process with Mail.app, but I knew that I was going to have to jump through hoops and spend an hour reading the documentation to figure out how to respond with an attachment with mutt. Come to think of it, I should amend my previous statement on how well I know the app. I know how to read and organize my email in mutt, and I can use it to build an offline mirror of my hosted email. I can build a search index for it, and send plain text email. I know how to view attachments and how to use a command line web browser to view HTML email. But, the one thing I didn’t know how to do was the one thing I needed to get done. Something trivially simple with the built in mail client. 

So, to the wayside it went. While I was at it, I decided to do some cleaning up of the rest of my command line tools as well. I uninstalled everything I had installed with brew with a simple command:

brew uninstall `brew list`

Then I reinstalled the few command programs that I knew I needed for work. 

brew install jq jsmin rbenv

This mass uninstall also removed MacVim. Something I’ve had [conflicting][1] [feelings][2] about for a while now. As I said in my last post, MacVim excels at editing text, but I realize I set up a bit of a straw man comparing it with TextEdit. Obviously TextEdit was never the competition with MacVim, instead, I should have been comparing it with BBEdit and Ulysses, my other two text editors of choice. 

Like Vim, BBEdit and Ulysses are power tools, but unlike Vim they are *Mac* power tools. They are built specifically for the Mac environment, by [small teams][3] who are dedicated to their craft, and who charge a reasonable, sustainable rate for their product. They approach their jobs in different ways, and are very different applications. BBEdit is built for developers and sysadmins, and has depths of integration and feature set that I’m only just beginning to explore. Ulysses is built for writing prose, and it’s where I’m writing this. Honestly, it’s beautiful. 

We live in a blessed era of Mac productivity. We have almost an embarrassment of riches when it comes to incredibly well crafted third party applications, and we still have access to all the low-level Unix tools that attracted me to the platform thirteen years ago. I’ve waffled back and forth over using the old tools and adopting new ones, but I’m getting too old for that. I simply want my tools to work for me. As of right now, I don’t imagine I’ll be going back to mutt, vim, or anything else command line. Not when there are fantastic Mac apps that do the job either just as well, or better. 

[1]:	https://jonathanbuys.com/01-28-2013/vim_power.html
[2]:	https://jonathanbuys.com/12-23-2015/Winning_NaNoWriMo.html
[3]:	http://www.barebones.com/company/
