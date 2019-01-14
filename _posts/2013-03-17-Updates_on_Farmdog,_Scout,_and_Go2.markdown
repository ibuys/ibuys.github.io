---
layout: post
title: Updates on Farmdog, Scout, and Go2
tags: [farmdog, paragraphs, indie, go2]
date: 2013-03-17 10:49:11
---

Last week I sent in the certificate of organization to recreate Farmdog as an LLC in the state of Iowa. I have the [domain name][1], [twitter account][2], and a [test site][3] built. Assuming everything goes through with the state without problem, Farmdog Co. will be ready to launch very soon. 

Scout has a couple of rough edges to clean up before shipping, I need to finish the help doc for it, and fix a couple of odd user interface inconsistencies. But, for the most part, I think Scout is ready to ship. Narrowing the scope and number of features slotted for 1.0 was a big help. I'm planning on selling Scout through the Mac App Store, as well as on Farmdog.co using Fastspring. So, I still have some work to do on Sandboxing, as well as license keys and trial limitations. Probably a few days work to get all of that integrated and tested. 

Which brings us to Go2, my professional bookmarking app. I'm rewriting Go2 from the ground up, and I'm pretty happy with how it is coming so far. 

![Alt Text][4]

When the Mac App Store launched, Go2 was there on day one. It sold well the first month, but was downhill from there. Previously, Go2 had a bit of an identity crisis as it tried to find it's place. Was it a general bookmarking app like Delicious or Pinboard? Was it a replacement for Command-K in the Finder? When customers downloaded Go2, what were they expecting? As time went on and as I talked to other Go2 users, it became clear that they were using it similarly to how I use it, as a professional bookmarking tool for quick access to servers over SSH, FTP, or as web pages. So, the newest version of Go2 builds on these strengths, and makes it even easier to get to where you want to go. Here's a quick rundown of new features:

- Importing the SSH known_hosts file.
- Search field in the status bar now launches the first bookmark when the user hits the return key.
- When you down arrow out of the search field, you can now use the forward slash key to return to the search field. 
- Overall improved look and feel

Also, interactions with Go2 are normally through opening bookmarks. So, the main interface is now in the status bar, and new bookmarks will be added through the preferences pane. 

Finally, I've abandoned core data as the storage engine for Go2, and am in the process of moving the plain text storage engine I wrote for Scout into Go2. Hopefully, this means that upgrades will be easier, and I should, finally, be able to sync through Dropbox or some other file syncing technology. This should make it easier for teams to use Go2 as their central source of truth for network servers. 

Like I said, I'm excited about relaunching Farmdog. I've learned a lot over the years, and I can't wait to get rolling.


[1]: http://farmdog.co
[2]: https://twitter.com/farmdogco
[3]: http://fdtest.site44.com
[4]: /media/Screen_Shot_2013-03-17_at_7.11.44_PM.png