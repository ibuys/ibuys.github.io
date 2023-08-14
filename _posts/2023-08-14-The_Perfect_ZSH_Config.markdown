---
layout: post
title: The Perfect ZSH Config
date: 2023-08-14 07:07:34
tags: tech unix 
---

If you spend all day in the terminal like I do, you come to appreciate it's speed and efficiency. I often find myself in Terminal for mundane tasks like navigating to a folder and opening a file; it's just faster to type where I want to go than it is to click in the Finder, scan the folders for the one I want, double-click that one, scan again… small improvements to the speed of my work build up over time. The speed is increased exponentially with the correct configuration for your shell, in my case, `zsh`. 

`zsh` is powerful and flexible, which means that it can also be intimidating to try to configure yourself. Doubly-so when there are multiple 'frameworks' available that will do the bulk of the configuration for you. I used [Oh My Zsh](https://ohmyz.sh) for years, but I recently abandoned it in favor of maintaining my own configuration using only the settings that I need for the perfect configuration for my use.

I've split my configuration into five files:

- `apple.zsh-theme`
- `zshenv`
- `zshrc`
- `zsh_alias`
- `zsh_functions`

I have all five files in a `dotfiles` git repository, pushed to a private Github repository. 

The `zshenv` file is read first by `zsh` when starting a new shell. It contains a collection of environmental variables I've set, mainly for development. For example:

```
export PIP_REQUIRE_VIRTUALENV=true
export PIP_DOWNLOAD_CACHE=$HOME/.pip/cache
export VIRTUALENV_DISTRIBUTE=true
```

The next file is `zshrc`, which contains the main bulk of the configurations. My file is 113 lines, so let's take it a section at a time. 

```
source /Users/jonathanbuys/Unix/etc/dotfiles/apple.zsh-theme
source /Users/jonathanbuys/Unix/etc/dotfiles/zsh_alias
source /Users/jonathanbuys/Unix/etc/dotfiles/zsh_functions
```

The first thing I do is source the other three files. The first is my prompt, which is cribbed entirely from Oh My Zsh. It's nothing fancy, but I consider it to be elegant and functional. I don't like the massive multi-line prompts. I find them to be far too distracting for what they are supposed to do. 

My prompt looks like this:

```
 ~/Unix/etc/dotfiles/ [master*] 
```

It gives me my current path, what git branch I've checked out, and if that branch has been modified since the last commit. 

The next two files, as their names suggest, contain aliases and functions. I have three functions and 16 aliases. I won't go into each of them here, as they are fairly mundane and only specific for my setup. The three functions are to print the current path of the open Finder window, to use Quicklook to preview a file, and to generate a uuid string. 

The next few lines establish some basic settings.

```
autoload -U colors && colors
autoload -U zmv

setopt AUTO_CD
setopt NOCLOBBER
setopt SHARE_HISTORY
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_SPACE
```

The `autoload` lines setup `zsh` to use pretty colors, and to enable the extremely useful `zmv` command for batch file renaming. The interesting parts of the `setopt` settings are the ones dealing with command history. These three commands allow the sharing of command line history between open windows or tabs. So if I have multiple Terminal windows open, I can browse the history of both from either window. I find myself thinking that the environment is broken if this is not present. 

Next, I setup some bindings:

```
  # start typing + [Up-Arrow] - fuzzy find history forward
  bindkey '^[[A' up-line-or-search
  bindkey '^[[B' down-line-or-search
  
  # Use option as meta
  bindkey "^[f" forward-word
  bindkey "^[b" backward-word
  
  # Use option+backspace to delete words
  x-bash-backward-kill-word(){
      WORDCHARS='' zle backward-kill-word
  
  }
  zle -N x-bash-backward-kill-word
  bindkey '^W' x-bash-backward-kill-word
  
  x-backward-kill-word(){
      WORDCHARS='*?_-[]~\!#$%^(){}<>|`@#$%^*()+:?' zle backward-kill-word
  }
  zle -N x-backward-kill-word
  bindkey '\e^?' x-backward-kill-word

```

These settings let me use the arrow keys to browse history, and to use option + arrow keys to move one word at a time through the current command, or to use option + delete to delete one word at a time. Incredibly useful, use it all the time. Importantly, this also lets me do incremental searching through my command history with the arrow keys. So, if I type `aws`, then arrow up, I can browse all of my previous commands that start with `aws`. And when you have to remember commands that have 15 arguments, this is absolutely invaluable. 

The next section has to do with autocompletion. 

```
# Better autocomplete for file names
WORDCHARS=''

unsetopt menu_complete   # do not autoselect the first completion entry
unsetopt flowcontrol
setopt auto_menu         # show completion menu on successive tab press
setopt complete_in_word
setopt always_to_end

