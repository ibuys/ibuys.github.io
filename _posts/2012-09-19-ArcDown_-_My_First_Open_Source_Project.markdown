---
layout: post
title: ArcDown - My First Open Source Project
tags: [opensource, farmdog, indie]
date: 2012-09-19 10:49:11
---

Part of a Farmdog project I'm working on needs nice syntax highlighting for markdown. After searching around for a bit I found Ali Rantakari's [PEG Markdown Highlight][1] project, and knew that it would be a perfect fit. Unfortunately, the code was not written for [ARC][2], or Automatic Reference Counting, and my project was. Rantakari's code worked fantastic outside of ARC, but inside it needed a few days worth of love and attention. 

I tried to dig through and fix the errors in my project, but after a while it seemed like a better idea to rip it out, start a blank Xcode project and do all of the fixing there. Thus, [ArcDown][3] was born. 

ArcDown is a reference project, intended to be an example of how to use the PEG Markdown Highlight in your project. It's far from perfect, not even close to finished, and is not going to replace MacVim for me any time soon, but it is a fun project to work on at night. If you are interested, ArcDown is released under the MIT license, so, fork away.


[1]: http://hasseg.org/peg-markdown-highlight/
[2]: http://clang.llvm.org/docs/AutomaticReferenceCounting.html
[3]: https://github.com/jbuys/ArcDown