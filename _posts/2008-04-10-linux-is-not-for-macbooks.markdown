--- 
layout: post
title: Linux is not for MacBooks
tags: [linux, productivity]
---

I recently gave Linux my second, and final, serious shot at running it full time as my primary operating system on my MacBook. This time, it lasted all of three days before I dug out my Leopard install disk and began the long migration back to OS X. To preempt any questions on the subject, no I didn't [dual boot][1], and no, I didn't have a good [time machine][2] backup. I was going to force myself to learn to do things the Linux way on my laptop.

Right then I should have realized that this was going to be a problem. Using a computer should not be difficult, especially if its a Mac. Apple goes to great lengths to try to keep the operating system out of the users way, to make it nearly invisible so you can use the applications. With Linux, its more like coaxing the operating system along, trying to trick it into doing what you want. But, seeing as I'm absolutely obsessed how my computer works... I just had to try.
  
The graphical desktop capabilities of beryl/compiz/desktop effects are simply not there yet. On OS X, there are limited effects when compared with beryl, but the effects that are there work seamlessly, _every time_. There is no noticeable slowdown, and no window stuttering when moving windows around. I understand that if I had a more powerful graphics card that the graphics would look better in beryl, but they look fine in OS X with the card that I have.  The other beef I have with beryl is that it doesn't always work the way I want it to. I could never be sure if the hot corners were going to activate the expose rip off 1, or if it was going to trigger the virtual desktops2, or if it was going to do nothing at all. Wobbly windows and transparent desktop cubes are neat, but when the effects that I would like to have, the ones that actually increase the usability of the system are not reliably available, you might as well not have any of them. Most of the effects of beryl are a complete waste, and are simply there because the developers discovered that they could, not because they increase the usability of the system. Just because you can do something, doesn't mean you should.
  
I realize that the developers do their best to support all the hardware that they possibly can, but when it comes down to it, I just want all of my devices to work, and work well. Hardware support is the biggest YMMV in Linux, because you never know what chipset any given device you are using is until you find out that its not supported. Wireless support is getting better, but its still a long ways from working as well as it does under either OS X or Windows. The Network Manager applet was a big step forward, but if your card is not supported out of the box it doesn't do you any good. Ubuntu includes a "Restricted Drivers Manager" which is very nice, it allows you to download non-free drivers to enable your hardware to work, if it supports them. In the case of my 802.11n Atheros card, I had to spend quite a bit of time in the command line to coax it to work. Sine there were no Linux native drivers, I had to use the ndis-wrapper application to use a Windows driver for the card that I downloaded from Toshiba3. I never did get my built-in iSight web cam to work. Also, my battery drained faster, and my laptop ran hotter. There are additional tweaks that you can do to help with this, but I think its something that the installer should do once its aware that its on a laptop. I'm sure if Apple released the specs for their hardware that all of it would work seamlessly. But, they didn't. So, it doesn't. Life just isn't fair.

Another thing that bugs me about quite a lot of the desktop software is that it always seems to be in a continual state of "beta". Even the apps that are released as final releases always seem to have that beta feel to them. There are a few notable exceptions. I love [Amarok][3], and I really like [F-spot][4]'s tag based organization feature. However, going back to my beryl comments, beryl is included and activated by default in Ubuntu and several other distributions, and according to the main [site][5], they are only at version 0.2.1. Or is it [0.5.2][6], or 0.6.2? Compiz and beryl merged... so... right.

Also, the fonts look terrible. I'm not sure why this is exactly, but I agree with [Scalzi][7] on this one. To get any decent fonts you have to install the Microsoft fonts, but even then, they don't seem to be rendered quite properly.

Linux desktops (and laptops) have a lot of potential, its too bad that they never seem to fully realize it. I've been waiting for the Linux release that will change my opinion for 8 years now, and I've come to the conclusion that Linux is best kept where it absolutely excels: on the server. As a Systems Administrator, I've run several operating systems ranging from Windows (NT, 2000, 2003) to AIX and everything in between, and Linux is by far my favorite OS to have on a server. Unfortunately, for now, its best kept on the server.
  
* * *

1. It would be very hard to argue that the Linux version is not just a copy. Well, imitation and flattery I suppose.
2. UNIX has had virtual desktops for years, it was about time they made their way over to the Mac.
3. I don't remember the exact model or link that I found that worked, I was just happy to have _something_.


[1]: http://www.apple.com/macosx/features/bootcamp.html
[2]: http://www.apple.com/macosx/features/timemachine.html
[3]: http://amarok.kde.org/
[4]: http://f-spot.org/Main_Page
[5]: http://www.beryl-project.org/releases.php
[6]: http://compiz.org/
[7]: http://scalzi.com/whatever/?p=359
