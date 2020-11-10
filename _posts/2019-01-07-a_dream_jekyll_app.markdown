---
layout: post
title: A Dream Jekyll App
date: 2019-01-07 14:09:31
tags: [apps, mac, jekyll, blogging]
---

I've never been 100% happy with this site. On the one hand, Jekyll lets me have full control of my content, and I never have to worry about losing any of it or having anything locked inside a database on a server somewhere. On the other hand, things like adding media is more complicated than I'd like. I've written scripts to help, of course, but I'd really rather have the best of both worlds. 

I've considered creating an application to manage this for me. Like [MarsEdit][1] for Jekyll and GitHub Pages. A text editor with a git client and an understanding of Jekyll site structure. It could even let the user sign up for GitHub and setup the repository. I thought I might setup my old Paragraphs app to do this for me… I could tear out the site rendering code and replace it with a wrapper around a libgit2. But, the text editor in Paragraphs needs a lot of work, and there would be multiple parts of the app that would need considerable rework to get it to an even *barely functional* state. The other option would be to create a new app from scratch, but at this point if you aren't creating an iOS app in Swift when starting anew what are you even doing with your life? Problem is I don't know either Swift or iOS development. My skills in this area are basically outdated. 

A search for "Jekyll" in the Mac App Store finds one result, for a "markup viewer" app with dubious usefulness. A quick Duck search finds a couple people with the same idea, one that setup a web GUI, which is not at all what I'm talking about, and one that started something five years ago and never finished it. From what I can tell, the app that I want doesn't exist. Too bad [Ulysses][2] and [IA Writer][3] added support for Medium into their apps instead of GitHub pages. 

So should I build this app or not? It's basically a text editor that you can drop media on, hit publish, and have it push the site to GitHub. The same thing I have now, but automated, simple, and beautiful. Is there a market for this style of app? Would GitHub allow it? Could I learn the skills required to create it in a reasonable time? iOS development is supposed to be easier than macOS… but I'm not sure that applies when you're carrying so much baggage around from the old style of development. 

In the end, I'm not sure it'd be worth the effort for me. I've already got a beautiful text editor, and my scripts and workflows make it simple for me to create and publish new posts. I think I've talked myself out of building this app myself, but darned if I wouldn't love for someone else to build it.


[1]: https://www.red-sweater.com/marsedit/
[2]: https://ulysses.app
[3]: https://ia.net/writer