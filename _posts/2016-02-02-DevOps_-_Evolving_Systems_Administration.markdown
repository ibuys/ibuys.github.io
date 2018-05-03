---
layout: post
title: DevOps & Evolving Systems Administration
date: 2016-02-02 10:11:21
tags: work
---

The phrase “DevOps” gets thrown around quite a bit, so I thought it might be helpful for me to write down exactly what it means to me. DevOps is the evolution of [systems administration][1]. A few years ago, I noticed that the SysAdmin field was finally starting to change, after years of being relatively static. For decades, A sysadmin would set up the hardware, install the operating system, setup SSH (or, telnet in the bad old days), install your application, and get it running. Even when virtualization became more mainstream and worked its way into production workloads, it didn’t change the core tasks of a sysadmin. There were simply more boxes to manage, and without appropriate configuration management, each virtual machine became a unique little snow flake. A few tools became more commonplace like CFEngine, Puppet, or Chef to ease the burden of virtual machine sprawl, but it wasn’t until cloud computing came along that the role of a sysadmin really started to change.  

I realized that the traditional role of a sysadmin was going to change over next few years, and I needed to be on the right side of the this wave of change. Today’s sysadmin needs to know code – because the entire infrastructure is based on code. DevOps as a concept means to me that the mindset of a traditional sysadmin in a data center wasn’t going to cut it for the kind of skills needed for the new environment. Hardware doesn’t matter, operating systems don’t matter, the only thing that matters is the ability to run the application, and run it in a way that is stable, scaleable, and secure. 

One has to completely change the way they think about infrastructure. A common flaw that I’ve seen is trying to treat AWS like your data center. AWS will let you do that, gladly, but it will be expensive. It’s utility computing, like water. You get your water from the local water company, and you pay for what you use. The water company will let you turn on your faucet and just run water all day, but it will charge you for it and you will pay for far more than what you actually need. That’s why you have to have tooling, in this example a faucet to turn the water off and on. In a similar manner, you need automation systems in your infrastructure to scale up and down as needed.  

The other part of the evolution is that you have to stop thinking of the infrastructure as a systems administration task, and instead think of AWS and other cloud providers more like an application programming framework. Tying into building blocks like legos, and picking the appropriate parts to run your application. 

Systems administration is evolving in the same way programming languages have, building up to ever higher layers of abstraction. DevOps is simply working with the developers to build the best possible system to run the application. 

[1]:	http://jonathanbuys.com/02-24-2009/systems-administrator.html
