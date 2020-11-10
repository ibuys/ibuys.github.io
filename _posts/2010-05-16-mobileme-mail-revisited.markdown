---
layout: post
title: MobileMe Mail Revisited
tags: [mac, apple, online, productivity]
---
<a href="/media/mobileme_logo.png"><img src="/media/mobileme_logo_thumb.png" /></a>

If the only computers you use are Macs, or if you only use Microsoft Outlook on a PC, you may not have spent a significant amount of time in the web interface to [MobileMe][2].  The web interface occupies a curious spot in Apple's portfolio as one of their few products that tries to do everything, and gets very little of it right.  One piece in particular that gets most things wrong is the web interface to MobileMe Mail.

MobileMe Mail is built on [SproutCore][3], a library of Javascript and HTML 5 frameworks intended to build desktop like applications for the web.  The Mail web app *looks* like the desktop Mail application, and has certain features that try to mimic the feel of the desktop application, but falls short in functionality.  The Mail web app tries to bring the desktop experience to the web, but in doing so ignores the web paradigm that makes Gmail such a success.  I've narrowed down the problems with the web interface to five main areas.

**Speed**. Too often I've seen the dreaded "MobileMe Mail is loading" message. ![MobieMe Mail Wait Message][4]That this message even exists tells me that the application is too slow. The message is a web equivalent to an app splash screen; I don't want to see a splash screen, I want to see my mail.  Mail displays another spinning gear and a "Loading..." message when switching between folders, or sometimes just between messages in the same folder, instead of text.  These messages do not tell me that Mail is working, they tell me that something is wrong with the applications internal design.

**Search**. In the top right hand corner of MobileMe Mail is a search field.  Typing in the search filed will allow you to search in only the currently selected folder.  This is wrong.  When Apple introduced [spotlight][5] in Tiger, they made a huge deal out of it, and rightly so.  Search on the desktop changed the way I used my Mac, and the speed improvements in Leopard made it the default way I find anything. In placing this search field in the web interface, I expect to be able to search not only all of my mail in all of my folders, but all of my contacts, documents, appointments, and media available in MobileMe.  Instead, it searches in one folder in one application.  Not only that, but it appears to only search basic fields in each message, not through the text of the message itself.

**Rules**.  There are no rules for automatically processing incoming mail.  This is also wrong.  Rules should sync from the desktop Mail app.  For some users who may be using an iPad, and only and iPad, there is no way to filter incoming mail.  The lack of rules and filtering severely limits the usability of the web interface, and is another big advantage Gmail has over MobileMe Mail.

**Folders**. While Gmail has no folders and instead uses labels and search, MobileMe Mail has neither good search, nor good folder management.  The only options available for folders is to create, delete, and rename the folders.  Since Mail is unable to use search as an organizing feature, folders are the only option.

**Notes**.  It's almost hard to include notes as a part of MobileMe Mail that does things wrong, when it actually doesn't do notes at all.  iPhone OS 4 is [supposed][6] to (finally) bring notes syncing between the desktop Mail client and the iPhone over IMAP, and therefore MobileMe, but I haven't seen an announcement of the Notes being added to the Mail interface, or as an additional web service.

Apple has made strides to improve their online services since the [rocky][7] conversion from DotMac, and I hope that they continue to make the MobileMe web interface better, faster, and more usable.  Critics often call MobileMe Apple's answer to Google's, Yahoo's, and Microsoft's online services, offered at a premium price. However, it is important to keep in mind that MobileMe's Mail is not a competitor to GMail, Yahoo Mail, or even Hotmail.  MobileMe is meant to enhance the experience of owning multiple Apple devices: Macs, iPhones, iPads, and iPods, by providing a synchronization service between them for things that matter.  The web interface to MobileMe is an addition to the MobileMe service, not the service itself.

[2]: http://www.apple.com/mobileme/features/me-dot-com.html
[3]: http://www.sproutcore.com/what-is-sproutcore/
[4]: https://jonathanbuys.com/media/mobileme_wait_message2.png
[5]: http://arstechnica.com/apple/reviews/2005/04/macosx-10-4.ars/10
[6]: http://www.tipb.com/2010/04/09/iphone-40-notes-sync/
[7]: http://theappleblog.com/2008/11/12/break-away-from-mobileme-seven-services-to-help-you-make-the-move/

