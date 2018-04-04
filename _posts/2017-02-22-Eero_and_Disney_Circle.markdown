---
layout: post
title: Eero and Disney Circle
date: 2017-02-22 15:12:31
tags: 
---

> tldr: If you have a Circle device and an Eero mesh network, plug the Circle into the Eero connected to your modem with an ethernet cable. 

The router I bought last year just wasn’t cutting it anymore. Several times a day I’d have to turn off wifi and turn it back on again on my Mac, and I’d rarely see speeds over 12 Mbps, even though I’m paying for 100 Mbps from Mediacom. Part of it had to do with the placement of my desk relative to where the router sits, and part of it has to do with running my Mac in clamshell mode through most of the day. Whatever the reason, I was tired of it and splurged for a set of [three Eero routers][1]. Now I have one in the basement next to the modem, one in the office, and one in the kitchen, and I consistently get speeds around 70-80 Mbps from [fast.com][2]. 

I was quite happy with my setup, until random devices on my home network suddenly stopped connecting to the Internet. First it was the Apple TV, then the Fire TV, then my daughters laptop, then my other daughters iPhone, then my iPhone, and when it got to my wife’s iPhone something had to change. Of course, I knew the culprit had to be our [Circle from Disney][3]. 

The Circle is a little white box that sits on the network on controls access. It blocks content that we’d rather not have, and sets time limits, bed times, and reward systems for the kids. We have all the devices assigned to their owners and what we think are reasonable rules setup. For some reason when we hooked up the new routers I thought it’d be a good idea to move the circle out into the office; I guess I wanted to be able to see it. I sat the Circle next to the office Eero and assumed everything would be fine. It was not. 

As I understand it, the Eero works by creating a subnetwork underneath your home network that is dedicated to the routers staying in contact with each other. Eero calls the software that manages the the system “[TrueMesh][4]™”, and it lets a device float between routers in the house without slowing down network speeds. The Circle works by using a technique called “[ARP poisoning][5]”, where the Circle [becomes the default gateway][6] on the network, allowing it to manage the traffic. 

So, my theory is that when I set the Circle next to one of the satellite Eero routers, the Circle connected to the closest router and spoofed the default routers ARP address, which caused the router to not be able to communicate with the real default router, breaking the mesh network. Moving the Circle back to the basement and physically connecting[^1] it to the primary router  solved the problem. 

I should mention that the Eero also has parental controls similar to Circle’s built in. I haven’t fully explored them yet, but from what I can tell they don’t quite have the feature set of the Circle. Future software updates might change that, I’ll be keeping an eye on it. 

Overall I’m quite happy with both the Eero and the Circle. While expensive, the combination of the two gives me a fast, robust home network with detailed controls over who and what connects, what they have access to, and for how long. [^2]

[^1]:	Documentation for the Circle says that if your home internet speed is higher than 60 Mbps you should use the ethernet port. They probably don’t have a radio in the Circle strong enough to support faster speeds.

[^2]:	Also, don’t forget to dust your Eero regularly.

[1]:	https://eero.com
[2]:	fast.com
[3]:	https://meetcircle.com/circle/
[4]:	https://eero.com/technology
[5]:	https://en.wikipedia.org/wiki/ARP_spoofing
[6]:	https://meetcircle.com/circle/tech-specs/
