---
layout: post
title: Adopting BBEdit Scripts for Vim
date: 2015-01-04 16:00:01
tags: [vim, BBedit, drdrang]
---

In addition to my experiments with the design of this site, I was also testing out BBEdit as my main writing and programming tool. BBEdit didn't stick, but I did like some of the scripting the good [Dr. Drang][1] has done, and wanted to adopt a few for MacVim. I started with three of his scripts today, one to paste and select text in one command, one to convert a tab-separated table to Markdown, and another to even up the Markdown table so it's easier to read in plain text. 

Since Dr. Drang's scripts read from stdin and output to stdout[^fn1], converting them to Vim was very easy, once I found the right syntax for my vimrc file[^fn2]. My first thought was that I would be able to copy the same syntax I use for calling the outstanding [formd by Seth Brown][2], but formd is meant to parse the entire text of the file, not just the selection. Eventually, I found my answer on [StackOverflow][3].

My vimrc file now has the following lines:


	" Even up a markdown table
	vmap <leader>mn <esc>:'<,'>!~/Unix/bin/Normalize-Tables.py<CR>
	
	" Convert a tab separated tabel to a markdown table
	vmap <leader>mt <esc>:'<,'>!~/Unix/bin/Tabs-to-Markdown-Tables.pl<CR>

The first word, `vmap`, maps the shortcut to visual selections in Vim. Next, `<leader>mn` creates the shortcuts `,mn` for *Normalize-Tables.py* and `,mt` for *Tabs-to-Markdown-Tables.pl*. 

The next part `<esc>:'<,'>` grabs the selection and passes it to the command, which starts with an exclamation point[^fn3] and ends with `<CR>`, which stands for "Carriage Return".

I need to spend some time in my vimrc file to sort out the naming convention for all the key maps, but for now, I'm thinking ",mn" for "markdown normalize", and ",mt" for "markdown from tabs". 

For the third part I'm borrowing from Dr. Drang, I wanted to paste and select text at the same time. Once again I had to turn to [StackOverflow][4], and now have this mapped in vimrc: 

	nnoremap <leader>sp :set paste<CR>:put  *<CR>:set nopaste<CR> <Bar> `[v`]
	
The first part sets the mapping, `,sp`, which I'm thinking of as "select paste", and then pastes the text from the OS X system clipboard. Next, the `<Bar>` entry strings two mappings together in Vim. Finally, `\`[v\`]` performs the selection on the last change to the text. 

So, now I can take text from Excel like this:

	Left align	Center align	Right align
	This	This	This
	column	column	column
	will	will	will
	be	be	be
	left	center	right
	aligned	aligned	aligned

paste and select it with `,sp`, followed by `,mt` to convert the table to Markdown.


	|Left align|Center align|Right align|
	|--|--|--|
	|This|This|This|
	|column|column|column|
	|will|will|will|
	|be|be|be|
	|left|center|right
	|aligned|aligned|aligned|

and finally `,mn` to even the table up nicely:


	| Left align | Center align | Right align |
	|:-----------|:------------|:-------------|
	| This       | This        | This         |
	| column     | column      | column       |
	| will       | will        | will         |
	| be         | be          | be           |
	| left       | center	   | right        |
	| aligned    | aligned     | aligned      |


As always, my thanks to the good Doctor for scripts and inspiration. 


[^fn1]: As God intended. 
[^fn2]: Someday, someone will create the perfect app for managing your vimrc file, but today is not that day. 
[^fn3]: Or a bang, if you're an old Unix guy.


[1]: http://www.leancrew.com/all-this/2012/11/markdown-table-scripts-for-bbedit/
[2]: http://drbunsen.github.io/formd/
[3]: http://stackoverflow.com/questions/2575545/vim-pipe-selected-text-to-shell-cmd-and-receive-output-on-vim-info-command-line
[4]: http://stackoverflow.com/questions/4312664/is-there-a-vim-command-to-select-pasted-text?rq=1
