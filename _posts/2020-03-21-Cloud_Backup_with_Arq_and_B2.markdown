---
layout: post
title: Cloud Backup with Arq and B2
date: 2020-03-21 09:14:10
tags: mac
---

I'm a fan of the three-pronged approach to backups. I've got two different drives attached to my iMac, one for Time Machine for hourly backups, and the other for SuperDuper! for nightly clones of the internal drive. For many years I've also had BackBlaze running for a third off-site backup in case the house goes up in flames. At $6 per month it wasn't bad, but at the beginning of the year when I did a review of subscriptions and decided what should stay, it didn't make the cut. Not having an off-site backup bothered me though, and I considered starting it back up again till I heard [the guys on ATP](https://atp.fm/episodes/368) talking about [Arq](https://www.arqbackup.com) and thought I'd give it a shot. 

What I like most about Arq is that it's a standard Mac-assed Mac app. It fits in with the rest Mac environment, is light on resources, and just works as expected. The developer, [Stefan Reitshamer](https://twitter.com/reitshamer), has been working on it since 2009 and has built a good business around it, releasing a Windows version and their own cloud backup option. 

At $50 Arq itself is a bit pricy, but by pairing it with Backblaze's own B2 online storage I'm only paying around $1 per month for the storage. Compared with the normal Backblaze service price of $6 per month, I'll have recouped my money after five months of using Arq. My personal dataset that I'm backing up isn't that big, but it is important. 

I like having more control over my backups, and knowing that if I add something to the Arq backup set that it'll stay there, no matter if I disconnect a drive or if the data is deleted from my Mac. More control means that there's more setup than Backblaze or Crashplan, but that's a tradeoff I'm willing to live with. 
