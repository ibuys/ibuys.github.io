---
layout: post
title: iCloud and Core Data
tags: culture online mac
---

I inadvertently started a bit of a [conversation](http://storify.com/Jury/the-trials-of-icloud) today when I complained about the state of NetNewsWire on Twitter. I've been a NetNewsWire user for years, and I was very surprised when it was sold to Black Pixel. My surprise turned to disappointment when the application was not updated, and now NetNewsWire has stopped working for me completely. 

I have a group of feeds in a folder called "Read", which I keep as my must-read list. It just so happens that this list is the one that has stopped syncing with Google Reader. I recall there being conversation online about moving away from Google Reader, and how it being the only RSS syncing service was Not A Good Thing. From what I can gather, the new version of NetNewsWire was going to sync it's feeds using iCloud instead of Google Reader, a move that I would have welcomed. I keep a separate account used only for syncing my Google Reader feeds, so being able to get rid of that account would be great. Unfortunately, NetNewsWire uses core data as it's data storage back end, and development has hit enough significant problems with this setup that Black Pixel decided to work on something else instead. 

Reminds me of another story, another once favorite app, Yojimbo. Bare Bones has been documenting their efforts with Yojimbo [publicly](http://www.barebones.com/support/yojimbo/icloud.html), and have had to push back releasing a new version that supports iCloud syncing several months. They had once promised that syncing would be implemented by the time MobileMe syncing was unavailable, but were unable to meet that promise. 

Black Pixel and Bare Bones have some of the sharpest, and most experienced developers in the business working on these problems, and have not been able to come up with a shippable solution. In that light, I'm actually a bit glad that I didn't try to tackle iCloud syncing with Go2, and that I've settled on using plain text for storage in Scout. The plain text setup should allow me to build Dropbox (or any other comparable technology) syncing into Scout, although I'm not sure that it will be available in version 1.0. 

The programming, it is hard. 

