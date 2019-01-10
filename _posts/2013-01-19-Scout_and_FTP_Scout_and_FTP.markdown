---
layout: post
title: Scout and FTP
tags: [farmdog, paragraphs, indie]
date: 2013-01-19 10:49:11
---

Building a desktop application that manages creating your site is great, but only publishing to a local folder is for the birds. After only a few posts using Scout, I can say that the process of publishing to a folder, switching to Terminal, and running rsync will not fly for any potential customers I may have. It's a pain. 

However, the choices for publishing online like Scout is meant to are not great. The point of Scout is that you can publish to any bare-bones, $3-per-month web host in the world, and not have to worry about the site going down because of high PHP or database processing overhead. There is no database, and there is no active code being executed. The only thing you need for Scout to work is a web server to serve up the site, and an ftp server to get your site to the server. But, that means that I need to write the code for dealing with FTP, and probably SFTP. 

This is going to be hard for a couple of reasons. There could be a thousand different implementations of FTP, and a virtually unlimited number of "edge" cases that I might run into. For example, just testing some FTP code with my current web host caused all of my FTP connections to the host to be denied for a few minutes, too many connections at once. I clearly still have a lot to learn about stream programming, but if there were ever anything I would like to use a library for, this is it. 

Speaking of libraries, I've kind of got a thing about using external code, and I'm a bit conflicted about it. On one hand, I don't want to continuously reinvent the wheel, but on the other hand, I don't want to mindlessly drop someone's half-baked framework into my project. Choosing someone else's code to use must be done very carefully. Right now, I'm considering two things for networking, writing everything myself using CFNetwork, or building in support for libcurl. The libcurl library might be a better choice, since I could also use it for SFTP file transfers, but, it might also complicate my code, and add an external dependency. Tough call, still need to think it through. 

In the mean time, another thing I've noticed Scout needs is a decent full screen mode. The current full screen mode just makes the window bigger, which is not really a lot of help. Full screen should vertically center the current text being edited, make the font bigger, and possibly make the text view a bit narrower than the full width of the screen. 

Also, themes are coming along nicely. Scout will support a fairly simple development of themes for your site, in a little `theme.stemplate` package file. Double-click on the theme and Scout will import it, and it will show up as an available choice in the theme chooser. 

Scout is by far my most ambitious project. Still tons to talk about, and lots of possibilities. Who knows, what about live statistics in the app? Beautiful PDF report generation? A Farmdog hosted option available with in-app subscription and zero configuration? It's all possible, all it takes is time. 

Development continues.

