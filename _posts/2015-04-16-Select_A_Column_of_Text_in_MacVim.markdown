---
layout: post
title: Select A Column of Text in MacVim
date: 2015-04-16 19:47:06
tags: 
---

I often need to work with columns of text; output from commands, text grabbed from a web page, what have you. Since I have a somewhat odd aversion to using a spreadsheet like a normal person, I discovered, nearly by accident, that I could easily select a column of text in [MacVim.][1] 

To do so, simply position the cursor where you would like to start, hold down option while dragging over the text you'd like to select. Once the text is selected, you can delete it, yank it, or insert new text for every row selected. 

For an example, today I needed to comment out a few lines of text in a config file. Just for kicks I selected the first two characters of every row, pressed shift "i" (a capital i), typed the hash symbol, and when I pressed escape every row of text I had selected was commented out. 

That example is a bit contrived, what I mainly use this for is just deleting columns to pair down the text I'm working with. Give it a try for yourself. I'm sure there's a way to do this without using the trackpad, but this is quick and easy enough for me to remember.


[1]: https://code.google.com/p/macvim/
