---
layout: post
title: Paragraphs
tags: farmdog indie paragraphs
---

![Alt Text](/media/pgraphs.png)

In the back of my mind, I always knew that the name "Scout" made no sense. I like the name, I like the bit of a kick the "Sc" at the start of it makes, and the snappy end with the "t". It sounds good, but there is no correlation between what this application does, and what it *was* named. 

Scout is now  **Paragraphs**.

>paragraph |ˈparəˌgraf|
>
>noun
>
>a distinct section of a piece of writing, usually dealing with a single theme and indicated by a new line, indentation, or numbering.
>
>verb [ with obj. ]
>
>arrange (a piece of writing) in paragraphs.

And, as you can see by the image above, we now have a snazzy new icon. I spent a long time thinking about the name and icon, and how they related to the function of the app. I commissioned two icons to be created. The first one was intended to look at home in the dock, and mimicked the "chrome circle with something inside of it" look 

![Alt Text](/media/Scout_512_copy.png)

It's a fine looking icon, and I might find some use for it eventually, but I think it accomplished it's goal of "fitting in" a bit too well. To me, it looks bland, without character. For days after receiving the final icon I racked my brain about what to do. I even got out Photoshop and tried to edit it myself, to no avail. Then I remembered Shawn Blanc's article about his grandfathers [Royal Quiet De Luxe typewriter](http://shawnblanc.net/2013/03/royal-quiet-de-luxe/), and the pieces started to fall into place. 

In addition to the name and icon of Paragraphs (I'm still having trouble not calling it Scout), I've squashed a ton of bugs, and added a few niceties. If you highlight a word and press Command-I, the word will be surrounded by asterisks, Markdown syntax for italics. Similarly, pressing Command-B will surround the word with two asterisks, Markdown for bold. Finally, highlighting a word, while you have a link on the clipboard (meaning you just copied a link from Safari or another browser), and pressing Command-L will format the highlighted word as a Markdown link. It's pretty snazzy if I do say so myself. 

I've put a lot of work lately into the animations, trying to make them as smooth as possible. There is still work to do there, but I think we are miles ahead of where we started. I also have a new theme that will ship with Scout, thanks to Kev Rodgers. Now Paragraphs will have the Default theme, a minimal CSS "Plain" theme, and Kev's "Fresh Install" theme, which also looks quite nice. I hope to add many more in the future. RSS feed is fixed again, and I've put a lot of additional checks into the site parsing code to ensure that Paragraphs can continue running if it can't build the site for some reason, testing that strings are valid, not null, and not empty, before using for example.

I got word today that the DUNS number for Farmdog Co. has been approved, and will be available to use in two weeks. So, barring any unforeseen disasters, we should be looking at a product launch within the next month. However, I've read that you should never pre-announce shipping dates, so take that with a very large grain of salt.
