---
layout: post
title: The Mediacom SSH Issue
date: 2018-03-07 08:38:50
tags: [networking, work]
---

Sometimes it’s a miracle the Internet works at all. For the past week or so I’ve been unable to clone, pull from, or push to private Git repositories from either Bitbucket or Github using the normal `git clone git@bitbucket.org:whatever/whatevs.git` syntax. The problem had the symptoms of a blocked port or a bad network route; I’d issue the command in Terminal and wait, and wait, and wait, and the command would eventually timeout. After a quick look at the Github documentation I tried `ssh -T git@github.com` which also timed out and confirmed my suspicions. The ssh protocol was not getting through, but VPN and normal web traffic was. 

My first thought was that the issue was probably related to my new Mediacom modem. For my wife’s sake, we recently went back to cable, and when the installer came out to the house he replaced my modem with a newer, fancier one. I don’t think I needed the upgrade, although my speed has been bumped up a bit since the new one was put in, so whatever. Along with the new modem the installer was insisting on setting up “home networking”, which is Mediacom’s way of charging you to use their crappy wireless built into the modem. I explained to the installer that not only do I not need his assistance setting up my network, but that I also have invested in a very nice [Eero mesh networking][1] setup that was far better than anything Mediacom could give me. 

This resulted in a few phone calls between the installer and his supervisor. The installer informed me that he couldn’t turn off home networking or I’d be charged an additional $40 per month. That seemed ridiculous to me, but again, whatever, I asked the installer to just make sure my wireless worked the way it did before he came out. He obliged, my speed was good, and he finished setting up cable and left. 

It wasn’t for a day or two that I noticed the ssh problem. It was easy enough to verify that the issue was isolated to my home network using the Instant Hotspot ability of my iPhone. I verified that ssh to my repositories still worked over cellular, and decided to get in touch with Mediacom. But, knowing what I know of them, I figured I’d better cover all my bases and also get in touch with Eero. 

I thought I might need to talk to them because I have “Advanced Security” turned on in Eero Plus. This, among other things, checks outbound traffic for known malicious destinations and blocks it. I wondered if it might mistakenly be blocking my SSH traffic, but after contacting Eero support on Twitter they verified that was not the case. They did however point to what proved to be the problem. Eero advised me to contact Mediacom and make sure that the modem was in bridge mode and that we were not in a double-NAT setup. After checking my Eero’s networking settings I saw that it had a private IP address and knew that had to be the case. 

Then I waited a week to get in touch with Mediacom because I figured explaining all this to tech support would be a nightmare. 

Turns out, it wasn’t so bad. The first person I talked to had no idea what was going on and sent me over to “Tier 2”. Tier 2 helpfully explained that they do not offer ssh service, which I was fine with because I didn’t want to ssh to Mediacom. Then my call was disconnected while I was on hold, so I called back. The third person I talked to understood exactly what I needed. He was able to turn off the wireless networking on my modem, switch it over to be just a basic modem, reboot it, and just like that outbound ssh worked again. The first two support representatives met my expectations, the third exceeded them. I should probably have higher expectations for Mediacom, but here we are. 

I’m glad to have everything working again. Not being able to clone repositories using the standard git+ssh protocol was really cramping my style. Hopefully I won’t have to change anything about this setup I’ve got now for a few more years. I suppose the next thing I look into will probably be ipv6.  

[1]:	https://eero.com