---
layout: post
title: Sensible Information Organization
date: 2014-10-27 10:40:29
tags: [information, data]
---



There is no one application or system that is right for managing all of your information. If there were, we wouldn’t need apps like Contacts or Calendar, those things would just be merged into the Finder, or whatever mythical computing system I found myself wishing for the past couple of weeks. This is a *good thing*, even if not having a single view into all my data drives me a bit nuts sometimes. Specialization allows applications to provide a better experience for the specific type of data they were designed to handle. 

I [lamented on Twitter][1] the other day that personal information management is still not a solved problem. It’s a hard problem, because everyone’s needs for what they wish to keep and access on a computing device, how much they care about format and privacy, and the interface they prefer for accessing their data are different. What I thought I wanted, and what I spent far too long looking for, was a single application that I could actually dump *everything* into. It doesn’t exist, and it shouldn’t.

The system I’ve come up with, the system that works for me, and probably only for me, is to corral the different types of data that I wish to keep in different applications, based on what they are, and if I need access to them while mobile. 

## Types of Data

The kind of data I frequently find myself wanting to keep falls into a few categories. 

* Notes - Small pieces of text, normally nothing more than a few lines. Like meeting minutes, lists of books to read, random ideas, etc…

* Writing - Longer articles or blog posts. May include links, images, or other media. 

* Technical or Academic Reference - PDFs or Web Archives containing detailed technical information gathered for later reference when writing and professional development.

* Archived Reference - PDF scans of bills and statements. Needed at times for trend analysis (is our water bill going up?). 

* Disk Images - Install files for applications like Microsoft Office, or downloaded disk images for operating system installs. Rarely needed.

* Screenshots or other images. Sometimes needed to explain or convey ideas, Also collected for inspiration or to indulge a hobby (Someday I’m going to find the perfect 1967 VW Beetle).

* Scripts or Automator workflows - Home-built tools for automating reproducible Mac workflows. 

* Recipes - Everything from scanned PDFs of my wife’s great-grandmothers notecards, to saved web pages.

* Receipts - I need to be able to grab scans of these on the run quickly and easily. Good to have for later analysis of spending habits, and for tracking business expenses while traveling. 

## Requirements

Deciding on the right place for this data depends on defining the requirements up front. 

* Data must be stored in, or easily exported to, an open format.
* Mobile data must be available and editable on all devices.
* It *should* be fast and easy to get to and add to my data. The less friction in the workflow the better, but not at the expense of the previous two points. 

## Mapping Purpose to Application

*Accessable Only on Local Device*

* Financial or Medical Data - Filesystem
* Disk Images - Filesystem
* Archived Reference Files - Filesystem
* Technical or Academic Research - [DEVONthink][2]

*Accessable On Mobile Devices*

* Notes    - [nvALT][3] +  [Simplenote][4]
* Recipes  - Dropbox - Until [DTTG 2.0][5], then we will see. 
* Receipts - Dropbox + [PDFpen Scan Plus][6] + [Hazel][7]
* Screenshots and other images - [Ember][8]
* Writing - Dropbox + [MacVim][9] + [Nebulous Notes][10]

For things like the directions to my kids soccer games, dragging and dropping the PDF to nvAlt will extract the text and create a new note. If need be, I can open the note in MacVim and clean up the formatting, then drop the original PDF in the filesystem under archived reference files. 

Some data types can benefit from the organization of a database application. For that type of data, I’m leaning on the additional capabilities of DEVONthink to help me process the files and clippings I collect into new knowledge. DEVONthink’s AI engine helps me find connections to other entries that I might not have realized myself, and helps me to build a more solid understanding of the topic.

I think the same basic concept applies to recipes. I’m working on building a system that can take the basic ingredients as search terms and return a collection of recipes, as well as tags for things like “lunch”, “dinner”, and “family favorite”. For now, I’ll keep the recipes in Dropbox and index them in DEVONthink. Hopefully, I’ll soon be able to import them and sync them over to the [mythical DEVONthink To Go 2.0][11].

This system is new to me, but each of the components I’ve been using on and off for years. While I do like to simplify my computing environment, doing so at the expense of a sensible system is foolish. My attempts to combine unlike files and data into the same system failed, but allowing each type of data to be manipulated by an application specifically designed to handle it looks promising. I’ll be sure to post updates as the system evolves.


[1]: https://twitter.com/ibuys/status/526009245368471552
[2]: http://www.devontechnologies.com/products/devonthink/devonthink-pro.html
[3]: http://brettterpstra.com/projects/nvalt/
[4]: http://simplenote.com
[5]: http://forum.devontechnologies.com/viewtopic.php?f=44&t=16944
[6]: http://www.smilesoftware.com/PDFpen/Scan/index.html
[7]: http://www.noodlesoft.com/hazel.php
[8]: http://realmacsoftware.com/ember
[9]: https://jonathanbuys.com/08-04-2011/Text_Editing_in_MacVim.html
[10]: http://nebulousapps.net
[11]: http://blog.devontechnologies.com/2013/07/an-update-on-devonthink-to-go/
