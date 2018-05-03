#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import io
import glob
import re
import datetime
import shutil
import pytz
from subprocess import Popen, PIPE, STDOUT
from xml.sax.saxutils import escape

# This script should only do one damn thing: build my site. That's it.
# Strip the YAML junk out, get the date from the filename, and
# assemble the pieces. I'll use the layout of Jekyll for a template,
# and put the pieces together with this script.

baseURL = "http://jonathanbuys.com/"
workDir = os.environ['HOME'] + "/Public/Site/"
layoutDir = workDir + "_layouts"
postsDir = workDir + "_posts"
essaysDir = workDir + "essays"
siteDir = workDir + "_site"

mediaDir = workDir + "media"
destMediaDir = siteDir + "/media"
imagesGlobalDir = workDir + "images-global"
destImagesGlobalDir = siteDir + "/images-global"
jsDir = workDir + "js"
destJsDir = siteDir + "/js"
cssDir = workDir + "stylesheets"
destCssDir = siteDir + "/stylesheets"
destEssaysDir = siteDir + "/essays"

postTemplate = open(layoutDir + "/post.html").read()
defaultTemplate = open(layoutDir + "/default.html").read()

# print defaultTemplate
# print postTemplate

# Define a copy directory method
# from: http://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if not os.path.exists(d):
                shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


# load all posts into an array
allPosts = []
allPosts = glob.glob(postsDir + "/*.markdown")

structuredPostsList = []

