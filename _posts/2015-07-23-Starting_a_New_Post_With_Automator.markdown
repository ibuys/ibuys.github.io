---
layout: post
title: Starting a New Post With Automator
date: 2015-07-23 05:37:19
tags: mac,automation
---

Automator is one of my favorite tools on the Mac, and unfortunately one of the most unappreciated. I have several workflows and services that I've built up over the years, things that I could have turned to a third-party tool like Keyboard Maestro, Alfred, or even my beloved Quicksilver for, but I like the simplicity of using a built-in application. 

My "New Post" workflow is a simple example of using Automator to mix GUI elements with a shell script. There are only two actions. The first uses the "Ask for Text" action to prompt for a post title, and the second uses the "Run Shell Script" action to run this bit of bash: 

	NAME=`echo $* | sed s/\ /_/g`
	POSTNAME=`date "+%Y-%m-%d"-$NAME`
	POST_FQN=~/Public/Site/_posts/$POSTNAME.markdown
	POST_DATE=`date "+%Y-%m-%d %H:%M:%S"`
	touch $POST_FQN

	echo "---" >>$POST_FQN
	echo "title: $*" >> $POST_FQN
	echo "date: $POST_DATE" >> $POST_FQN
	echo "tags: " >> $POST_FQN
	echo "---" >> $POST_FQN


	/usr/bin/open $POST_FQN


The first line removes spaces from the title passed to it from the Ask for Text action and replaces them with underscores so I can use the title as the URL slug. The second line adds the creation date[^1] to the file name, and the third creates a full path to the file. The fourth line simply creates an empty file with the correct naming scheme for my site generator tool. 

The collection of `echo` statements on the next few lines add YAML frontmatter to the post, a bit of residual formatting from the sites Jekyll roots. Finally, I use the Mac's `open` command to start my favorite text editor, normally MacVim, and start writing. 

Using Automator can be frustrating at times, especially when there is no action for something you think there should be an action for, but for manipulating text and mixing in scripting, it's not bad.  



[^1]: With apologies to Matt Gemmell. I've not yet committed to removing the ugly cruft from my URLs. 


