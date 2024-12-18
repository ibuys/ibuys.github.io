---
layout: post
title: More on 1Password
date: 2021-12-21 06:58:05
tags: mac apple culture
---

1Password 7 was an incremental improvement on 6, and 6 was an incremental improvement on 5, and so on all the way back to the [original 1Passwd](https://app-updates.agilebits.com/product_history/OPM2#v2024). But 1Password 8, which is [now in Beta](https://releases.1password.com/mac/early-access/#1password-for-mac-8.5.0-57) is a horse of a different color.

I've been trying to understand the reasoning behind the change. In a nutshell, AgileBits decided that the Mac wasn’t worth having a dedicated codebase, so they’ve thrown everything out and started over from scratch with Rust and Electron.

Over the past several months I’ve been thinking about how much I care about this, and decided that, for me, there’s a fairly short list of things I care a lot about, and the software I use every day on my Mac is one of them.

Part of what makes a Mac great is the predictability of application behavior. Once a user gains an understanding of the Mac environment, they can reasonably expect to be able to quickly pick up any other application. Things like menu items, keyboard shortcuts, help docs, and how the UI of the application are presented are standardized across the system.

Cross-platform shovelware often doesn’t care about any of that. Instead, they focus on their own UI paradigms, and often miss out on the built-in benefits of native app integration. The 1Password developers Mitchell Cohen and Andrew Beyer said as much in a recent interview on the Changelog Podcast, [episode #468](https://changelog.com/podcast/468), (emphasis mine):

> You go to a Starbucks, a college campus, you just look at your friends, family and co-workers, and they love their Macs. But you look at the software they’re using, and it’s normal software. It’s cross-platform software, web-based, a lot of times just inside of a web browser… And they don’t really think about it that way. They don’t ask for apps that look like Apple made them in the ‘90s the way that I think a lot of people kind of want us to go back and do that. And regardless of what technology we use, we’re not gonna do that. *We’re going to make an app that looks and feels like the experience that we want*, just like every other developer effectively is doing in 2021.

> I actually think that for the average college student, for instance, who uses a Mac, they’ll think of something like Discord or Slack or Notion and say “That’s what a Mac app looks like. That’s how it works.” They’re not going to point to these apps that came out decades ago, that sort of are the standard bearers for what a native Mac app is supposed to be. 

Sad, but I don't think I can argue against their point. The [concept of a Mac app](https://daringfireball.net/linked/2020/03/20/mac-assed-mac-apps) is fading, but that doesn't mean we have to like it, or even agree that it's right. 

Electron tries to mimic the native AppKit environment, and in some apps it gets pretty close. But Electron is a resource hog, that's the other downside. Slack takes up way more RAM than it should, and Microsoft's Teams makes my MacBook Air’s fans kick in every time I use it.

Electron is what you use when your company goals are more important than building the best application for your users. Honestly, how many Mac users really care about Linux? Well, at least one of the [1Password devs does](https://changelog.com/podcast/468#transcript-50).

> But one of the really important goals was we wanted a browser extension that could work without a natively-installed application on the machine. And there’s a lot of reasons for that. One, *at the time we had no Linux app, so that was a part of the market where – like, I’ve been using Linux since YellowDog on my original iMac… Whether I’m using Linux now or not, I always wanted 1Password on Linux*; and this was a really easy way to make something that would run on Linux immediately.

> The other thing is you have this thing called ChromeOS, which is this system – it runs Android apps sometimes, but it’s another place where a lot of things are done on the web, they’re done within Chrome… It’s a great place where you want a web extension or a browser extension that doesn’t need a Mac app running, or something like that. 

I would argue that even on Linux not having a native experience for Gnome or KDE or whatever they use now is *worse* than having a cross-platform Electron app that doesn't respect the local desktop environment. But, on Linux, I suppose having anything at all is a glass of ice water in hell.

Inside 1Password even the concept of what constitutes [a native Mac app](https://changelog.com/podcast/468#transcript-74) has already become diluted to unrecognizable. 

> So I wanna push back on this idea of native app, because it comes up in every conversation these days… We’ve done a ton of research, a ton of interviews, and to the normal who doesn’t watch this show and isn’t part of our Twitter tech community, a native app is an app that has an icon on your dock, that has keyboard shortcuts, that you can download and install on your computer…

I'd say that's a *very* low bar. Surprisingly, the conversation goes back to the Linux desktop experience. 

> *We’re doing things on Linux that no one’s ever done before*, for instance having biometrics and browser extension integration, and integration with the system keychain… The Linux community has been really grateful and appreciative of that, and me too, *because I love Linux*.

> It goes on and on, and we’re always going to do that, because the app isn’t very useful if it doesn’t integrate well with your computer.

> But the buttons are not NSbutton And that’s where I’m just – I don’t really care anymore. I wanna build a great product, with great features, and I think that’s true for all of us.

The developers go into detail about the amount of work they've had to do to make the next version of 1Password feel at least somewhat at home on the Mac, as far as their definition of that goes. What they don't go into detail on is how 1Password will keep up to date on the Mac as those custom details change and start to look and behave not just out of place, but out of date. When the Mac UI changes, Mac apps that have integrated with the native AppKit framework inherit the new look and functionality mostly "for free". The work that AgileBits is putting into reimplementing AppKit functionality is going to have to be maintained and updated constantly.

Seems to me that they could have saved themselves the work and updated their existing 1Password 7 codebase, but only AgileBits knows for sure. 

To be fair, Apple isn't helping themselves much here. Pushing out their own apps that don't adhere to their own HIG only encourages third-party developers to continue to use UI paradigms and design languages created for themselves, not the user.

I think 1Password 8's release will mark the start of a sad chapter in the state of the Mac. Paradoxically, it comes at a time when the [Mac has never been stronger](https://appleinsider.com/articles/21/04/12/apple-mac-shipments-grew-more-than-110-year-over-year-in-q1-2021), when the [hardware has never been better](https://daringfireball.net/2019/11/16-inch_macbook_pro_first_impressions), and when Apple is at the [top of their game](https://sixcolors.com/post/2021/10/apple-announces-record-fourth-quarter/). Even with all that being true, the actual user experience of using a Mac with popular third-party software is going to be worse in 2022 than it was [in 2006](https://web.archive.org/web/20060615173608/http://1passwd.com).


### Other Notable Quotes

[Source](https://changelog.com/podcast/468#transcript-38)
> But even on the desktop apps and mobile apps, we had web views, we had web-based integrations. And in fact, the most important part of our desktop app, which people interact with every day, has always been web-based and very heavily so. And that of course is the browser extension.

> [16:16] So it’s interesting to see people think of what we’re doing as sort of like a move, or a shift, when really it’s just taking something we’ve always cared about deeply and continuing to use it in our product for the things that appeal to us about it.

---

[Source](https://changelog.com/podcast/468#transcript-40)
> So one thing we’re very excited about with 8 is actually making it so that you do interact with all of our service and our apps, not just the command backslash as useful as it is. So that’s really on our minds.

---

[Source](https://changelog.com/podcast/468#transcript-45)
> We wanted to make sure that we were building a product that was modern and discoverable in this day and age. And we had a lot of problems there, whether you were on a Mac and switched to Windows; at the time we didn’t even have a Linux client… There were parts of 1Password that felt, looked and acted differently. And a lot of that is because of our origin story. We had two founders that started this company over 15 years ago, they built the first Mac app, and essentially built the company from the ground up that way… And when the time came to add Windows, they just hired someone to write a Windows app. They joined the company, started building up a small team; same for Android, started with one person…

---

[Source](https://changelog.com/podcast/468#transcript-84)
> We’re actually very interested in driving this approach of like write a cross-platform app using web technologies, because it’s awesome. *You get to dictate your own design language*. 

---

[Source](https://changelog.com/podcast/468#transcript-93)
> I’m not 100% – I’m still waiting to see, is there another Electron app that does unlocking with Apple Watch? We might be the only one; I haven’t found another one. But *we spent a heck of a lot of effort into the actually making our Mac app as good in 1Password 8 as 1Password 7*. 

> One of the things you brought up was the permissions dialogue not being in a separate window; we actually at one point had the app do that. That is something you can absolutely do; that’s not an Electron feature, or a problem with Electron that prevents you from having multiple windows. *We made a conscious design choice to bring the 1Password design language into these new apps*.
