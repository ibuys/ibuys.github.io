---
layout: post
title: The Future of DevOps is AI
date: 2017-12-07 09:03:10
tags: [work, devops, ai]
---

The work of systems administration, that is, racking new hardware, running cables, and loading operating systems, is quickly becoming eclipsed by devops. Servers come from the factory ready to rack, and the base operating system has become nearly meaningless in the context of running applications thanks to Docker. All you need is a baseline Linux install, the specifics of what each application needs to run are taken care of inside the Docker container. 

If you are running your workloads in the cloud[^1], the need for a dedicated sysadmin is even more redundant[^2], since both the hardware and the base operating system are outsourced to AWS, Microsoft, or Google. However, bridging the gap between deploying applications to production and writing the application code sits devops, which for the past several years has been a fantastic opportunity for sysadmins to branch out into new and interesting ways. That opportunity is not going to last forever though. The core tasks of a devops engineer are repeatable, and the current complexity that devops now handles is moving more and more towards simplification.

In devops, there is a starting point, a set of tasks, and a specific end goal to achieve. Primarily, a devops engineer will take code from a repository and build out the systems to test and deploy that code to production in a secure, scaleable environment. That’s what I do anyway. History tells us that any repeatable, programmable task will be automated by a machine sooner or later, and I think we are starting to see what those new machines will look like. 

Jason Kottke [posted a link][1] to Chess.com earlier today about how Google’s AlphaZero AI became the best chess player in history in four hours. It wasn’t loaded with a chess program, the AI taught itself how to play, and became unbeatable. Putting [Skynet theories][2] temporarily aside, how big of a step is it from there to automating devops? An AI could be trained on Github, given AWS or GAE as a deployment ground, and given an end goal of each application up and running. 

Programmer friends who I floated this idea to in the past had mixed replies. Some claimed that the AI necessary to do this would be beyond anything currently in our capabilities. Others said that it *might* be possible. I think the writing on the wall is clear. It is possible, and I imagine it’s only a matter of time before the big three cloud providers each deploy their own version of automatic code deployment. It won’t look like much from outside, the only configuration they’ll need is access to your repository, and the AI will build up everything else necessary. 

The models exist, the artificial intelligence exists, and the need for the service exists. DevOps is a career path with an expiration date. If that date is 10, 20, or 30 years down the road, I can’t tell, but it’s closer than any of us working in the industry would care to consider. 

[^1]:	Which you really should be.

[^2]:	Well, that is *if* you are running your applications in the cloud the way the cloud was meant to be used.

[1]:	https://kottke.org/17/12/googles-ai-beats-the-worlds-top-chess-engine-w-only-4-hours-of-practice
[2]:	https://www.youtube.com/results?search_query=skynet+terminator