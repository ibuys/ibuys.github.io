---
layout: post
title: New Mac Essentials - Quicksilver
tags: productivity mac setup
date: 2012-07-19 10:49:11
---

## Introduction ##

Setting up a new Mac can be fun, but time consuming too. As I scan the icons in my dock, I see several that will not be there when I upgrade to Mountain Lion. As well compartmentalized as OS X is, and as well as it handles applications, I still like to keep things as clean as possible. 

Part of keeping things clean is using the applications that ship with OS X. I use Safari for my browser, with my own [setup][1], Mail for Email, iChat for instant messaging, and iCal for my calendar. All of my music is in iTunes, including my Grateful Dead collection. If Apple shipped a decent Twitter client and RSS feed reader, I'd use those too, but since they don't, this is where my short list of third party applications starts.

For Twitter, I like using [Hibari][2]. It is a very simple and clean application, and I love the [design philosophy][3] behind it. I do wish it had a few extra features, like viewing someone's profile in the app, or showing photographs similarly to the way the Twitter desktop app does it, but other than that I really like it. 

My RSS feeds are all in [NetNewsWire][4], synced to Google Reader. Checking my list I see that I'm subscribed to 26 carefully selected sites. This list is continually revised, and if I find one that is not holding my interest as well as I'd like, it gets dropped from the list. 

I use [DEVONthink][5] as my [anything bucket][6] and [outboard brain][10]. I've gone back and forth between DEVONthink, Evernote, and Yojimbo, but find DEVONthink gives me the features that I want, without reliance on some amorphous cloud.  

This is where things start to get a little geeky. I initially intended for this to be a single post, but as I write, it seems like it would be better to break it down into a series of smaller posts, each dedicated to a single app. Below is the list of apps that I use on a daily basis, and each has a story. 

## Downloads ##

* [Hibari][2]
* [NetNewsWire][4]
* [DEVONthink][5]
* [Dropbox][7]
* [Quicksilver][8]
* [Caffeine][9]
* [Chrome][11]
* [MacVim][12]
* [Marked][13]
* [Moom][14]
* [OmniGraffle][15]
* [Read Later][16]
* [TextExpander][17]
* [The Hit List][18]
* [1Password][19]



## Quicksilver ##

Quicksilver is the king of productivity hacks for the Mac. Few applications can claim to have the impact on how a person uses their computer more than Quicksilver. At it's most base form, Quicksilver is an application launcher, but it is also so much more than that. Setup however, takes a bit of work. 

First, grab some plugins from Quicksilver's preferences panel. The important ones, to me, are *"User Interface Plugin"*, *"Clipboard Plugin"*, *"1Password Plugin*", and *"Web Search Module*". You can see the full list that I currently use in the screenshot below.

<a href="/media/qsprefs.png"><img src="/media/qsprefs_thumb.png" /></a>

Next, select the "Catalog" tab, then the "Quicksilver" item from the left view, and enable *"Internal Commands"*, *"Internal Objects"*, and *"Proxy Objects"*. These sources give Quicksilver some very interesting abilities. Click on the "Custom" item from the left view, and click the plus icon on the bottom and select "Web Search List". In the drawer that opens on the right, click the plus icon and edit the "Name" field to be *"ddg"*, and the URL field to be: 

    https://duckduckgo.com/?q=***

Now select the "Triggers" section of the preference pane, and click the plus icon on the bottom, then select "HotKey", and in the field marked "Select an item" type *"ddg"*, and then tab to the next field and type *"Search For"*. Next, tab to the "Target" field, which will automatically be populated with text. We do not want this text in our trigger, so we will right click on this field and select "Remove". Now click "Save". 

<a href="/media/ddg_setup.png"><img src="/media/ddg_setup_thumb.png" /></a>

Double-click on the "HotKey" field to open up a drawer on the right hand side of the preferences window and assign your preferred hot key. I prefer Option-Space. Now, whenever I type my hotkey, Quicksilver opens with the third text panel open ready for me to type my DuckDuckGo search for whatever I'm looking for. When I hit return, Quicksilver opens Safari with my search results, and since I use DuckDuckGo, I use the vi keyboard commands to navigate the results, and Command-Return to open the selected results in a background tab. 

Click the plus button at the bottom of the Triggers panel to create a new custom trigger. Type *"Current Application"*, then tab to the next panel and type *"Show Menu Items"* and click "Save". Double-click the "HotKey" field again, and assign a new key combo to this trigger. I prefer Control-Space. This trigger gives us quick access to the menu items of whatever application has focus at the time. For example, I use it quite a bit in [OmniGraffle][15] to group items. Any application that makes heavy use of menu items (like Photoshop) is a great fit for this trigger. 

<a href="/media/current_app.png"><img src="/media/current_app_thumb.png" /></a>

Create another custom trigger, but this time type *"Show Clipboard"*. The default action should be *"Run"*, so save this command and assign it a key combo. I use Shift-Command-V. Make sure you are capturing your clipboard history in the Preferences tab. 

<a href="/media/show_clipboard.png"><img src="/media/show_clipboard_thumb.png" /></a>

It is worth spending some time in the preferences, actions, and triggers portions of Quicksilver's configuration. There be gold in dem hills. I've covered what portions of Quicksilver I use, but it can do much, much more. Now that it is under rapid development again, I look forward to many more years of use. 

## MacVim ##

Tune in next time to focus on my favorite writing tool. Same bat-time, same bat-channel.




[1]: https://jonathanbuys.com/01-27-2011/Keyboard_Driven_Safari.html 
[2]: http://hibariapp.com/ 
[3]: http://violasong.com/2012/01/hibari-design-philosophy
[4]: http://netnewswireapp.com/
[5]: http://www.devontechnologies.com/products/devonthink/overview.html
[6]: http://shawnblanc.net/2009/09/yojimbo-and-anything-buckets/
[7]: http://www.dropbox.com/
[8]: http://qsapp.com
[9]: http://www.lightheadsw.com/caffeine/
[10]: http://www.wired.com/techbiz/people/magazine/15-10/st_thompson/
[11]: http://daringfireball.net/2010/11/flash_free_and_cheating_with_google_chrome
[12]: https://code.google.com/p/macvim/
[13]: http://markedapp.com/
[14]: http://manytricks.com/moom/
[15]: http://www.omnigroup.com/products/omnigraffle/
[16]: http://mischneider.net/readlaterapp/
[17]: http://smilesoftware.com/TextExpander/
[18]: http://www.potionfactory.com/thehitlist/
[19]: https://agilebits.com/onepassword
