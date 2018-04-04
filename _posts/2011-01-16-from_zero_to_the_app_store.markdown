---
layout: post
title: From Zero to the App Store
date: 2011-01-16 10:16:25
tags: farmdog indie cocoa
redirect_from: /01-16-2011/from_zero_to_the_app_store.html
---

This past Thursday I was privileged to speak at our local
[CocoaHeads][1] about my
history, and how I was able to bring my app to market. Since someone on
Twitter asked for [my slides][2], which don't amount to much, I thought writing up
my experiences would be a little more useful.

I didn't grow up with computers. My first experiences programming were not
when I was six on my Dad's Apple II. We were poor, we lived on an Indian
reservation in Montana, and for a good part of my life we lived in a mobile
home. My first experience with a computer was in high school, after a semester
of learning to type on an IBM Selectric, we moved on to one semester of
computers, which was basically typing out documents in WordPerfect. That was
it… for years. I didn't start learning computers in depth until I had been in
the Navy for a few years, and needed to learn them to make rank as a Radioman.
It was then that I found I had a knack for technology, and started pursuing
it. My first computer was a PC, a mistake I made exactly once. I had the
machine for a few months before Linux was loaded on it for the first time. In
2000 I was introduced to Unix, and started working with OpenBSD, Linux, HP-UX,
and Solaris. I enjoy Unix, I find that the system has a spartan elegance to
it, especially the BSD flavors. Around this same time I heard that Apple was
basing their new operating system, OS X, off of Unix, and I was anxious to try
it out. In 2003, we moved back to the states, and I bought my first Mac, an
iBook G4.

The iBook served me well, and I fell in love with the Mac and with the Mac
community. I became a regular reader of Daring Fireball, and was inspired by a
post named "[The Life][3]". However,
I had one college semester of programming experience in C, an experience that
left a bad taste in my mouth, so I figured that "The Life" was out of my
reach, put it behind me and moved on. Eventually I got out of the Navy and
found work as a Unix sysadmin, using the skills that I learned while on active
duty. The reality of work in a cubicle is much different than I imagined it
would be. In the Navy there is always something different right around the
corner. You will spend a max of 3-4 years at a single command, and during
those years you will most likely have several different jobs. Things are much
different as a civilian, and while I have a good job, the prospects of keeping
this same job for the next ten or more years scares me more than a little. So,
the question that came to mind was "is this what I want to do for the next 30
years?", and Gruber's article on The Life came back to mind.

So, I decided to learn Objective-C.

This decision was not taken lightly. I considered the possibility that it was
beyond me, that I was not smart enough, or that I did not have the necessary
math and programming and educational background to become a developer. Could I
be dedicated enough to learn something so far out of my area? Was I smart
enough to learn this? That last question gnawed at me, and I finally decided
that there was no way I was going to know unless I tried, and gave it
everything I had. So, I did some googling and found that for first timers
wanting to learn Cocoa, most experienced developers pointed to what I now
simply refer to as "The Book", [Cocoa Programming for Mac OS
X][4].

For the next several months, I would wake up at 5AM and go through The Book,
page by page, chapter by chapter, every challenge, no cheating. If I got stuck
on something, I'd search the [Apple developer
documentation][5] (which is
excellent), or search through the
[CocoDev][6] mailing list
archives. I was investing in my future, so it was important to understand
everything in The Book. Eventually, I finished The Book, and started working
on my own little Mac app, a GUI version of a little shell script that I wrote
called "go".

The first few versions of Go were tough. I had a hard time getting my head
wrapped around the "Modal, View, Controller" framework that Cocoa and the Mac
developer tools are built around. I could not for the life of me figure out
how to get an image to display in an NSTableView. That was by far the single
most difficult hurdle I had to overcome. Changing my mindset from "Ok, place
button here, and place image here", which didn't work, to "OK, place button
here, and display data from my data source in this table". I struggled for
weeks, months even with this simple concept. Trying to work against the MVC is
a sure way misery and failure. It was around this time that I found the local
CocoaHeads group. I went to a meeting, and the speaker (a great guy), was
talking about drawing pixels and getting your views to look _just_ right. It
was interesting, to be sure, but over my head at the time. I left that meeting
disheartened, feeling that maybe it was simply too much for me, and I was just
not smart enough.

