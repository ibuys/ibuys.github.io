---
layout: post
title: Dropbox and AWS
date: 2018-03-04 14:39:53
tags: [aws]
---


Dropbox apparently saved a boatload of money by moving their infrastructure off of AWS and building out their own data centers. Taken at face value this might seem like a strike against AWS, but the way I see it this was the only way Dropbox was going to be able to differentiate themselves as a service. Their job is to provide cloud storage, something AWS can do easily, but if that’s the only thing you are getting from AWS, it’s going to cost an arm and a leg. This news once again got me thinking about the industry as a whole, my place in it, and how I think about cloud services. 

If you've been in the technology industry for a while it's easy to think about cloud services like AWS as just another data center. A place where you can spin up a new virtual machine and manage your server instance just like you would if you were racking hardware or using VMWare. AWS will happily let you do that, but you'll be missing out on the advantages that thinking about the cloud as a development platform offers.  

The biggest innovation from AWS is that you only ever pay for what you use. Compare this with managing a data center, where you have to purchase enough hardware to handle peak utilization for the next several years, and then watch as your investment sits mostly underutilized for most of the time. You also have to make an educated guess about expansion for the next few years. Did you buy enough storage? How about memory? Will you need to purchase more in the future? How much of an interruption will that be if you do? Cloud services take care of all of that by only providing what's needed when you need it, as long as you take advantage of what the platform offers.   

Over the years I’ve noticed a trend towards more simplification in the systems that I build and design. In general, the fewer moving parts in a system the better. It will be more reliable, and easier to troubleshoot when something does go wrong. Unfortunately, I’ve also watched as the industry went in the opposite direction, building card houses out of frameworks and management systems barely out of their infancy. It may be that I’m jaded by my experience, or it may be that I’m just a grumpy old man, but whenever I hear about someone building out a Kubernates infrastructure to run their Docker containers in the cloud I get the suspicion that someone along the way got a case of the *clevers*[^1]. Is that necessary? Is it *really*?  

I should specify that the fewer moving parts in my part of the systems I build the better. Amazon, Google, and Microsoft undoubtedly have several layers of gears running their underlying systems, but the trick here is that they use those same layers for thousands of customers running millions of workloads. For example, my favored system uses very small instances in an autoscaling group to automatically add and remove capacity as needed to reflect the ebb and flow of normal business traffic. If sales sends out a big promotional email, the system will recognize the increase in traffic and spin up enough instances behind the load balancer to be able to handle it. When traffic dies back down, the system terminates the additional instances. All transparently behind the scenes. The configuration for the build is simple enough, and the documentation for what each component does is straight-forward. What’s more, Amazon themselves use the same systems to build out higher level services. 

Growing your instance size or changing it’s type is also a simple matter. If the base size is too small or too big, a simple adjustment to the CloudFormation template will automatically create a new instance, deploy the latest revision to the application to it, and shut down the old one. Building on the massive scale of AWS, it’s virtually guaranteed that you’ll never run out of resources. Also, unlike hardware in a data center, Amazon’s instances tend to get both *faster* and *less expensive* with each new release. Simply upgrading your instance type can save time and money.

For a lot of business out there that aren’t Dropbox, AWS can provide you a path to simplification of your infrastructure where you can build up secure, scaleable, and cost effective environment. If this sounds appealing, but you need someone to handle the complexity for you, get in touch, maybe we should talk.
 

[^1]:	Much respect, Mr. Poush. 👊