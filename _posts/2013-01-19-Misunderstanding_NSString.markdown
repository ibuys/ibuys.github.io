---
layout: post
title: Misunderstanding NSString
tags: [farmdog, cocoa]
date: 2013-01-19 10:49:12
---

So, while I was debugging the first post using Scout, I found an oddity in NSString. I was building the links between the posts using `stringByAppendingPathComponent`, to join the site's base URL with the path component of the individual post.  Unfortunately, that method seems to be stripping one of the forward slashes off of the `http://` string, which screws up building links. 

To test it, I created a blank Xcode project, and added this method to the App Delegate:

	-(void)awakeFromNib
	{
    NSString *first = @"http://first";
    NSString *second = @"second/part.html";
    NSLog(@"first + second = %@", [first stringByAppendingPathComponent:second]);
	}

And, sure enough, here is the output from that method:

	2013-01-03 19:26:02.388 NSStringTester[39861:303] first + second = http:/first/second/part.html

A quick search through Scout's source files shows that I'm using `stringByAppendingPathComponent` 53 times. Looks like I've got some work to do. 

Also, this is a good time to point out that when you are doing web development, it is very important to test with multiple browsers. Safari hid the problem, Firefox did not.

Finally, it turns out that this is not actually a bug in NSString, but a bug in my understanding of this method.  My thanks to [Matt Yohe](https://twitter.com/mattyohe/status/287009148665733120) who was kind enough to point out my mistake on Twitter. 

<div class="bbpBox" id="t287009148665733120">
<blockquote>
<span class="twContent"><a href="http://twitter.com/ibuys">@ibuys</a> <a href="http://twitter.com/eridius">@eridius</a> also: “Note that this method only works with file paths (not, for example, string representations of URLs).”</span><span class="twMeta"><br /><span class="twDecoration">&nbsp;&nbsp;&mdash; </span><span class="twRealName">Matt Yohe</span><span class="twDecoration"> (</span><a href="http://twitter.com/mattyohe"><span class="twScreenName">@mattyohe</span></a><span class="twDecoration">) </span><a href="https://twitter.com/mattyohe/status/287009148665733120"><span class="twTimeStamp">Thu Jan 3 2013 7:34 PM CST</span></a><span class="twDecoration"></span></span>
</blockquote>
</div>

I'm still considering filing this as a bug, but I can see where they are coming from. Double slashes would not work for a file URL, but if they are already parsing the string for something like that, why not just check for "http" as well?

