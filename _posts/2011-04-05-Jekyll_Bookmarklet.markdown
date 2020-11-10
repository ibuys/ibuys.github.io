---
layout: post
title: Jekyll Bookmarklet
tags: [blogging, programming, javascript]
---

I have a handful of Automator scripts I've created to make maintaining this site with [Jekyll](https://github.com/mojombo/jekyll/wiki/) just a little easier. The first script let's me highlight some text on a web page and click a bookmarklet (or, more likely, hit the command+3 key combo), and the script creates a newly formatted Jekyll post with the highlighted text in markdown quoted syntax, and opens it in my default Markdown editor. 

Here is how its done.

First, open Automator and create a new application with a single action: "Run Shell Script". Next, copy and paste this script into the text field:

{% highlight bash %}
TITLE=`osascript -e 'tell application "Safari" 
set pageTitle to (do JavaScript "document.title" in document 1)
end tell'`

URL=`osascript -e 'tell application "Safari" 
set pageURI to (get URL of document 1)	
end tell'`

TEXT=`osascript -e 'tell application "Safari"
set selectedText to (do JavaScript "(getSelection())" in document 1)
end tell'`

QUOTEDTEXT=`echo -n ">"; echo -n $TEXT`

LINK=`echo -n [$TITLE]; echo -n \($URL\)`

NAME=`echo $TITLE | sed s/\ /-/g`
USERNAME=`whoami`
POSTNAME=`date "+%Y-%m-%d"-$NAME`
POST_FQN=/Users/$USERNAME/Dropbox/WebLog/_posts/$POSTNAME.markdown
touch $POST_FQN
echo "---" >> $POST_FQN
echo "layout: post" >> $POST_FQN
echo "title: $TITLE" >> $POST_FQN
echo "---" >> $POST_FQN
echo "" >> $POST_FQN
echo "$QUOTEDTEXT" >> $POST_FQN
echo "" >> $POST_FQN
echo "via: $LINK" >> $POST_FQN
/usr/bin/open $POST_FQN	
{% endhighlight %}
	
Note the line beginning `POST_FQN`. I have this site locally stored in a dropbox folder named "WebLog", so you will have to change this line to point at your `_posts` folder. The rest should work fine. Save the script as an application somewhere that makes sense and quit Automator. 

Next, drag this bookmarklet to your bookmarks bar: [Blog This](javascript:location.href='blogPost:url='+location.href+'title='+decodeURIComponent(document.title\)).

The last part is a bit of a hack, but it works well. You will need to let the operating system know that your new Automator app responds to the `blogPost://` url scheme. So, find your Automator application saved from the first step, control-click on it and select `Show Package Contents`. In the new Finder window that opens, open the `Contents` folder and find the file named `Info.plist`. Right click on that file and open it using your favorite plain text editor, something like MacVim or TextEdit. 

Find these two lines:

{% highlight HTML %}
<key>CFBundleIdentifier</key>
<string>com.apple.automator.Post From Safari</string>
{% endhighlight %}

And add this directly underneath:

{% highlight HTML %}
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>Post to Blog</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>blogPost</string>
        </array>
    </dict>
</array>
{% endhighlight %}

Save the Info.plist file and close the Finder window. You should be all set. Highlight something on this page and click the bookmarklet. 

