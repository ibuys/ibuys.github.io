---
layout: post
title: On TermKit - Steven Wittens 
tags: mac productivity
date: 2011-05-19 10:49:11
---

>I've been administering Unix machines for many years now, and frankly, it kinda sucks. It makes me wonder, when sitting in front of a crisp, 2.3 million pixel display (i.e. a laptop) why I'm telling those pixels to draw me a computer terminal from the 80s.

via: [On TermKit | Steven Wittens - Acko.net][1]


I too have been administering Unix and Unix-like machines for many years. I admire Steven's ambition, and his obvious programming and design expertise, but I believe his architecture with TermKit is a bit misguided. TermKit is a combination of Cocoa, Node.js, and WebKit, and while it works, there are a lot of moving parts to get it to work. 

Steven seems to have missed the point of the command line, and why we are still use it after all these years. I like using a carpenter's analogy. Sometimes, you just need a hammer. Sure, there are framing nailers and powder-actuated guns, but sometimes, the only way to get the job done is to hit something with something else hard and heavy. That's the command line, that's Unix.  

Neal Stephenson uses a better tool analogy. Popping open the Terminal is akin to bringing out the [Hole Hawg][2], it's ugly, it's powerful, and it gets the job done.

The most basic point for why Terminal.app still exists, and why the command line is still a preferred tool for systems administration is that Unix is a text-based operating system. All of the configuration files are text, much of the system information is available as text, and all input and output from the commands are text. So, when you are operating on the lowest level of the system, reaching for optimum efficiency, the command line gives you direct access. Anything built on top of that is an unnecessary layer of abstraction.  

Being able to "cat" a PDF file is a neat trick, but I have a hard time imagining how it could help revolutionize systems administration.


[1]: http://acko.net/blog/on-termkit?page=3
[2]: http://www.team.net/mjb/hawg.html
