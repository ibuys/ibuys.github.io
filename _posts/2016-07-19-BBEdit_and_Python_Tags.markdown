---
layout: post
title: BBEdit and Python Tags
date: 2016-07-19 08:42:20
tags: [python, ctags, bbedit] 
---

I'm in the process, a very long process, of switching from Vim to BBEdit as my primary editor. The reasons are long and varied, but boil down to me being tired of screwing around with Vim's configuration. I do a lot of work in Python now, and I'm using the experience of building and maintaining cloudchain to learn how to navigate BBEdit. Hopefully, someday I'll be as good here as I was with Vim. 

Today I learned that BBEdit ships with support for ctags, best [defined by the documentation](http://ctags.sourceforge.net/whatis.html): 

> Ctags generates an index (or tag) file of language objects found in source files that allows these items to be quickly and easily located by a text editor or other utility. A tag signifies a language object for which an index entry is available (or, alternatively, the index entry created for that object).

The tag file serves two purposes. First, BBEdit will use the tags to allow you to jump to the point in your project where the selected function was defined. Second, if you copy the tags file to a specific spot, BBEdit will use that file for code autocompletion. 

* `⌘-` -> Find the definition of the selected function.
* `⌘⎇[` -> Jump back to the point you were at in the previous file (if the function was defined elsewhere).

To generate the tags file, open your project directory in Terminal and run `bbedit --maketags`. Then copy the resulting tags file to `~/Application Support/BBEdit/Completion Sources/Python/tags`. Quit and restart BBEdit and autocompletion and function definition should both work. 