for pos, item in enumerate(allPosts):
    # iterate through the array
    # for each post, grab the date from the file name
    postName = os.path.basename(item)
    #print postName
    match = re.match(r'(\d{4}-\d{1,2}-\d{2})',postName)
    #print match.group(1)
    date = datetime.datetime.strptime(match.group(1),"%Y-%m-%d")
    #print date.year
    contents = open(item).read()

    # grab the title from the yaml
    #titleMatch = re.escape(re.search(r'(title:[\s\w,|.|\'\/-]+\n)', contents))
    #print titleMatch;
    myLines = []
    for line in contents.splitlines():
        if line.startswith("title:"):
            myLines.append(line)

    postTitle = myLines[0].replace("title: ", "")
    postDateString = "<p class=\"smalldate\">Posted on " + date.strftime("%B %d, %Y") + "</p>"
    
    #postTitle = titleMatch.group(1).replace("title: ", "").replace("---","").rstrip()

    # remove yaml front matter
    # head, sep1, postText = contents.rpartition("---")
    postText = contents

    # convert to HTML
    p = Popen(['mmd', '-s'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    #print(postText)
    mmd_stdout = p.communicate(input=postText + '\n')[0]
    #print(mmd_stdout)
    mmd_stdout = mmd_stdout.replace("fn:",match.group(1) + "-fn:").replace("fnref:", match.group(1) + "-fnref:")
    datePlusMmd = mmd_stdout + postDateString 

    # wrap html in templates
    postHTML = postTemplate.replace("{{content}}",datePlusMmd)
    fullHTMLTitles = defaultTemplate.replace("{{ page.title }}", postTitle)
    fullHTML = fullHTMLTitles.replace("{{ content }}", postHTML)
    #print fullHTML

    # make directory from date
    #postPublisDir =
    postDate = date.strftime("%m-%d-%Y")
    directory = siteDir + "/" + postDate
    if not os.path.exists(directory):
        os.makedirs(directory)

    # write html file to the directory named with title and underscores
    postFileName = postName.replace(match.group(1) + "-","").replace(".markdown",".html")
    # print postFileName
    fullPostFilePath = directory + "/" + postFileName
    URL = baseURL + postDate + "/" + postFileName

    # build dictionary and add to list for later
    postDict = {'title': postTitle, 'date': date, 'text': mmd_stdout, "url": URL}
    structuredPostsList.append(postDict)

    # print fullPostFilePath
    with open(fullPostFilePath, 'w') as f:
        f.write(fullHTML)


# end iteration

# copy media
if not os.path.exists(destMediaDir):
    os.makedirs(destMediaDir)
copytree(mediaDir, destMediaDir)

# copy images
if not os.path.exists(destImagesGlobalDir):
    os.makedirs(destImagesGlobalDir)
copytree(imagesGlobalDir, destImagesGlobalDir)


# copy javascript
if not os.path.exists(destJsDir):
    os.makedirs(destJsDir)
copytree(jsDir, destJsDir)

# copy css
if not os.path.exists(destCssDir):
    os.makedirs(destCssDir)
copytree(cssDir, destCssDir)

# copy (and process) essays
if not os.path.exists(destEssaysDir):
    os.makedirs(destEssaysDir)

allEssays = []
allEssays = glob.glob(essaysDir + "/*.markdown")
for pos, item in enumerate(allEssays):
    contents = open(item).read()
    postName = os.path.basename(item)
    # print postName

    # grab the title from the yaml
    titleMatch = re.search(r'(title:[\s\w,|.|\'\/-]+\n)', contents)
    postTitle = titleMatch.group(1).replace("title: ", "").replace("---","").rstrip()

    # remove yaml front matter
    head, sep1, postText = contents.rpartition("---")

    # convert to HTML
    p = Popen(['mmd'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    mmd_stdout = p.communicate(input=postText + '\n')[0]
    # print(mmd_stdout)

    # wrap html in templates
    postHTML = postTemplate.replace("{{content}}",mmd_stdout)
    fullHTMLTitles = defaultTemplate.replace("{{ page.title }}", postTitle)
    fullHTML = fullHTMLTitles.replace("{{ content }}", postHTML)
    # print fullHTML

    # write html file to the directory named with title and underscores

    fullPostFilePath = destEssaysDir + "/" + postName.replace(".markdown",".html")

    # print fullPostFilePath
    with open(fullPostFilePath, 'w') as f:
        f.write(fullHTML)

# build 100books
item = workDir + "100books.markdown"
contents = open(item).read()
postName = os.path.basename(item)

# print postName
# grab the title from the yaml
titleMatch = re.search(r'(title:[\s\w,|.|\'\/-]+\n)', contents)
postTitle = titleMatch.group(1).replace("title: ", "").replace("---","").rstrip()

# remove yaml front matter
head, sep1, postText = contents.rpartition("---")
# convert to HTML
p = Popen(['mmd'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

mmd_stdout = p.communicate(input=postText + '\n')[0]
# print(mmd_stdout)

# wrap html in templates
postHTML = postTemplate.replace("{{content}}",mmd_stdout)
fullHTMLTitles = defaultTemplate.replace("{{ page.title }}", postTitle)
fullHTML = fullHTMLTitles.replace("{{ content }}", postHTML)

# print fullHTML
# write html file to the directory named with title and underscores
fullPostFilePath = siteDir + "/" + postName.replace(".markdown",".html")

# print fullPostFilePath
with open(fullPostFilePath, 'w') as f:
    f.write(fullHTML)


# build 404
item = workDir + "404.markdown"
contents = open(item).read()
postName = os.path.basename(item)

# print postName
# grab the title from the yaml
titleMatch = re.search(r'(title:[\s\w,|.|\'\/-]+\n)', contents)
postTitle = titleMatch.group(1).replace("title: ", "").replace("---","").rstrip()

# remove yaml front matter
head, sep1, postText = contents.rpartition("---")
# convert to HTML
p = Popen(['mmd'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

mmd_stdout = p.communicate(input=postText + '\n')[0]
# print(mmd_stdout)

# wrap html in templates
postHTML = postTemplate.replace("{{content}}",mmd_stdout)
fullHTMLTitles = defaultTemplate.replace("{{ page.title }}", postTitle)
fullHTML = fullHTMLTitles.replace("{{ content }}", postHTML)

# print fullHTML
# write html file to the directory named with title and underscores
fullPostFilePath = siteDir + "/" + postName.replace(".markdown",".html")

# print fullPostFilePath
with open(fullPostFilePath, 'w') as f:
    f.write(fullHTML)


# build contact page

item = workDir + "contact.html"
contents = open(item).read()
postName = os.path.basename(item)

# print postName
# grab the title from the yaml
postTitle = "Contact"


# wrap html in templates
postHTML = postTemplate.replace("{{content}}",contents)
fullHTMLTitles = defaultTemplate.replace("{{ page.title }}", postTitle)
fullHTML = fullHTMLTitles.replace("{{ content }}", postHTML)

# print fullHTML
# write html file to the directory named with title and underscores
fullPostFilePath = siteDir + "/" + postName

# print fullPostFilePath
with open(fullPostFilePath, 'w') as f:
    f.write(fullHTML)




# build best page

item = workDir + "best.html"
contents = open(item).read()
postName = os.path.basename(item)

# print postName
# grab the title from the yaml
postTitle = "best"


# wrap html in templates
postHTML = postTemplate.replace("{{content}}",contents)
fullHTMLTitles = defaultTemplate.replace("{{ page.title }}", postTitle)
fullHTML = fullHTMLTitles.replace("{{ content }}", postHTML)

# print fullHTML
# write html file to the directory named with title and underscores
fullPostFilePath = siteDir + "/" + postName

# print fullPostFilePath
with open(fullPostFilePath, 'w') as f:
    f.write(fullHTML)











# build about page

item = workDir + "colophon.markdown"
contents = open(item).read()
postName = os.path.basename(item)

titleMatch = re.search(r'(title:[\s\w,|.|\'\/-]+\n)', contents)
postTitle = titleMatch.group(1).replace("title: ", "").replace("---","").rstrip()

# remove yaml front matter
head, sep1, postText = contents.rpartition("---")
# convert to HTML
p = Popen(['mmd'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

mmd_stdout = p.communicate(input=postText + '\n')[0]
# print(mmd_stdout)

# wrap html in templates
postHTML = postTemplate.replace("{{content}}",mmd_stdout)
fullHTMLTitles = defaultTemplate.replace("{{ page.title }}", postTitle)
fullHTML = fullHTMLTitles.replace("{{ content }}", postHTML)

# print fullHTML
# write html file to the directory named with title and underscores
fullPostFilePath = siteDir + "/" + postName.replace("markdown","html")

# print fullPostFilePath
with open(fullPostFilePath, 'w') as f:
    f.write(fullHTML)


# build index.html

indexPosts = sorted(structuredPostsList, key=lambda k: k['date'])[-10:]

# print indexPosts

indexStrings = "<div id=\"posts\">"
x = 9
while x > 0:
    postDict = indexPosts[x]
    indexStrings = indexStrings + "<h3><a href=\"" + postDict['url'] + "\">" + postDict['title'] + "</a></h3>"
    indexStrings = indexStrings + "<article><p class=\"thin_line\"></p><p class=\"smalldate\">Posted on " + postDict['date'].strftime("%B %d, %Y") + "</p>"
    indexStrings = indexStrings + postDict['text'] + "</article>"
    x = x - 1

indexStrings = indexStrings + "</div>"
# print indexStrings

# wrap html in templates
postHTML = postTemplate.replace("{{content}}",indexStrings)
fullHTMLTitles = defaultTemplate.replace("{{ page.title }}", "").replace("<p class=\"thin_line\"></p>","")
fullHTML = fullHTMLTitles.replace("{{ content }}", postHTML)

# print fullHTML
fullPostFilePath = siteDir + "/" + "index.html"

# print fullPostFilePath
with open(fullPostFilePath, 'w') as f:
    f.write(fullHTML)

# build atom.xml

item = workDir + "atom.xml"
contents = open(item).read()

atomStrings = "\n"
x = 9
while x > 0:
    postDict = indexPosts[x]
    print postDict['title']
    xmlTitle = escape( postDict['title'])
    xmlText = escape(postDict['text'])
    xmlLink = postDict['url']
    xmlDate = postDict['date'].isoformat('T') + "Z"

    atomStrings = atomStrings + "<entry>"
    atomStrings = atomStrings + "<title>" + xmlTitle + "</title>"
    atomStrings = atomStrings + "<link href=\"" + xmlLink + "\"/>"
    atomStrings = atomStrings + "<updated>" + xmlDate + "</updated>"
    atomStrings = atomStrings + "<id>" + xmlLink + "</id>"
    atomStrings = atomStrings + "<content type=\"html\">" + xmlText + "</content>"
    atomStrings = atomStrings + "</entry>"

    x = x -1

atomXML = contents.replace("{{ site.time }}",datetime.datetime.utcnow().isoformat('T') + "Z")
atomXML = atomXML.replace("{% content %}", atomStrings)

# print atomXML
fullPostFilePath = siteDir + "/" + "atom.xml"

# print fullPostFilePath
with open(fullPostFilePath, 'w') as f:
    f.write(atomXML)



# build archive

sortedList = sorted(structuredPostsList, key=lambda k: k['date'])
# sortedList = sorted(structuredPostsList, key=lambda k: k['date'], reverse=True)
# print sortedList

archiveString = "<ul class=\"postList archive\">\n"
x = len(sortedList) - 1

while x > 0:
    postDict = sortedList[x]
    archiveString = archiveString + "<li><a href=\"" + postDict['url'] + "\">" + postDict['title'] + "</a></li> \n"

    x = x - 1

archiveString = archiveString + "</ul>"

# print archiveString


item = workDir + "toc.html"
contents = open(item).read()
archiveHTML = contents.replace("{% content %}", archiveString)
fullArchiveHTML = defaultTemplate.replace("{{ content }}", archiveHTML)
fullArchiveHTML = fullArchiveHTML.replace("{{ page.title }}", "Table of Contents")

# print archiveXML
fullPostFilePath = siteDir + "/" + "toc.html"

# print fullPostFilePath
with open(fullPostFilePath, 'w') as f:
    f.write(fullArchiveHTML)



#TODO:
# Add a check for flags:
# build, just build
# serve, start the built in python web server after building
# deploy, build, then ssh to NFSN

print "Site build complete."
