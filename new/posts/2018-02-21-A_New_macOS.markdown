---
layout: post
title: A New macOS
date: 2018-02-21 20:12:26
tags: [mac, apple]
---

I've heard several people on podcasts or blog posts claim that they'd like to see Apple hold off on new features that nobody wants and just fix the existing bugs in the Mac. This claim is normally followed up with a missive that they can't imagine what Apple could add to the Mac at this point anyway, since macOS is a stable, mature operating system. Well, I can think of a few things.

Let's start with the Mac's management of information. There is, supposedly, artificial intelligence baked into the Mac in the form of [Siri][1], an AI assistant that is supposed to be able to answer questions and perform basic tasks. Basic, as in "far too basic". I've yet to find a way that the AI actually helps me get anything done. Siri has hooks into all of the built-in apps that manage my information: Notes, Contacts, Reminders, Calendar, Mail, Spotlight, and the file system, but doesn't help me find relevant information unless I specifically ask her for it. What if Siri could suggest additionally relevant information with a simple swipe of the trackpad? The "Today" view in the Mac's right-hand sidebar would be a perfect place to show relevant files, folders, emails, contacts, notes, or tasks based on textual analysis and AI.

If you have an email selected in Mail, you could swipe over from the right and see a list of other information related to that email. Likewise if you select an event in Calendar, or a Note, etc… Eagle-eyed readers will most likely note the similarities between my suggestion and the fantastic [DEVONthink][2]. That's no accident. I've felt for a long time that the AI at the core of DEVONthink would be spectacular if built into macOS. In DEVONthink, selecting a file and clicking on their little top hat icon will show you a list of related documents and suggest an appropriate group, or folder, for the document. I'd like to see the Mac [sherlock][3] that bit of functionality and expand it to the entire system.

Speaking of things that should be system-wide, how about tags? I suggest the next version of macOS come with the ability to tag everything. Let's put tags in notes, todos, calendar events, contacts… the entire suite of productivity apps built into the Mac. The whole shebang, as they say. And, to be clear, let's make sure they are the same tags, not siloed tags unique per application. That wouldn't be nearly as useful in the big macOS data soup. 

Next, you know how Apple bought the iOS app "Workflow"? How about we stop messing around and ship Hazel as a built-in part of the Mac. It already fits right in, running invisibly in the background and acting on rules set in the preference pane. Of course, if Apple bought it we could put rules for everything in Hazel. We could have Hazel triggering rules not just for files and folders, but for Mail, Calendar, Reminders… [are you getting it][4]?

Finally, let's build in real security into every part of the Mac. I suggest private key encryption for everything before it is sync'd off of the machine. Transmitting files over SSL is fine. Storing files on the server on an encrypted disk is also fine. However, the files themselves are not encrypted, which means (as I understand it) that if the iCloud server is running the files are available. The encryption on the server just means that if someone tried to run off with the hard drive they couldn't get into it. That's why you can get to them from the web. Your login to icloud.com does not unencrypt the files, it simply allows you access to them. End-to-end private key encryption would be the next step that Apple could take to ensure that their customer's information is safe and secure, even when transmitted across the Internet. 

The purpose of a computer is to be a [bicycle for the mind][5], a way to not only manage information, but help you make better decisions, cook better meals, make better deals, build better software, write better papers. Whatever you do, a computer should seamlessly help you do it better, and get out of your way to let you do it.

If the Mac is the pickup truck, [or SUV][6], of the computing world, and the [heaviness of macOS][7] is what lets iOS stay light, then my suggestion is to lean into that philosophy and make the Mac the absolute best tool for managing information. A professional grade tool for professional daily use. And, obviously, since this is us, do it with *style*.


[1]: https://www.macworld.com/article/3088224/macs/how-to-use-siri-on-macos-sierra.html
[2]: http://www.devontechnologies.com/products/devonthink/overview.html
[3]: https://www.cocoanetics.com/2011/06/on-getting-sherlocked/
[4]: https://youtu.be/vZYlhShD2oQ?t=150
[5]: https://www.brainpickings.org/2011/12/21/steve-jobs-bicycle-for-the-mind-1990/
[6]: https://sixcolors.com/post/2016/12/cars-and-trucks-and-mac-suvs/
[7]: https://daringfireball.net/2010/12/future_of_the_mac_in_an_ios_world