I gave up, and for several months did not touch Xcode or Cocoa.

I'm not sure what brought me back, but I have a feeling it was stubbornness.
The idea that there was a learned skill that I could not learn was too much
for me. I started getting the feeling that I was _almost there_, that my
understanding of Cocoa was incomplete, but I was just one more article read,
one more blog post scanned, from finding the missing piece. So, I started
reading again, I started building again, and piece by piece I started to
understand Cocoa. I found that the best way for me to display an image was to
use a value transformer. Store the data as a string, transform that string to
an image, and the NSTableView would happily display that image for me. I
started asking questions on Twitter and the mailing lists, and was recognized
by [Jim Turner][7], who ran CocoaHeads in Des
Moines.

Jim is not the type of guy to give you an answer, but he is the type of guy to
point you in the right direction. Jim and I exchanged emails a few times, and
he pointed out where I was going about things wrong, or making things harder
than they needed to be. Eventually, I built real, working versions of Go,
which Jim was kind enough to beta test. Some of his critiques of Go were
scathing, but absolutely necessary. Each email Jim would send me with a list
of things that were wrong with Go, I'd drop into a to-do list and check off
each item as it was fixed.

Some features that I worked on for months I killed. Some features that I spent
months working on and hundreds of lines of code I found could be replaced with
only a few lines of more functional code. The original version of Go used
AppleScript and the Cocoa ScriptingBridge framework to launch the Terminal. I
would build a shell script in Cocoa, then send that to the Terminal as a "Do
Shell Script" AppleScript. This entire structure was replaced when I learned
about the functionality of NSWorkspace and NSURL. Now, all bookmarks are URLs,
and opened by NSWorkspace. Much simpler, and more functional. This discovery
allowed me to take Go in a new direction, instead of being a launcher for SSH
connections, Go could be a universal bookmarker, storing and launching
bookmarks for anything that could be addressed by URL, which turns out to be
just about everything. I finalized the functionality of Go, and spent another
month or so building in a copy protection scheme and a 30 day trial, and…
launched.

Farmdog Software was launched to the amazement of no one. I had the store open
for three months and sold a grand total of seven copies of Go. I was
languishing in obscurity. No one knew what Go was, who I was, or had heard of
Farmdog Software. Then Apple announced the Mac App Store, and I knew that was
my opportunity.

I started an entire redesign of Go, and renamed the application Go2. I
redoubled my efforts. Now I was not only programming in the morning before
work, but also at lunch, and at night after the kids were in bed. I built a
custom NSCell class, and spent a long time building the Status Bar search menu
that Go2 has now. Jim came to the rescue once again with a way to use the down
arrow to navigate out of the search field, which was the final piece of the
Go2 puzzle.

I submitted Go2 to the App Store, and in the last week of December it was
rejected. Turns out there was an odd bug that only showed itself at launch
time, and only on the first time the app was launched. I fixed that bug,
resubmitted, and Go2 was in the store on day 1.

Go2 and Farmdog still have a long, long ways to go, but they are on their way,
and that's the important thing. If anyone can take anything away from all this
I hope that it is to never give up. Never. Nothing worth doing is ever easy.


[1]: http://cocoaheads.org/us/DesMoinesIowa/index.html
[2]: http://public.iwork.com/document/?d=CocoaHeads_Presentation.key&a=p62622474
[3]: http://daringfireball.net/2005/10/the_life
[4]: http://www.amazon.com/Cocoa-Programming-Mac-OS-3rd/dp/0321503619
[5]: http://developer.apple.com/library/mac/navigation/
[6]: http://lists.apple.com/mailman/listinfo/cocoa-dev
[7]: http://www.nukethemfromorbit.com/
