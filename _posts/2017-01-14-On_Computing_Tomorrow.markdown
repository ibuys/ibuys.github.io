---
layout: post
title: On Computing Tomorrow
date: 2017-01-14 09:05:02
cover: /images/covers/harvest.jpg
---

I’ve been thinking more about my defense of the Mac as a long-term computing platform, and I’m slowly coming around to understanding that at the base of my ideas is a type of willful ignorance that I should know better than to indulge in. The world is changing, computers are changing, and how we work and interact with them is changing drastically. To get to the root of this, let’s follow the five “whys” of why I need a Mac to work. 

I need a Mac to get my work done. *Why?*

Because the Mac is a Unix based computer that includes the standard set of tools I use day to day, and it’s solid and reliable enough for me to depend on to work well when I need it.

*Why do I need a Unix computer to work?*

Because I’m a devops engineer, or automation engineer, or advanced sysadmin, whatever you’d care to call this job at the moment. I work primarily with AWS, and the best tools for building the automation systems for deploying our applications use the command line. Not to mention I often need to ssh into a server to troubleshoot it. 

*Why does the AWS environment use the command line?*

Well, technically the command line is just one of the tools available, the awscli tools talk back to the AWS API, and AWS has SDKs available for popular languages. I could, and often do, write python code to accomplish what I need done. I suppose the real answer to this question is that there is currently no better interface for doing what I do.

*Why is there no better interface for doing what you need to do?*

Because designing human interfaces that make sense is difficult, especially with complex concepts. We need to be able to express logically that one bit of code needs to pull data from another bit of code which is pulling data from a database, all the while ensuring that the customer is getting the information they need quickly and easily. 

*Why are the systems you work with so complicated?*

That’s a good question. Maybe they don’t need to be, or maybe in the near future they won’t be anymore. My work involves manipulating data, building websites that allow people access to upload and download data, and ensuring that the infrastructure these systems run on remains fast and available. How much of this is now being built into platforms like AWS, Azure, and Google Cloud Platform? How much of what I do each day could soon be accomplished by machine learning?

What if you could ask your phone to generate a graph of Apple’s annual profit and loss, and be sure that the visuals it returned were accurate and reliable? What if I could tell an iPad to build a highly available, auto-scaling infrastructure for hosting the Python code in my git repository, and the iPad would just go out and build everything I needed? How far are we from AI being able to tell from looking at a git repo the details of the infrastructure it needs? In that scenario, what use is “devops” when the engineer is AWS? For that matter, how far away are we from telling the computer the logic of what we need and having it develop the code for us?

Possibly not far. A [recent article in Wired][1]explores this very possibility:

> Traditional coding won’t disappear completely—indeed, O’Reilly predicts that we’ll still need coders for a long time yet—but there will likely be less of it, and it will become a meta skill, a way of creating what Oren Etzioni, CEO of the Allen Institute for Artificial Intelligence, calls the “scaffolding” within which machine learning can operate.

That scaffolding is where I’ve been aiming my career for quite a while now, but, it may not be enough. 

> In the long run, Thrun says, machine learning will have a democratizing influence. In the same way that you don’t need to know HTML to build a website these days, you eventually won’t need a PhD to tap into the insane power of deep learning. Programming won’t be the sole domain of trained coders who have learned a series of arcane languages. It’ll be accessible to anyone who has ever taught a dog to roll over. “For me, it’s the coolest thing ever in programming,” Thrun says, “because now anyone can program.”

Basic economics says that scarcity creates value, in a world where anyone can program the skill currently required would be drastically devalued. This predicts a move from “infrastructure as code” to “infrastructure as algorithmically determined”. 

I need a Mac for what I do now, but if current trends continue I might not need a Mac for much longer to do my job. In fact, as the tech industry continues to evolve, it’s entirely possible that it will evolve to the point where it no longer needs me. When that happens, maybe I’ll finally open up that coffee shop I’ve been dreaming about for decades. 

[1]:	https://www.wired.com/2016/05/the-end-of-code/
