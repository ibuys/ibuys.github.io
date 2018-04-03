---
layout: post
title: Living In The Technical Past
tags: productivity setup mac
---

<a href="/media/trowel.png"><img src="/media/trowel_thumb.png" /></a>

[Bruce Lawson](http://www.brucelawson.co.uk/2011/i-hate-computers-but-i-love-what-you-can-do-with-them/) has a few interesting things to say about computers.

> You may think it a badge of honour that you can do “sudo dpkg -i –force-all cupswrapperHL2270DW-2.0.4-2a.i386.deb” from memory. I think you’re burying your turds with a trowel in a thunderstorm.

It's a good article, well worth a read. I'm a systems administrator with a degree in Human Computer Interaction, so what Bruce has to say about command line and graphical applications is right up my alley. The field of systems administration has not changed much in the past thirty years since the release of Unix upon the world. While I have not been using a computer for that long, thanks to the Navy I have seen the advancement of technology first hand from vacuum tubes and punched paper tape to the MacBook Air I'm typing this on. I still need to open a terminal emulator and type arcane spells in strange fonts, whispering curses against whoever decided to design the config file *that* way. 

Spending time in the terminal over several years gives me a feeling of familiarity with the environment. I know my spells well, and can generally accomplish what I'm setting out to do with little hassle. However, simply because I am familiar with a setup does not mean that it is the best, just the one I know how to use. I have railed against GUIs as a sysadmin, and with good cause. Most GUI's designed for the back end systems are horrible. Configuring a switch through a gigantic Java application that, one, uses no native controls, and two, is slow, and three, is unstable and may crash is a terrible way to work. Little to no thought is put into usability of these systems, so of course I would rather use a command line. Building a well designed application is *hard*. 

I've been reading the Steve Jobs biography, and what struck me in the first portion of the book was how hard the original Macintosh team worked to make a computer easy to use. Jobs was famously demanding to work for, and would become furious when complexity was exposed to the person using the computer. The sysadmin field needs a Steve Jobs and an Apple, because currently the best we can come up with is increasingly complicated scripts to automate the tasks we need to do on the servers. If a task can be scripted, it can also be designed, animated, and brought to life in the modern age of computing. 

The command line fetish does not end in the data center though. [Sparrow][1] was recently the subject of a kerfuffle, and the state of desktop email clients was discussed on [Build & Analyze][2]. The discussion prompted this quick exchange between myself and Seth Brown:

<div class="bbpBox" id="t226809065844662272"><blockquote><span class="twContent">Sparrow =&gt; Mutt</span><span class="twMeta"><br /><span class="twDecoration">&nbsp;&nbsp;&mdash; </span><span class="twRealName">Seth Brown</span><span class="twDecoration"> (</span><a href="http://twitter.com/DrBunsen"><span class="twScreenName">@DrBunsen</span></a><span class="twDecoration">) </span><a href="https://twitter.com/DrBunsen/status/226809065844662272"><span class="twTimeStamp">Sat Jul 21 2012 5:41 PM CDT</span></a><span class="twDecoration"></span></span></blockquote></div>


<div class="bbpBox" id="t226818888988491776"><blockquote><span class="twContent"><a href="http://twitter.com/DrBunsen">@DrBunsen</a> assuming the Mutt learning curve, I suppose.</span><span class="twMeta"><br /><span class="twDecoration">&nbsp;&nbsp;&mdash; </span><span class="twRealName">Jonathan Buys</span><span class="twDecoration"> (</span><a href="http://twitter.com/ibuys"><span class="twScreenName">@ibuys</span></a><span class="twDecoration">) </span><a href="https://twitter.com/ibuys/status/226818888988491776"><span class="twTimeStamp">Sat Jul 21 2012 6:20 PM CDT</span></a><span class="twDecoration"></span></span></blockquote></div>


<div class="bbpBox" id="t226824341327863809"><blockquote><span class="twContent"><a href="http://twitter.com/ibuys">@ibuys</a> I’ve used Mutt before, so I’m comfortable with it, but now I’m going to try and use it full time; hooks to Address Book will be key.</span><span class="twMeta"><br /><span class="twDecoration">&nbsp;&nbsp;&mdash; </span><span class="twRealName">Seth Brown</span><span class="twDecoration"> (</span><a href="http://twitter.com/DrBunsen"><span class="twScreenName">@DrBunsen</span></a><span class="twDecoration">) </span><a href="https://twitter.com/DrBunsen/status/226824341327863809"><span class="twTimeStamp">Sat Jul 21 2012 6:41 PM CDT</span></a><span class="twDecoration"></span></span></blockquote></div>


Seth is a scientist, and no slouch when it comes to thinking through computer interaction. I value his opinion, so so it will be interesting to see what he comes up with. I too have used Mutt as my email client in the past, and became frustrated with basic things like dealing with attachments. My frustrations are not unique, and the reason graphical clients like Apple's Mail exist; to make the task of reading and sending email easier. 

Mutt is powerful, and when properly configured can ease the burden of dealing with large amounts of email, but at a cost. To me, using Mutt always felt like I was tossing out twenty years of HCI research and design. Unlike data center applications, consumer facing applications have advanced greatly in usability. 

Being a "power user" does not mean you need to disregard graphical applications. It means you learn whatever application you decide on inside and out. 


[1]: http://www.marco.org/2012/07/24/the-sparrow-problem
[2]: http://5by5.tv/buildanalyze/87
