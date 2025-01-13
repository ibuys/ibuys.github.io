---
layout: post
title: Inner-Document Markdown Reference Links
date: 2021-07-09 16:29:59
tags: bbedit markdown
---

I'm writing a fairly large document for internal use at work, and instead of using something like Word I've generated a bunch of markdown files that I'm stringing together with the excellent [Pandoc](https://pandoc.org) to generate a very nice PDF file with LaTeX. The resulting PDF is beautifully formatted, thanks to the [Eisvogel template](https://github.com/Wandmalfarbe/pandoc-latex-template). A key part of the PDF is a functional table of contents outline in the sidebar of Preview, and the ability to link to different parts of the PDF from arbitrary text. 

Pandoc generates header identifiers for each section of the document automatically, which you can use as normal markdown-formatted links. The documentation states:

> A header without an explicitly specified identifier will be automatically assigned a unique identifier based on the header text. To derive the identifier from the header text,

> * Remove all formatting, links, etc.
> * Remove all footnotes.
> * Remove all punctuation, except underscores, hyphens, and periods.
> * Replace all spaces and newlines with hyphens.
> * Convert all alphabetic characters to lowercase.
> * Remove everything up to the first letter (identifiers may not begin with a number or punctuation mark).
> If nothing is left after this, use the identifier section.

So, the header `Header identifiers in HTML` becomes `#header-identifiers-in-html`. I did this manually exactly once before I was certain that it was going to be far too tedius and something that could be easily solved by `awk`, or so I thought.

It turns out that the BSD version of `awk` included with macOS doesn't support the flag needed to convert to lowercase, so instead I grabbed a quick perl command and sandwiched it between two `awk` commands:

```
sed s/\ /-/g | perl -p -e 'tr/A-Z/a-z/' | sed s/^/\#/g
```

Then all I needed to do was drop that in a file with a shebang header and mark it executable, move the file into BBEdit's "Text Filters" folder and it was made available to BBEdit from the Text menu. Now I just highlight some text I want to format as a link, and select the menu option. 

I suppose I could get even fancier and muck with the clipboard, and work all the other Pandoc rules into the script, but I imagine this will take care of %95 of my use cases for what I'm doing. That's more than enough. 