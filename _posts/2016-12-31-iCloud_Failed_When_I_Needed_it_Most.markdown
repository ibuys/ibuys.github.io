---
layout: post
title: What Worked, and What Didn’t in 2016
date: 2016-12-31 13:43:46
tags: [icloud, mac, iphone, apps, devonthink]
---

Part of what’s been great about using Apple products is the feeling of living just a little bit in the future. The Mac, iPod, iPhone, and iPad paved a way towards a far less complicated future, where technology was seamlessly integrated into our lives, and enhanced our day to day interactions with our work and with each other. Apple, better than anyone, understands that technology is at it’s best when it’s nearly invisible. But, living in the future comes at a price, namely a sacrifice of stability and accepted norms of *what works*. 

Yesterday we were driving to see family who lives three hours away. About a half hour into the trip I got a Skype message from a friend asking for some technical help. After he explained the problem I knew how to fix his issue, but I needed to SSH into a server to do it. Unfortunately, I left my Mac at home, and had nothing but my iPhone. Undaunted[^1], I setup a VPN and downloaded [Prompt by Panic][1]. This is where I ran into a problem. To SSH into the server I needed to get my private key[^2]. Prompt would use the key if I could get it copied into my clipboard, but getting it there turned out to be more of a hurdle than I could overcome. 

I tried to get the key from [BackBlaze][2], but the iOS client wouldn’t let me view the text of the key or to export it with a share sheet, it only told me the type of file it was, which was no help. I also thought that I *might* have a copy of the key[^3] in a zip file in my Archive folder under my Documents folder, and I recently turned on iCloud sync for my entire [Desktop and Documents][3] folders, so I thought I should have been able to get to the key from there. In what was probably the most frustrating technical failure of the night, the iCloud app refused to download any file, and any other app I had installed that also had access to iCloud also refused to download files or would simply freeze up and crash. 

The point of moving documents into the cloud was to have them when I needed them, but when I did need them the system failed. To add insult to injury, when I wanted to look up something frivolous this morning the app worked fine. I’ve since turned that feature off. If I can’t rely on it, it’s not worth it having it turned on. I *wanted* to live in the future where I never had to think about having access to my data, where it’s just always there when I need it, but in this case, the future simply isn’t ready quite yet. 

 This fiasco caused me to think a bit more about what has and has not worked in technology in 2016. A lot of virtual ink has been spilled about virtual reality and self-driving cars, but neither of them are quite ready for the real world yet, not that I’ve seen anyway. Social media has allowed [trolls to run rampant][4], [sucked our attention reserves dry][5], and [helped elect][6] the single most unqualified president in history to the highest office in the land. Twitter and Facebook have had great years in the past, but 2016 was not one of them. I’ve withdrawn almost completely from both of them, but I’m looking forward to Manton finally unveiling [micro.blog][7]. Yahoo announced that they let over a [billion accounts get hacked][8], the [DNC got hacked][9], and the [Internet of Things][10] got hacked. Overall, not a good year for online security either. A great year to be a [1Password][11] customer though.  

2016 was a not-too-subtle reminder to be critical of the organizations and devices which play a role in our lives. A reminder that trust is easily lost and not easily regained. That the promises people make are not always the ones they keep. 

So, what *has* worked? On a personal level, while I’ve been critical of my need for the application in the past, my experience with [DEVONthink and DEVONthink to Go][12] has always been exactly what the developers said it would be. I’ve never lost data, the new sync works reliably and securely, and the company continues to be active and responsive with their customers. I’ve left DEVONthink in the past, 2017 is the year I commit to it wholeheartedly. 

My Mac, iPhone, and Apple TV continue to work well. I almost never have an issue with any device. The one issue I had with my iPhone was recognized by Apple as being widespread and they fixed it for me at no cost. My particular [recipe for apps][13] on my Mac continues to work well, although I removed Byword shortly after writing it to consolidate all writing in Ulysses. Speaking of which, Ulysses deserves a special mention as being rock solid, beautiful, and reliable. It’s my favorite writing application, probably ever. Likewise, Day One continues to be fantastic, and receives my highest recommendation for consistent, intentional journalling. There’s more that’s worked over the past year, things silently working along in the background, but these are the things that stand out to me.

I work in the technology industry. I’ve spent sixteen years (so far) studying where and how it fails, what works, what doesn’t, and how to get the most out of our investment. This year my optimism took a hit, and more things than I expected failed. In 2017, I’m looking forward to finding new ways for this tech to not only become more invisible, but more trustworthy as well. 2017 is not just about personal benefit, it’s about security and social conscience as well. It’s about choosing technology that works best for yourself, and for everyone involved. I’m looking forward to exploring exactly what that means as we sail into the uncharted waters of a new year. 



[^1]:	I live in the future where this sort of thing is possible.

[^2]:	Passwords are, by default, disabled in AWS instances.

[^3]:	I’ve got a passphrase on the key itself.

[1]:	https://www.panic.com/prompt/
[2]:	https://www.backblaze.com
[3]:	https://www.apple.com/icloud/icloud-drive/
[4]:	https://daringfireball.net/linked/2016/10/18/disney-twitter-image
[5]:	http://www.nytimes.com/2016/11/20/jobs/quit-social-media-your-career-may-depend-on-it.html?smtyp=cur
[6]:	https://www.washingtonpost.com/news/the-intersect/wp/2016/11/17/facebook-fake-news-writer-i-think-donald-trump-is-in-the-white-house-because-of-me/
[7]:	http://micro.blog/about
[8]:	http://www.nytimes.com/2016/12/14/technology/yahoo-hack.html?_r=0
[9]:	https://en.wikipedia.org/wiki/2016_Democratic_National_Committee_email_leak
[10]:	http://www.npr.org/2016/10/22/498954197/internet-outage-update-internet-of-things-hacking-attack-led-to-outage-of-popula
[11]:	https://1password.com
[12]:	http://www.devontechnologies.com/products.html
[13]:	https://jonathanbuys.com/The_Recipe
