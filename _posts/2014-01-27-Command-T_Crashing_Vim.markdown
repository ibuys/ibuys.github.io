---
layout: post
title: Command-T Crashing Vim
date: 2014-01-27 14:20:16
tags: [vim, mac]
---

For some reason today when I opened up MacVim and hit ,t to navigate to a file, MacVim crashed. The terminal spat out an ugly, and unhelpful error about "deadly signal SEGV", but knowing that I just invoked the Command-T plugin, the error was easy to track down. Command-T is not like other plugins that I have installed with Pathogen, it lives on its own and is not updated as a Git submodule. 

To fix the error, all I needed to do is download the latest version of Command-T as a ".vba" file and run through the install again. The install procedure is [fairly simple][1]:

> To install open the vimball archive in Vim: 
> 
>  vim command-t.vba 
> 
> Then source it: 
> 
>  `:so %` 
> 
> The C extension must also be then compiled; for instance, if Vimball installs your plugin files in ~/.vim, then you would do this: 

{% highlight bash %}
cd ~/.vim/ruby/command-t 
ruby extconf.rb 
make 
{% endhighlight %}


And now everything is back to normal. Command-T is a great plugin, I recommend it. My latest adventures in Vim are available on [Github][2], if you'd like to follow along.


[1]: http://www.vim.org/scripts/script.php?script_id=3025
[2]: https://github.com/jbuys/MyVim