zstyle ':completion:*:*:*:*:*' menu select

# case insensitive (all), partial-word and substring completion
if [[ "$CASE_SENSITIVE" = true ]]; then
  zstyle ':completion:*' matcher-list 'r:|=*' 'l:|=* r:|=*'
else
  if [[ "$HYPHEN_INSENSITIVE" = true ]]; then
    zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]-_}={[:upper:][:lower:]_-}' 'r:|=*' 'l:|=* r:|=*'
  else
    zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'r:|=*' 'l:|=* r:|=*'
  fi
fi

unset CASE_SENSITIVE HYPHEN_INSENSITIVE
# Complete . and .. special directories
zstyle ':completion:*' special-dirs true

zstyle ':completion:*' list-colors ''
zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#) ([0-9a-z-]#)*=01;34=0=01'
zstyle ':completion:*:*:*:*:processes' command "ps -u $USERNAME -o pid,user,comm -w -w"
# disable named-directories autocompletion
zstyle ':completion:*:cd:*' tag-order local-directories directory-stack path-directories

# Use caching so that commands like apt and dpkg complete are useable
zstyle ':completion:*' use-cache yes
zstyle ':completion:*' cache-path $ZSH_CACHE_DIR

zstyle ':completion:*:*:*:users' ignored-patterns \
        adm amanda apache at avahi avahi-autoipd beaglidx bin cacti canna \
        clamav daemon dbus distcache dnsmasq dovecot fax ftp games gdm \
        gkrellmd gopher hacluster haldaemon halt hsqldb ident junkbust kdm \
        ldap lp mail mailman mailnull man messagebus  mldonkey mysql nagios \
        named netdump news nfsnobody nobody nscd ntp nut nx obsrun openvpn \
        operator pcap polkitd postfix postgres privoxy pulse pvm quagga radvd \
        rpc rpcuser rpm rtkit scard shutdown squid sshd statd svn sync tftp \
        usbmux uucp vcsa wwwrun xfs '_*'

if [[ ${COMPLETION_WAITING_DOTS:-false} != false ]]; then
  expand-or-complete-with-dots() {
    # use $COMPLETION_WAITING_DOTS either as toggle or as the sequence to show
    [[ $COMPLETION_WAITING_DOTS = true ]] && COMPLETION_WAITING_DOTS="%F{red}…%f"
    # turn off line wrapping and print prompt-expanded "dot" sequence
    printf '\e[?7l%s\e[?7h' "${(%)COMPLETION_WAITING_DOTS}"
    zle expand-or-complete
    zle redisplay
  }
  zle -N expand-or-complete-with-dots
  # Set the function as the default tab completion widget
  bindkey -M emacs "^I" expand-or-complete-with-dots
  bindkey -M viins "^I" expand-or-complete-with-dots
  bindkey -M vicmd "^I" expand-or-complete-with-dots
fi

# automatically load bash completion functions
autoload -U +X bashcompinit && bashcompinit


```

That's a long section, but in a nutshell this lets me type one character, then hit tab, and be offered a menu of all the possible completions of that character. It is case-insensitive, so `b` would match both `boring.txt` and `Baseball.txt`. I can continue to hit tab to cycle through the options, and hit enter when I've found the one I want. 

The last section sources a few other files:

```
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
[ -f "/Users/jonathanbuys/.ghcup/env" ] && source "/Users/jonathanbuys/.ghcup/env" # ghcup-env
[ -s "/Users/jonathanbuys/.bun/_bun" ] && source "/Users/jonathanbuys/.bun/_bun"
source /Users/jonathanbuys/Unix/src/zsh-autosuggestions/zsh-autosuggestions.zsh
source /Users/jonathanbuys/Unix/src/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
``` 
If I'm experimenting with Haskell, I'd like to load the `ghcup-env` variables. If I have `bun` installed (a way, way faster `npm`), than use that. The final two sources are for even more enhanced autosuggestions and command line syntax highlighting. So, typos or commands that don't exist will be red, good commands where `zsh` can find the executable will be green. The autosuggestions take commands from my history and suggest them, I can type right-arrow to accept the suggestion, or keep typing to ignore it. 

Taken together, I've been able to remove Oh My Zsh, but keep all of the functionality. My shell configuration is constantly evolving as I find ways to make things faster and more efficient. I don't consider myself a command line zealot, but I do appreciate how this setup gets out of my way and helps me work as fast as I can think.

--- 

> p.s. A lot of this configuration was taken from other sources shared around the internet, as well as the `zsh` documentation. I regret that I haven't kept references to the origins of some of these configs. If I can find the links I'll post them here. 

