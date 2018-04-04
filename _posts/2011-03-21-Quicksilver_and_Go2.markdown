---
layout: post
title: Quicksilver and Go2
tags: farmdog go2 quicksilver
---

Go2 1.2 is in review, and when it is released it will bring a new feature that I'm hoping will speed up access to bookmarks considerably: Spotlight integration. Spotlight is amazing technology, and one of the biggest advantages OS X has over it's competition. The Spotlight search and matching algorithms can index millions of files, which makes it a perfect companion for people who have anywhere from hundreds to thousands of bookmarked server connections in Go2. So far, my own menubar indexing gets a bit choked up at around 1500 bookmarks or so. It still works, but no where near as fast as Spotlight. 

How Go2 makes its bookmarks available to Spotlight is a bit strange. When the user selects the option in the preferences, Go2 creates a folder in the users' Public folder named "Go2Data". Go2 exports each bookmark as a .go2 file inside the Go2Data folder as a basic XML file. I chose to put the bookmarks in the Public folder because, for one, the folder is not normally used, and two, the Library folder is, for all practical purposes, invisible to Spotlight. I even asked about this on [StackOverflow][1], and it seems there is no way to force Spotlight to index files inside the Library folder, which is unfortunate because that would be the perfect spot to put the .go2 files. However, I believe Public is a good alternative, we will see if Apple agrees by approving the 1.2 update.

A secondary, and unexpected, benefit from Spotlight integration is that Quicksilver can now index and launch Go2 bookmarks. Simply add the Go2Data folder as a custom "File and Folder Scanner" object to the Quicksilver Catalog, and ensure that you select a depth of 1 for the folder. I've been using this myself for a few days and I'm happy with the speed and the result matching. 

As long as nothing goes drastically wrong, Go2 1.2 should be available in the Mac App Store in a few days.


[1]: http://stackoverflow.com/questions/4902383/how-can-i-force-spotlight-to-index-my-applications-plain-text-files-in-the-user
