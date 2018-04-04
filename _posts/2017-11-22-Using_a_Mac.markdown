---
layout: post
title: What's a Computer?
date: 2017-11-22 09:52:44
tags: mac, ipad, apple
---



I've been enjoying watching the new iPad commercial of a kid and her iPad roaming around the city. Two things come to mind. First, is this what it's like for kids in the city? Having never lived in one myself I find it fascinating that she just roams around, takes the bus, hangs out in an alley, whatever. Second, and more important, is what she's doing with that iPad. 


<iframe width="560" height="315" src="https://www.youtube.com/embed/sQB2NjhJHvY" frameborder="0" allowfullscreen></iframe>

The first time we see her with the iPad she’s chatting with a friend over FaceTime, snaps a screenshot, and draws on it. She shows the screenshot to her friend, then sends a copy of it over Messages. Next she’s in an alley with a bunch of furniture, sitting in a seat and twisted to her left to type on the iPad keyboard. She notices a praying mantis on a leaf next to her and quickly snaps a photo, dropping that picture into what looks like a Pages document about bugs in the city. We see her typing in a bakery, drawing in a tree, and reading a comic on the bus. Finally, she’s lying in the grass in her backyard typing again, and when her neighbor asks her what she’s doing on her computer, she replies “what’s a computer?”

We’ll put to the side the ridiculousness of that question, as we the viewer are supposed to assume that the next generation is going to grow up using the tablet form factor and will have no idea what a classic desktop computer is. It’s a stretch, but ok. The commercial calls back to a [previous iPad video][1] that shows people working in different ways in different occupations using an iPad Pro. In the previous video they use the camera to capture and analyze athletic performance, they type and draw, share building schematics, and use the iPad in place of printed technical manuals. Both commercials point to the type of lifestyle and *work-style* that Apple believes the iPad is best suited for. 

In no video does it show a developer sitting at his desk for eight hours a day starting at the screen and trying his level best to edit code, ssh into servers, and manage his git repositories. All things that are technically possible on an iPad Pro, but not *better* than they are on a Mac. A few months ago I bought an iPad Pro, Smart Keyboard, and Pencil and attempted to work only using it. The experience was very similar to using a laptop. The screen was small, and I wound up hunched over my desk for several hours a day struggling through tasks that were second nature on the Mac. Before my two-weeks were up, I wound up returning the iPad and getting my money back. I bought a 27” iMac instead, [and it’s been fantastic][2]. 

However, the experience made me think about what kind of work I do and how I don’t want to get stuck in the past while the world moves on around me. There’s a thin line between waiting for the technology to mature to the point where you can use it without *stress*, and growing stagnant. There is a fairly good chance that many new developers in the next ten years might not have worked on anything but an iPad, depending on if they got one issued to them in school or not. I want to be able to move to the new technology when it’s ready for me, but judging when it’s ready might not be something I can do objectively, but I think we can lay some ground rules. 

**The iPad needs to be able to connect to an external monitor and trackpad.**

Yes, I can hear the “but it’s a touch interface” objections from here. To answer that I’d like to point at the current iOS feature to 3D press on the keyboard to move the cursor in a text field. Like Jason Snell has argued, they’ve already given us a mouse-like interface, why not take it all the way? It’s probably healthier to move around all day like the kid in the video, but there are a whole lot of us who have a desk they sit at every day, and the iPad is simply poorly ergonomically designed for long periods of work. 

**The iPad needs to be able to run a full suite of Unix tools.**

So much of my development work happens in Terminal.app. For example, in one of our applications we need to run a [Django][3] app that uses a ssh tunnel to a MySQL server, and then be able to load the Django site by browsing to localhost on a particular port. One could argue that if *that’s* the kind of work you are doing, you should just use a Mac. I’d argue that loosening of the iPad restrictions *just a bit* would open the device up to an entirely new class of user. They don’t need to give full access to the Unix underpinnings of iOS to provide a Unix development environment, they could chroot the user in a sandbox. It’s technically possible, but not currently possible. 

**The iPad needs a local and remote backup solution.**

I worry about my data. Too much, obviously. My Mac runs the classic [3-2-1 backup system][4] (three copies of your data, two local, one remote). iCloud backup could work, but a local Time Machine would be even better. Being able to restore just one file to what it was an hour ago is, at times, priceless. I’d say we are probably closest to having this, depending on the app you are using, but a system-wide, effortless, file-level backup and recovery system would be fantastic.[^1] 

I may be able to switch to an iPad before all these three things happen, but it would be so cumbersome and difficult that my work would suffer as a result.

What I don’t want to do is jump on the “it’s not a real computer” bandwagon. That’s the same argument that was used against Macs for years, back when my Mac was the only one in the company outside of design. The Mac was derided for years as an expensive toy by IT departments and PC enthusiasts. They were wrong then, and those saying it’s impossible to get any real work done on an iPad now are wrong. What I’m saying is that *for now*, it’s impractical for me to use an iPad for every day work, but I don’t think it’ll stay that way forever. For now, there simply is no alternative to the command line to do what I do. In the future, that might not be the case. 

I’ve found it interesting to look at how work was done before computers became commonplace. Writers used typewriters, which served as the models for how computers first evolved, but I think the more interesting occupation to look at is that of an [architect working at a drafting table][5] or a drawing board. They might have done some sketching or taken down some ideas in a notebook, but the real work happened with an expansive canvas in an environment that was conducive to long periods of uninterrupted work. 

The iPad Pro right now is a professional notebook. I’m waiting for it to be a drafting table, something similar to the [Microsoft Surface Studio][6], but without the suck. 


[^1]:	I know, the iPad isn’t supposed to worry about “files”, but then again it does have a Files app now, so I’d say that argument also went out the window. 

[1]:	https://www.youtube.com/watch?v=5_pMx7IjYKE
[2]:	http://jonathanbuys.net/imac-two-months-in/
[3]:	https://www.djangoproject.com
[4]:	https://www.backblaze.com/blog/the-3-2-1-backup-strategy/
[5]:	https://en.wikipedia.org/wiki/Drawing_board
[6]:	https://www.theverge.com/circuitbreaker/2016/10/26/13380462/microsoft-surface-studio-pc-computer-announced-features-price-release-date
