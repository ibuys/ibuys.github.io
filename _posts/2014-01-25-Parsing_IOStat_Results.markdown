---
layout: post
title: Parsing iostat Results
date: 2014-01-25 19:54:56
tags: [linux, sysadmin, statistics]
---

In the course of load testing a new system, we gathered the output from [iostat][1] from a group of servers. In addition to parsing through the device statistics, we thought it would be handy to graph the CPU stats as well. We set iostat to run every five seconds and captured the output in a text file, one per server. This gave me a sizable pool of data, but with everything I needed on separate lines. 

{% highlight bash %}

Time: 18:00:01
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.79    0.03    0.48    0.06    0.00   98.64

Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
sda               2.22         0.20        38.52    1948442  373500872
sda1              0.00         0.00         0.00      16224       1848
sda2              2.22         0.20        38.52    1931938  373499024
{% endhighlight %}


I gathered all the text files into a single directory, and ran a loop in zsh to create a csv file, ready for easy manipulation in any number of programs.
{% highlight bash %}
for each in `ls`
egrep -A 1 '(Time)|(avg-cpu)' $each |sed s/Time\:\ //g | grep -v '\-\-\|avg-cpu' | paste -s -d '\ \n' - - | sed 's/\( \)\{1,\}/,/g' > $each.csv
{% endhighlight %}

I always start building long lines like this one section at a time. Each section is separated by a pipe, (`|`), so the first section in the loop calls egrep.

{% highlight bash %}
egrep -A 1 '(Time)|(avg-cpu)' $each
{% endhighlight %}


This command alone give us output that looks like this:

{% highlight bash %}
Time: 00:03:39
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.20    0.00    0.10    0.00    0.00   99.70
--
Time: 00:03:44
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.10    0.00    0.20    0.00    0.00   99.70
{% endhighlight %}


The "-A" flag on the egrep command tells egrep to get both the matching line in the text and the line directly below it. The section between the single tics, searches for either "Time" or "avg-cpu". This gives me the time and the CPU statistics I'm interested in. Next, I pipe this output to the next section, a [sed][2] command that strips out the "Time" string, so our command now looks like:

{% highlight bash %}

egrep -A 1 '(Time)|(avg-cpu)' iostat.ba-rec1  |sed s/Time\:\ //g 
{% endhighlight %}

And gives us output like:

{% highlight bash %}

00:04:14
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.00    0.00    0.10    0.00    0.00   99.90
--
00:04:19
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.40    0.00    0.30    0.00    0.00   99.30
{% endhighlight %}


The next section uses grep with the "-v" flag, which tells grep to reverse it's normal behavior and only return the strings that do *not* match the search text. 
{% highlight bash %}
egrep -A 1 '(Time)|(avg-cpu)' iostat.ba-rec1  |sed s/Time\:\ //g | grep -v '\-\-\|avg-cpu'
{% endhighlight %}

The grep command is looking for either "avg-cpu" or two dashes and removing both lines, giving us:
{% highlight bash %}

00:04:14
           0.00    0.00    0.10    0.00    0.00   99.90
00:04:19
           0.40    0.00    0.30    0.00    0.00   99.30
{% endhighlight %}

This is looking much better, but the lines of text are offset from what I need them to be. A post I read recently by [Dr. Drang][3] reminded me of [paste][4], which is perfect for this job:

{% highlight bash %}
egrep -A 1 '(Time)|(avg-cpu)' iostat.ba-rec1  |sed s/Time\:\ //g | grep -v '\-\-\|avg-cpu' | paste -s -d '\ \n' - - 
{% endhighlight %}

Which puts everything on the same line, nice and clean:

{% highlight bash %}
00:04:14            0.00    0.00    0.10    0.00    0.00   99.90
00:04:19            0.40    0.00    0.30    0.00    0.00   99.30
{% endhighlight %}

Only thing left now is to clean up the excess spaces a bit and separate each column by commas, another job for sed, which is only slightly modified from this post on [StackOverflow][5], which leads us to the final command:

{% highlight bash %}
egrep -A 1 '(Time)|(avg-cpu)' iostat.ba-rec1  |sed s/Time\:\ //g | grep -v '\-\-\|avg-cpu' | paste -s -d '\ \n' - - | sed 's/\( \)\{1,\}/,/g'
{% endhighlight %}

Which I redirect the output of to a text file, one per server, just like the input from the loop. This, finally, gives us the csv output we were looking for:

{% highlight bash %}
00:04:14,0.00,0.00,0.10,0.00,0.00,99.90
00:04:19,0.40,0.00,0.30,0.00,0.00,99.30
{% endhighlight %}

Now it is ready.


[1]: http://man.cx/iostat
[2]: http://man.cx/sed
[3]: http://www.leancrew.com/all-this/2013/11/two-simple-things/
[4]: http://man.cx/paste
[5]: http://stackoverflow.com/questions/9953448/how-to-remove-all-white-spaces-from-a-given-text-file
