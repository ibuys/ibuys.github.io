---
layout: post
title: Anatomy of a Crushing 
tags: linux online culture indie
---

>*We charged money for a good or service*
>
>I know this one is controversial, but there are enormous benefits and you can immediately reinvest a whole bunch of it in your project *sips daiquiri*. Your customers will appreciate that you have a long-term plan that doesn't involve repackaging them as a product.

via: [Anatomy of a Crushing (Pinboard Blog)](http://pinboard.in/blog/173/)

Exactly. I've said before that I prefer an honest transaction with a company, where I am clearly the customer, and am not volunteering to be part of the product being sold.

This post by the owner of [Pinboard](http://pinboard.in) is full of interesting information. For example, the service is hosted on three (now four) large, dedicated HP servers, which, according to [Netcraft](http://uptime.netcraft.com/up/graph?site=pinboard.in), are running Ubuntu and Apache. His database servers are MySQL, with a simple Master-Slave replication setup. I especially like this part:

>It has become accepted practice in web app development to design in layers of application caching from the outset. This is especially true in the world of Rails and other frameworks, where there is a tendency to treat one's app like a high-level character in a role-playing game, equipping it with epic gems, sinatras, capistranos, and other mithril armor into a mighty "application stack".
>
>I had just come out of Rails consulting when I started Pinboard and really wanted to avoid this kind of overengineering, capitalizing instead on the fact that it was 2010 and a sufficiently simple website could run ridiculously fast with no caching if you just threw hardware at it. ... 
>
>If you offer MySQL this kind of room, your data is just going to climb in there and laugh at you no matter what kind of traffic it gets.

Over-engineering is something we deal with at my workplace, and something I've been guilty of myself. Which is part of the reason I've been looking at moving away from virtualization, clouds, and other buzzwords and returning to the simplest, most reliable setup possible. A concept that Pinboard has nailed.


