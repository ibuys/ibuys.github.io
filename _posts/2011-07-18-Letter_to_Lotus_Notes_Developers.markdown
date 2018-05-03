---
layout: post
title: Letter to Lotus Notes Developers
tags: mac productivity
date: 2011-07-18 10:49:11
---

I have some issues with the design of Lotus Notes. I'm a relatively new user, I started using Notes in 2006, and at the time we were using 6.5 on Windows. I've since upgraded to 8.5.2 on Mac OS X. 

The very first thing that strikes me is the default "new mail sound" on the Mac:

<audio controls="controls">
  <source src="/media/Lotus_New_Mail.ogg" type="audio/ogg" />
  <source src="/media/Lotus_New_Mail.mp3" type="audio/mp3" />
  Your browser does not support the audio element.
</audio>

Now, imagine hearing that sound several times a day. I eventually got tired of having my Mac muted, and copied the new mail sound out of Mail.app and into Lotus Notes. Here is how it sounds now:  

<audio controls="controls">
  <source src="/media/Mac_New_Mail.ogg" type="audio/ogg" />
  <source src="/media/Mac_New_Mail.mp3" type="audio/mp3" />
  Your browser does not support the audio element.
</audio>

Much better. The original sounds like a carousel at a carnival or something. I would love to hear the rational behind that sound.

Secondly, there are preferences. Lots and lots of preferences, spread all over the place. Each day I start Notes at work, and someone will send me a link to a web site. I’ll click on that link, and each day an error will pop up saying “Unable to launch program”. I click “OK”, and then remember that I need to set my default browser in the Notes preferences. That is not a design issue, that is just buggy software. The design issue here is where I need to go to find the preference to change the default web browser.

On a Mac, all well designed applications’ preferences can be opened by pressing the key combination “Command + ,”. Notes also recognizes that key combo, but only opens a subset of the available preferences called “User Preferences”. The User Preferences are also available under a submenu named “Preferences” under the main Lotus Notes menu. In addition to the User Preferences, there are also menu options for Toolbar Preferences and Status Bar Preferences. Each menu option opens up a similar looking window with a plethora of options for changing different aspects of Notes’ appearance or functionality. None of the options change the default browser.

Under the “File” menu, where only functions relevant to the currently opened document should appear, there are four more menus leading to submenus for additional preferences: Application, Replication, Locations, and Instant Messaging. Under the Locations menu, there is a submenu option to "Manage Locations". This opens a new tab in front of the mail applications tab in the main window of Lotus Notes. Double-clicking on “Online” opens up a third tab with options defining how my Lotus Notes client connects to the Lotus Notes server. This tab has sub-tabs. The fourth sub-tab over is labeled “Internet Browser”. Clicking on this tab shows a screen with one option for choosing the web browser. Double clicking on the name of the browser, or clicking on the edit button towards the top left hand corner of the locations tab will show a drop down menu. Clicking on the drop down menu does not drop down a menu, but opens up another window where I can then choose the default browser. Then, I need to click “Save & Close”, close the Locations tab, and then I’ll be able to click on the link.

This is completely unnecessary. Mac OS X keeps the default browser settings, so all an external application needs to do is pass a URL to OS X (via the NSFileManager class, if you are into Obj-C), and the OS will launch the appropriate application to handle the protocol.

This doesn't even begin to get into other standard Mac practices like pressing Command-N to start a new email (Notes tries to create a new application?), the lack of spotlight integration, or the fact that none of the controls are standard controls. No syncing with Address Book or iCal, and the text fields do not inherit the standard NSTextField or NSTextView functionality. The UI is literally surrounded by buttons. Lotus Notes is a very powerful application, but all I want to do is check my email and calendar. Every now and again I use it to send a time-off request. 

I understand that Notes has a long history, and I understand that it is a cross-platform application. I've also read the paper([pdf][1]) on the redesign of Notes, and commend the team on bringing Notes this far. However, I believe the application has a long way to go, assuming a goal of Lotus Notes is to be a viable mail application on Mac OS X, and not just what the company forces the user to use. 

I'm willing to help in any way I can.

[1]: http://www.notesdesignblog.com/NotesDesignBlog/NDBlog.nsf/dx/cs148-comstock2.pdf/$file/cs148-comstock2.pdf
