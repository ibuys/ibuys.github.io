---
layout: post
title: How Long Will macOS Be Unix?
date: 2020-03-16 08:24:43
tags: mac unix
---

<img src="/media/UNIXad.png" loading="lazy" />

I've started to worry about the Unix core of macOS. Possibly unnecessarily, but there have been a few troubling signs over the years, the biggest of which is obviously the lack of access to a decent development environment on iOS. On iOS, web development is *possible*, but only in the barest, most basic sense of the term. As soon as you need to do anything even remotely complex, like build a Django project, run the server locally, and browse the site for testing, you are out of luck. That's fine, because it's iOS and I don't need to do development on my phone, but for years Apple has been saying that they thought iOS and specifically the iPad was the future of computing. In the past few months we've seen other signs that point towards Apple looking to simplify their products to the point where they'd no longer be usable for me. 

Another obvious sign is that [Apple has deprecated][1] what they call "scripting languages".

>Scripting language runtimes such as Python, Ruby, and Perl are included in macOS for compatibility with legacy software. Future versions of macOS won’t include scripting language runtimes by default, and might require you to install additional packages. If your software depends on scripting languages, it’s recommended that you bundle the runtime within the app. (49764202)

Well, fine, for years we've needed to download the Xcode Command Line Tools to install git and a compiler. I imagine (hope) that future versions of the download will include the scripting languages needed to bootstrap [Homebrew][2].

What bothers me the most though is that Apple has [removed the man pages][3] from their online documentation. Even the old archived links no longer work. In fact, if you start at developer.apple.com/opensource, and follow the link at the bottom to "[View Unix Documentation][4]", you are brought to an extremely [out of date archive page][5] with five (5!!) links, none of which are relevant. I've been listening to Swift and Objective-C developers complain on podcasts about how the language documentation is incomplete or out of date, but that's nothing compared to what's been done to the Unix documentation. So far, the best we can get is doing a search on the open source repository… until that goes away. 

I use a Mac because I love the simplicity and reliability of the user interface coupled with a solid Unix core, and because the indie developer community produces some of the best software in the world. The text editor I'm using now for example, BBEdit. Personally I think it's clear that the Mac's model for a software ecosystem is the best we've been able to come up with. Provide a person with the ability to craft an application themselves, and be able to make a living off of doing so by selling to a global audience. This results in high quality, sustainable software built by people who care deeply about their work and are motivated to continue developing it. Not to mention that the community built between writers, developers, artists, and hobbyists is welcoming, friendly, and inclusive. 

One of the reasons for the Mac's success in the 2000's and 2010's is because it made such a great developer or sysadmin machine because of the Unix architecture. Being a Mac, if you never needed to know about it, you would never see it, but if you did need it, the Terminal app was always right there in the Utilities folder, pop it open and you're off to the races. Unfortunately, given recent moves by Apple, I'm not sure how much longer I'll be able to stay with the mac as my primary work machine. If I literally can't get my job done, I'll be forced to go somewhere else. That really doesn't sound appealing to me.


[1]: https://developer.apple.com/documentation/macos_release_notes/macos_catalina_10_15_release_notes
[2]: https://brew.sh
[3]: https://apple.stackexchange.com/questions/239484/does-apple-provide-a-web-site-with-content-of-man-pages-for-the-command-line-c
[4]: https://developer.apple.com/opensource/
[5]: https://developer.apple.com/library/archive/navigation/index.html?filter=unix
