---
layout: post
title: New Mac Essentials - MacVim
tags: mac setup productivity vim
date: 2012-07-29 10:49:11
---

Investing time learning a text editor is a serious commitment. Over time, you find yourself reaching for the editor's built-in shortcut keys everywhere you type. In my case, I do almost all of my writing in [MacVim][1]. Unfortunately, MacVim comes with a fairly steep learning curve that many are unwilling to tackle. Part of the complexity of Vim, from which MacVim is derived, is the configuration. Over the years I've come up with a setup that works for me.

*Downloads*

* [MacVim][2]
* [Starter Configs][3]

*Included Plugins*

* [Pathogen][4]
* [Command-T][5]
* [Surround.vim][6]
* [Repeat.vim][7]
* [Supertab][8]
* [snipMate.vim][9]
* [NERD Commenter][10]

*Configuration*

My configuration is kept in Dropbox in a folder named Vim. I create three [symlinks](https://en.wikipedia.org/wiki/Symbolic_link) in my home directory.

    ln -s ~/Dropbox/Vim ~/.vim
    ln -s ~/Dropbox/Vim/gvimrc ~/.gvimrc
    ln -s ~/Dropbox/Vim/vimrc ~/.vimrc

MacVim is customized through plugins. The history and legacy code behind the plugins make them unwieldy to maintain, so the first plugin I install is one to manage other plugins. [Pathogen][11] by Tim Pope allows you to use Git to install other plugins, and keep them nicely organized in `~/.vim/bundle`. The GitHub page for Pathogen includes simple installation instructions. From here, to install other plugins, clone that plugin's Git repository into the `bundle` directory.  

I have found that the list of plugins I use changes every so often according to what language I'm working in or what task I'm working on. Vim is much like Linux… infinitely tweakable, and, if you are not careful, it can turn into a vast time sink. However, if you can curb your nerd impulse to optimize endlessly, and find a configuration that works for you, Vim will be your constant companion, always there for you when needed. 

[1]: https://jonathanbuys.com/08-04-2011/Text_Editing_in_MacVim.html
[2]: https://code.google.com/p/macvim/
[3]: https://www.dropbox.com/s/ibwodymcbt2u1i4/Vim.zip
[4]: http://www.vim.org/scripts/script.php?script_id=2332
[5]: https://wincent.com/products/command-t
[6]: https://github.com/tpope/vim-surround
[7]: https://github.com/tpope/vim-repeat
[8]: https://github.com/tsaleh/vim-supertab
[9]: http://www.vim.org/scripts/script.php?script_id=2540
[10]: https://github.com/scrooloose/nerdcommenter
[11]: http://www.vim.org/scripts/script.php?script_id=2332

