--- 
layout: post
title: The Linux Box and Upgrading Java
tags: [linux, sysadmin, work]
---

As a general rule, I really don't like to go outside of the box when it comes to Linux. And by that, I mean that I don't like going outside of what is provided by what ever distribution you are using, be that SLES, Red Hat, or Ubuntu. A lot of people put a lot of work into making sure that the packages that are available for the distribution actually work in the distribution and do not interfere with any other apps. Linux will let you do what ever you want, but just because you _can_ do something, doesn't mean that you _should_.
  
Going outside the box can have disastrous results with Linux. Back in early 2000 and 2001 when I was installing SuSE and Mandrake on my old IBM box, I wound up in dependency hell more than once. If you've never been there, it goes something like this:
 
OK, I want to upgrade my music player to the latest version, so I'll download the latest RPM. Wait, that failed, because it depends on a newer version of some library file that I don't have, so I'll go search the Internet and try to find that. OK, found it, downloaded the rpm, and it failed to install because it depends on a newer version of some other library file that I don't have.  Looks like there's no RPM for that library, so I'll download the source code and compile it. OK, ./configure; make; make install; Nope, that failed because of a gigantic list of dependencies that are not available! At this point, you have to make a decision: Do you go ahead and find the dependencies, or do you give up and have a drink instead. If you choose to go ahead, you download the source to a dozen different packages and install them, then compile your library, then compile your other library, then go to install the rpm to find that it fails because one of the applications you upgraded along the way is, get this, too new to support your music player, and the install still fails.  Oh, and by the way, half of your other apps that used to work, don't work anymore.

This was a very real problem a few years ago, that's why there is such a focus on package managers, and why I recommend staying in the box. That's why when I'm asked to go outside the box, I always tend to meet such requests with scrutiny. Do you **really** need that? How badly do you need that?
  
Java however, is not so bad. It's one of the few apps that is self contained in it's own directory. You download the executable bin file from Sun, run the installer, and put the extracted directory wherever you choose. I normally put it in /usr/local/ Then, I do a which java, and move the original java to java.bak. Next, I create a symbolic link to the new java in /usr/local. Run java -version, and verify that we are using the new and improved java.
  
