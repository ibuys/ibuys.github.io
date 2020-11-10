---
layout: post
title: More Scout Tips
tags: [farmdog, paragraphs, indie]
date: 2013-03-13 10:49:11
---

Eventually I'm going to need to compile this into a proper help doc, but for now, documenting Scout with Scout will do. 

Scout handles pages just a little differently than posts. New pages do not show up on the home page, and are not organized into subfolders based on date. Pages are converted into HTML and saved in the root of the site directory, right next to index.html. To create a page, add a new post, but before the title of the page add the characters `@@ `. That is two "at" symbols followed by a space. For example: `@@ Contact`.

Secondly, the default theme that ships with Scout, the theme of this site, is my own creation that I've cobbled together over the past few years. What I hope to see are a few people more talented than I create some really great themes. In fact, assuming Scout is successful, I plan on hiring a designer to do just that. However, there are a number of hurdles to overcome before that happens. 

To create a Scout theme, create a folder with the following files inside:

- atom.xml
- atomTemplate.xml
	- The two xml files are for creating the site RSS feed. 
- base.css
	- Should contain all of the site CSS
- default.html
	- The standard HTML template for the site. 
- indexTemplate.html
	- Wraps each post in a div with an id of "posts". 
- post.html
	- Creates the page template for each post
- robots.txt
	- Not currently used, but probably should be.
- screenshot.png
	- A nice screenshot of the post at 400x341 pixels.
- toc.html
	- The template for building the archive or table of contents. 

Scattered throughout the files listed above are strings that look like: YYYY_SCOUT_SOMETHING_YYYY. These are the Scout "Y Codes", as in, "why are they so ugly?" I was looking for something that was unlikely to be reproduced anywhere else, and this was the first thing that came to mind. I currently have the following Y codes defined:

- SCOUT_5ATOMPOSTS
- SCOUT_AUTHOR
- SCOUT_CONTENT
- SCOUT_CSS    
- SCOUT_CURRENTDATE
- SCOUT_CURRENTYEAR
- SCOUT_POST_CONTENT
- SCOUT_POST_DATE
- SCOUT_POST_TITLE
- SCOUT_POST_URL
- SCOUT_SUBTITLE
- SCOUT_TITLE
- SCOUT_URL

Hopefully, the titles of the codes are self-explanitory, but as I have time I will be documenting them properly. For now, you can probably take a look at how the files in default.stemplate are arranged. Scout looks for these codes in the template and replaces them with the proper data from the posts to generate the site. 

Lastly, you should never feel like you need to save your work in Scout. Scout automatically saves your work at various intervals. For example, whenever Scout looses focus as the main window, or whenever a new post is chosen, or when a new view is looked at, Scout automatically saves the current post as a plain text markdown file saved in `~/Library/Application Support/Scout/Posts/`. If you like you can watch the file being written to in the finder or as you use the application. Likewise, if you have a markdown file that you would like Scout to know about, you simply need to name it according to the naming convention of `YYYY-MM-DD-HH-MM-SSSS##Title_Of_Post.markdown` and drop it into this directory. Next time Scout is restarted it will treat this file as its own. 

Scout is intended to give you control over what you write without getting in your way about it. I know there are going to be some rough edges, but as we progress I'm sure they'll get worked out. 
