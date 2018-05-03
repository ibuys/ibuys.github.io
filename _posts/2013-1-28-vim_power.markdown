---
layout: post
title: Vim Power
tags: blogging 
date: 2013-01-28 10:49:11
---

<a href="http://www.flickr.com/photos/51724787@N06/8424086311/" title="vim_icon by Jon Buys, on Flickr"><img src="http://farm9.staticflickr.com/8466/8424086311_037e32dbcf_t.jpg" width="100" height="100" alt="vim_icon"></a>No server, desktop, or laptop install is complete without Vim, and yet, there are times when I still see questions pop up on IRC about how to do basic editing of config files with vi. I remember, years ago, asking some of the same questions of an older Unix guru, and asking why I should bother learning such an eccentric and "outdated" text editor. His answer has stuck with me, he said "Because it is the only text editor guaranteed to be on every server, and some day you will need it, and have no other alternatives." Vim, short for "vi improved" is ubiquitous, but it is also so much more, and the time you spend learning it will be repaid to you tenfold in productivity. 

Vim is designed to be run from the command line, without a mouse. To get around in a file, Vim uses three different "modes", where the same keys might do very different things, depending on which mode you are in. From my experience, this is the biggest obstacle of learning Vim, wrapping your head around what mode you are in, and how to navigate the text. 

When you first launch Vim, you are in normal mode. Normal mode does not allow you to edit the text directly, but allows you to move the cursor around the text using the keyboard. The basics of what you need to know are:

* j - Move the cursor down one line
* k - Move the cursor up one line
* l - Move the cursor to the right one character
* h - Move the cursor to the left one character

Once you have the cursor where you want it, you can press "i" to enter the next mode, "insert". Insert mode behaves more like other text editors, where the keys you press show up as text characters in the file. When you are done editing, you return to normal mode by pressing "Esc". This is a good start for getting used to how Vim works, and over time, those keys will become ingrained as muscle memory, you might find yourself inadvertently reaching for the escape key after typing in a web form.

Moving around one line or one character at a time is fine, but time consuming. What if you would like to move the cursor down five lines? In that case, you would enter "5j" in normal mode. What if you know exactly what line number you would like to jump to, say line 42? Enter "42G" in normal mode, and you will jump down to that line. Or, if you would like to jump straight to the end of the document, you could just enter "G" by itself. I do this quite a bit, jumping between "1G", the first line of the document, and "G", the last. If you would like to move 10 characters forward, you would enter "10l" in normal mode. Same to move back, "10h"

What if you just moved down ten lines, and would like to move down another ten lines? You could enter "10j" again, but it would be faster to use another Vim shortcut, the humble period. Hitting "." in normal mode *repeats the previous command*. So, whatever you did last, hitting "." will tell Vim to do it again. 

Hitting "i" in insert mode will allow you to start inserting text, however, there are a few other options as well.

* a - Append, or, start adding text right after where the cursor is
* o - Create a blank line on the line below the cursor, move the cursor to this line, and enter insert mode.
* O - Same as above, but the new line goes above the cursor, not below

Once you have the basics of when and how to insert text, moving around the text becomes more important. Luckily, Vim knows text well, and has a few tricks here as well.

* w - Move the cursor ahead one word
* b - Move the cursor back one word
* ( - Move the cursor back one sentence
* ) - Move the cursor forward one sentence

What about copy and paste? Vim has that covered as well, but instead of "copying" text, you "yank" text with the "y" command. To yank the current line, which means to copy the current line, you press "yy". To paste the line, move the cursor to where you would like it and press "p" in normal mode. 

So, now that you can fly around your text with ease, and insert new text at will, what are you going to do about the plethora of typos? A few more normal mode commands to commit to memory are:

* d - Delete one character, word, sentence, or the entire file if you like
* r - Replace one character
* R - Replace all the characters till you hit escape, just write right over them

To use the delete command, you can either place the cursor over the text you would like to delete and press "d", or you position the cursor at the beginning of a string of characters you would like to delete, for example, to delete one word, you press "dw". To delete five words, you press "5dw". To delete a sentence , you press "d)". To delete the entire file, you could jump to the beginning of the file: "1G", and delete to the end: "dG". 

And if you make a mistake? No problem, Vim keeps a detailed record so you can undo the last command with "u" in normal mode. 

So, you can jump around the file, insert text, and delete text. How do you save the text? To do this, we need to enter a third mode, *command* mode. To enter command mode, you must first be in normal mode, and then press ":". You should see the cursor move to the very bottom of the window next to a colon, waiting for you. To save the file in the current working directory, you would enter:

	:w FileName.txt

If your file already has a name, then simply entering ":w" will work. 

That's most of what you need to know to become proficient with Vim, but of course, there is so much more. I've barely scratched the surface of what Vim can do on its own, not to mention Vim's vibrant community of users and developers who have extended Vim through plugins. It is through the plugins that some real magic can start happening. However, to avoid asking on IRC how to edit a text file, this should have you covered. Finally, when you are finished editing, jump into command mode and enter "wq!". 






