---
layout: post
title: Searching for Non-Printable Characters in Text
date: 2025-08-14 07:10:39
---

One of the systems at work accepts data in csv format, which is essentially plain text with columns separated by commas. Occasionally a client will upload a file with mistakes in it, and while our applications are fairly robust and can handle *most* issues, sometimes one slips by that we weren't expecting. When this happens, as it has twice in the past as many days, I'm called in to find out why. 

The first issue was with a Python application that was pulling a file from S3, parsing it, and turning it into a tab-separated values file before uploading it back to S3 to be further processed by another system. The error given by Python's `csv` package was:

```
_csv.Error: need to escape, but no escapechar set
```

Which was odd because we process many, many files during a day and this same code hasn't needed to set anything else. After a bit of faffing around replicating the error locally, and isolating where in the code the error was occuring, I finally got it in my head to just grep the file for special characters. Sure enough, I found that the file contained tabs inside of the values, which given the logic of our program was causing it to have a bad time of it. 

The command `grep '\t' in.csv` gave me the lines containing the offending tabs, and `grep -n '\t' in.csv | cut -d : -f 1` gave me just the line numbers, which is what I was asked for. The `cut` command lets me select specific parts of a line, in this case I asked for `-d :` which set the colon as the delimiter, and `-f 1` which asked for just the first column. 

This morning I was asked to look at another task that had failed, this time using a custom Go binary that, again, parsed a csv file from S3. Thinking I might get lucky I ran the same search for tabs in the file but came up empty. After some looking around I found a [Stack Overflow](https://stackoverflow.com/questions/59232089/how-to-install-gnu-grep-on-mac-os) question that pointed me in the right direction, but I first had to install the GNU version of `grep`. 

When Mac OS was merged with NeXTSTEP to create Mac OS X, the NeXT OS brought with it pure Unix underpinnings thanks to BSD[^1]. Thanks to that lineage, the Mac contains all the Unix tools we'd expect, but it does not include the *Linux* tools you'd expect. There are sometimes subtle differences between the tools, and I've found that the (ugg…) *GNU/Linux* version of `grep` to be more flexible. Luckily, Homebrew makes it trivially easy to install standard GNU tools, and running `brew install grep` provided me with the `ggrep` binary. 

Equipped with the right tools for the job, I ran this command:

```
LC_ALL=C  ggrep --color='auto' -P -n "[\x80-\xFF]" in.csv
```

I've [written about](https://jonathanbuys.com/Random_Strings_on_the_Command_Line/) setting `LC_ALL=C` before, so I'll skip that here. The rest of the command I'll cover below.

`--color='auto'`, this makes it much easier to spot the matching characters in a long string. 

`-P`, tells grep to use Perl-compatible regular expressions

`-n`, print the line numbers

`"[\x80-\xFF]"`, This searches the text for the extended ASCII characters ranging from hexadecimal code `80`, or €, to code `FF`, the ÿ, or "Latin small letter y with diaeresis", according to the ASCII table hosted at [ascii-code.com](https://www.ascii-code.com). 

Finally, `in.csv` is just the file name. 

After editing the file, re-uploading, and kicking off the job again, it completed successfully. How in the world is it 2025 and we still have text encoding issues? 






[^1]: I thought for years that NeXTSTEP was based on FreeBSD, but [Wikipedia tells me](https://en.wikipedia.org/wiki/NeXTSTEP) that it was actually built initially on the older 4.3BSD-Tahoe. Sometimes I forget how long ago that really was, and how fast Steve Jobs was [pushed out of Apple](https://en.wikipedia.org/wiki/NeXT) after the announcement of the Mac in 1984.
