---
layout: post
title: Shellshocked Security Specialists 
date: 2014-09-30 14:29:52
tags: [security, bsd]
---

Between 2000 and 2003 I was part of a small group that was responsible for the security of the network in a remote military base. The work we did there was foundational for the rest of my career, at least so far. Once a week our team shut down for the afternoon to do training, and in the training one of us was responsible for researching a topic in depth and then presenting it to the rest of the team. We built web servers, firewalls, and proxies with OpenBSD, managed our intrusion detection system that we designed and installed ourselves, we even built a honeypot to watch malicious traffic. We spent a lot of long nights, and did a lot of hard work, but it paid off. 

Part of the reason this was such a unique experience was the time. The Internet was small, and slow, and the tools we had available were rudimentary and low level. Part of it was the place, we were part of the Navy, but we were remote and isolated, and not under the constant watchful eye of senior brass. We were able to get away with more because there was no one around to tell us we couldn't. But more than either of these, the main reason was Senior. Senior was the Senior Chief in charge of our team, and he was obsessed with security. He taught college level courses for the University of Maryland, would speak at the annual Black Hat conference, and did security consulting on the side. I recently learned he's also an author of [several books][1]. His obsession with security was only met by his obsession with education, and because we were his team, we were the beneficiaries of both. 

So, for years, night and day, we built servers, ran scans, performed penetration testing, and researched, researched, researched. We were all in front of the firehose. 

It was fantastic. 

I left the security field shortly after transferring out of the team. I simply couldn't stand the level of incompetence in the general IT population among so called "security specialists". The field outside of our team was composed of people concerned with paperwork, and constant one-upmanship. This kind of security specialist seemed more interested in telling you what you couldn't do than building things that let you do the things you want. I'm a builder. 

The recent hubbub over the so named "shellshock" vulnerability in bash reminded me again of why I left the security field. I was invited to a live screencast with a chat room put on by a big name in the security industry, so I logged on to have a few things clarified. I was unimpressed. 

The vulnerability in bash is only remotely exploitable if your web application is calling out to bash, and specifically bash. The presenters came up with a few ideas when I asked them for clarification on the specifics, but they seemed contrived to me. I asked about perl CGI's, and they said it's possible that the application could be vulnerable if perl called out to bash for any exec() or system calls, but when I asked for specifics they didn't have any. I doubt that would work, since perl would need to pass along the maligned bash environmental variables, but I'd be willing to be proven wrong. 
 
Secondly, they said that "similar to heartbleed", some applications could precompile bash for inclusion instead of depending on the system bash. I asked if they could provide an example of an application that did that, but they could not. I have never heard of an application doing that, and if I found one, I think it would be incredibly poor development practices. That would be an application to avoid at all costs. I asked on Twitter if anyone else had heard of something like that, but received no response. 

These kinds of statements are a problem because they are inaccurate and generalizing in a field that depends on exact and precision correctness. It doesn't change the fact that the bug still needs to be patched, just to cover the areas we don't know about, but having a correct understanding of what the exposure of the bug is, how it can be exploited, and where there is an actual emergency speaks volumes about the reliability and trustworthiness of the vendor. 

Someone can only cry wolf so many times. The heartbleed bug was worth staying up all night to fix. This, as far as I can tell, is not.  That doesn't stop the security firms and media outlets from getting excited about it though. 

This kind of fear mongering doesn't help anyone. What does help people is having the right information so they can make intelligent, informed choices that are right for them. Senior would never have let the kind of flippant comments I heard, being presented as fact from a trusted source, leave the meeting without providing proof. To do so not only makes you look incompetent, but reflects poorly on the entire industry. Are you in this to help protect people? Or just to make a buck?   

Finally, there is this garbage of an article by ZDNet: [Apple issues incomplete OS X patch for Shellshock][2], which claims that the patch issued by Apple did not patch for all listed CVE vulnerabilities, when, according to my testing, it does. 

> Testing by ZDNet showed that while the patch fixed the issues outlined in the original CVE-2014-6271 report and CVE-2014-7169, OS X remains vulnerable to [CVE-2014-7186][3].

I ran the tests on my machine for both CVE-2014-7186 and CVE-2014-7187, and both return as not being vulnerable. 

I don't mean to demean the importance of fixing the bug, I simply want to make sure the it is correctly and accurately understood. Tech journalists and security specialists alike benefit from sensational claims, which is a shame when there are so many more pressing problems in the world they could be working on. 

[1]: http://www.amazon.com/Kevin-Cardwell/e/B00IXFSODO/ref=dp_byline_cont_book_1
[2]: http://www.zdnet.com/apple-issues-os-x-patch-for-shellshock-7000034170/
[3]: http://en.wikipedia.org/wiki/Shellshock_%28software_bug%29#CVE-2014-7186

