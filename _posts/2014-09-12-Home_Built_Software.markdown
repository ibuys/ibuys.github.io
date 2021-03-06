---
layout: post
title: Home Built Software and Systems
date: 2014-09-12 22:39:53
tags: [bsd, linux]
---

GigaOm is [running an article][1] written by Ralph Dangelmaier, the CEO of BlueSnap, claiming “We’ve reached the end of ‘build it yourself’ software.” It’s a nice thought, along the same lines as “We’ve reached the end of ‘host it yourself hardware’,” and “We’ve reached the end of you needing anything other than what someone else has already developed.” In the past fourteen years I’ve been in the industry though, the systems I’ve seen run the best are the ones hosted on our own hardware running our own code. Off-the-shelf software can be great for certain situations, but if you are outsourcing a core function of your business, what kind of value are you really providing? 

Admittedly, building your own software from scratch is too much for most. However, if you use the building blocks of open source correctly, you gain the best of both worlds. Functionality and flexibility. 

Dangelmaier’s claims center around an odd story of a company nearly sixty years ago who started building entire houses using an assembly chain technique. The company could spit out up to thirty homes per day; thirty identical homes. I’m sure they were affordable at the time, what I wonder is how many of those homes are still standing today. When applying that same thought process to software systems, the concept of being able to slightly customize assembly line software starts to break down as soon as the needs of the business start bumping up against the upper limits of the purchased software. 

If you never need to run that Windows only application on anything other than a single server, you might be fine. As soon as you need to expand that system to provide high availability, failover, or disaster recovery, things start to fall apart, and costs go through the roof. The initial pain of developing the software yourself is made up for later by having the flexibility to modernize and adapt your system to changing times. 

I've recently started looking at building out my own system based on FreeBSD jails. I've had a fascination with what I call the beautiful system for years, I think it's high time I stopped making prototypes and built something worthwhile.


[1]: https://gigaom.com/2014/09/07/weve-reached-the-end-of-build-it-yourself-software/