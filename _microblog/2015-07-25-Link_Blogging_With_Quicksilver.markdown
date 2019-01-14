---
title: Link Blogging With Quicksilver
layout: post
date: 2015-07-25 21:38:37
tags: automator, mac 
---

I can't quite make up my mind on how I feel about "link blogging". On the one hand, there's already a lot of people out there who do it better than I can. On the other hand, sometimes I want to share something and make a few pithy comments about it. It's out of that second feeling that this script is born. 

The script started out as an Automator action, but having an Automator wrapper around a single shell script seemed like overkill.


	#!/bin/bash
		
	TITLE=`osascript -e 'tell application "Safari" 
		set pageTitle to (do JavaScript "document.title" in document 1)
	end tell'`

	URL=`osascript -e 'tell application "Safari" 
		set pageURI to (get URL of document 1)	
	end tell'`

	TEXT=`osascript -e 'tell application "Safari"
	set selectedText to (do JavaScript "(window.getSelection().toString())" in document 1)
	end tell'`

	QUOTEDTEXT=`echo -n ">"; echo -n $TEXT`

	LINK=`echo -n [Jump to Post]; echo -n \($URL\)`

	NAME=`echo $TITLE | sed s/\ /-/g`
	USERNAME=`whoami`
	POSTNAME=`date "+%Y-%m-%d"-$NAME`	
	echo $POSTNAME
	POST_FQN=~/Public/Site/_posts/$POSTNAME.markdown

	POST_DATE=`date "+%Y-%m-%d %H:%M:%S"`
	
	echo "---" >>$POST_FQN
	echo "layout: post" >> $POST_FQN
	echo "title: $TITLE" >> $POST_FQN
	echo "date: $POST_DATE" >> $POST_FQN
	echo "---" >> $POST_FQN

	echo "$LINK" >> $POST_FQN
	echo "" >> $POST_FQN
	echo "$QUOTEDTEXT" >> $POST_FQN
	echo "" >> $POST_FQN

	echo $POST_FQN

	/usr/bin/open $POST_FQN

That first line is pretty ugly. I don't recall when I wrote this, but it's been working reliably for long enough that I don't feel the need to change it just yet. Then again, a shell script that calls AppleScript that calls JavaScript seems pretty ridiculous.

This script looks at the current web page in Safari and grabs the title, URL, and any selected text and builds a new post in the format my site builder script expects. Similar to my previous New Post script, this one opens the new file in MacVim, ready for writing. 

I call the script from Quicksilver using the `Run…` command, and tied the command to `^⎇ ⌘ P` for a hotkey. 

I might start putting more links on the site. There are often things that I find might be interesting to a certain segment of the Mac community, mainly the more technical and scientific groups, that I haven't done anything significant with. I'd like to change that.

