---
layout: post
title: Install Gems Without sudo in macOS
date: 2017-04-26 07:33:39
tags: 
---

I came across a neat little command line tool via [Rob Griffiths' Robservatory][1] this morning, a Ruby gem named iStats[^1]. Install is easy enough in Rob's example, `sudo gem install iStats`, except that when you use `sudo` to install gems you are using the default macOS Ruby, and installing to system paths. 


	➜  ~ /usr/bin/gem environment                            
	RubyGems Environment:
	RUBYGEMS VERSION: 2.0.14.1
	RUBY VERSION: 2.0.0 (2015-12-16 patchlevel 648) [universal.x86_64-darwin16]
	INSTALLATION DIRECTORY: /Library/Ruby/Gems/2.0.0
	RUBY EXECUTABLE: /System/Library/Frameworks/Ruby.framework/Versions/2.0/usr/bin/ruby
	EXECUTABLE DIRECTORY: /usr/local/bin
	RUBYGEMS PLATFORMS:
		ruby
		universal-darwin-16
	GEM PATHS:
		/Library/Ruby/Gems/2.0.0
		/Users/jonathanbuys/.gem/ruby/2.0.0
		/System/Library/Frameworks/Ruby.framework/Versions/2.0/usr/lib/ruby/gems/2.0.0
	GEM CONFIGURATION:
		:update_sources => true
		:verbose => true
		:backtrace => false
		:bulk_threshold => 1000
	REMOTE SOURCES:
		https://rubygems.org/

While that *might* be fine, my personal preference is to keep the core system as close to default as possible. I once ran into an issue keeping [Jekyll][3] up to date,  so now I use the excellent [Homebrew][4] to install an updated version of Ruby and keep the gems in `/usr/local`, which is entirely mine and safe to write to. 

`brew install ruby`

Also, I make sure that `/usr/local/bin` is called before `/usr/bin` in my shells PATH variable.

`export PATH=/usr/local/bin:~/Unix/bin/:$PATH`

Now I can call `gem install iStats` and the gems will be installed safely, keeping my core system clean and my gems easily updatable. 

[^1]:	As Rob points out, this is apparently not associated with [iStat Menus][2].

[1]:	https://robservatory.com/see-sensor-stats-in-terminal/
[2]:	https://bjango.com/mac/istatmenus/
[3]:	https://jekyllrb.com
[4]:	https://brew.sh
