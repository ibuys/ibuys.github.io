---
layout: post
title: AWS reInvent Conference
date: 2014-11-21 20:44:12
tags: cloud,aws,automation
---

The re:Invent conference was fascinating.

**Culture**

First, the overall experience of the conference was fantastic. There were, of course, a few hiccups along the way, that's going to happen anytime you put 13,000+ people in the same conference, but overall everyone I talked to was enthusiastic and positive about what Amazon is doing. The feel was energetic, and, importantly, *diverse*. 

I met people from many different races and nationalities at the conference, and saw quite a few women attending as well. The men outnumbered the women, probably by 10:1 at least, but they were there, and that's important. I'd like to see that number getting closer to 1:1 as the years go by. 

The conference had a Japanese track, where popular sessions were given again, this time speaking in English a bit slower, and live translation provided for a primarily Japanese speaking audience. The sessions were never very crowded, and I found that I could easily get a seat at the front. Of course, if I ever saw any Japanese waiting for a seat I would have given mine up, but there were lots of empty seats. 

One of the most poorly designed aspects of the conference were that it didn't stagger the sessions out, so at the same time each hour, 13,000 people crowded the hallways and escalators, making it difficult to get from one session to the next. 

**Scale**

The most interesting session I attended was held by James Hamilton, AWS VP and Distinguished Engineer (quite the title), titled “[Innovation at Scale][1]”. James Hamilton has been part of the tech industry for [quite a while][2]. He was formerly at Microsoft, and IBM before that, and was the lead architect on DB2 when it was ported to Unix. This guy knew what he was talking about.

> This is the next decade in our industry.

I knew Amazon was big, but I didn’t realize just how big till I sat in on this session. Amazon S3 has grown by 132% in the past year, and EC2 over 99%. AWS has over five times the capacity in use than the aggregate total of the other fourteen providers in the industry. That includes Azure, Rackspace, IBM, Joyent, and all the rest.

Every day, AWS adds enough new server capacity to support all of Amazon’s global infrastructure when it was a $7B annual revenue enterprise, back in 2004. They are big, and growing fast.

AWS is split into eleven regions world-wide, and private AWS fiber interconnects all major regions. Inside each region are very high levels of redundancy. For example, in the US East region, there are 82,864 fiber strands connecting their availability zones and data centers. In each region, there are at least two Availability Zones (AZ). Latency between the AZs is less than 2ms, and normally less than 1ms.

Peak network traffic between AZs reaches 25Tbps, and yes, that’s *terabits* per second. All AZs are in different data centers. Capacity in an AZ is added by adding new data centers. Failover between data centers within an AZ is transparent. Each AWS data center holds between 50,000 and 80,000 servers. Inbound bandwidth to a single data center is up to 102Tbps. 

Another interesting fact I learned is that Amazon has custom chips built only for them by Intel for their custom-built servers. The chips have a faster processor at a given core count than what is available to the public from this partnership because of the scale Amazon operates at.

Amazon also builds all of their own networking equipment. They found that it was a lot cheaper to build their own networking gear. Not only did the overall cost of the networking gear go down, but the availability went up. It turns out that building their own gear allowed them to specialize on solving only their problems, which is a much smaller set of problems than the entire worlds that commercial networking vendors have to solve for. Amazon spun up 8000 servers to test their networking gear before they went into production.

Amazon runs their own version of Linux, which originally started off life as a Red Hat clone, something like CentOS, but has subsequently been heavily modified for Amazon’s particular needs. For example, Amazon has built their own networking stack tuned for the volume of traffic they need to process.

A lot of the work on their hypervisor has been to eliminate the virtualization tax. In the latest system they are rolling out, the NIC in each server supports SR-IOV (Single-Root I/O Virtualization), and each VM gets it’s own hardware virtualized NIC. This results in much lower latency, and less latency jitter from the instances.

**Building the Future**

I'm not sure how long Amazon is going to own this space, but they are certainly not slowing down and waiting for their competitors to catch up. I'm more in favor of a distributed Internet than one modeled after the old mainframe, client-server approach, but the capabilities that Amazon gives other businesses can't be ignored. 

My favorite analogy is the electric company. Any business that wanted to could build their own power generators and distribution infrastructure, but it would be crazy for them to do it. The economics just aren't there. It's far, *far* more affordable, and reliable, to let the specialists do it for you, and just pay for what you use. That's what AWS is building, computing on tap, just bring your code. 

The times are changing; either keep up, or get out of the way. 

[1]:	http://www.youtube.com/watch?v=JIQETrFC_SQ
[2]:	http://www.mvdirona.com/jrh/Resume/
