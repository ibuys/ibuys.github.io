--- 
layout: post
title: New SysAdmin Tips
tags: [work, sysadmin, culture]
---

My answer to a [great question](http://serverfault.com/questions/75476/toolkit-habits-for-linux-network-system-administration) over at serverfault.

First off, find your logs. Most Linux distros log to /var/log/messages, although I've seen a couple log to /var/log/syslog. If something is wrong, most likely there will be some relevant information in the logs. Also, if you are dealing with email at all, don't forget /var/log/mail. Double-check your applications, find out if any of them log somewhere ridiculous, outside of syslog.

Brush up on your vi skills. Nano might be what all the cool kids are using these days, but experience has taught me that vi is the only text editor that is guaranteed to be on the system. Once you get used to the keyboard shortcuts, and start creating your own triggers, vi will be like second nature to you.

Read the man page, and then run the following commands on each machine, and copy the results into your documentation:

{% highlight bash %}

    cat /etc/*release*
    cat /etc/hosts
    cat /etc/resolv.conf
    cat /etc/nsswitch
    df -h
    ifconfig -a
    free -m
    crontab -l
    ls /etc/cron.d
    echo $SHELL
{% endhighlight %}

That will serve as the beginnings of your documentation. Those commands let you know your environment, and can help narrow down problems later on.

Grep through your logs and search for "error" or "failed". That will give you an idea of what's not working as it should. Your users will give you their opinion on whats wrong, listen closely to what they have to say. They don't understand the system, but they see it in a different way than you do.

When you have a problem, check things in this order:

1.  Disk Space (df -h): Linux, and some apps that run on Linux, do some very strange things when disk space runs out. It may seem unrelated, until you check and find a filesystem 100% full.

2.  Top: Top will let you know if you've got some process that's stuck out there eating up all of your available CPU cycles. Nothing should consume 99% CPU for any extended period of time. If its a legitimate process, it should probably fluctuate up and down. While you are in top, check...

3.  System Load: The system load should normally be below 3 on a standard server or workstation. The system load is based on CPU, memory, and I/O.

4.  Memory (free -m): RAM use in Linux is a little different. It's not uncommon to see a server with nearly all of its RAM used up. Don't Panic, if you see this, it's mostly just cache, and will be cleared out as needed. However, pay close attention to the amount of swap in use. If possible, keep this as close to zero as you can. Insufficient memory can lead to all kinds of performance problems.

5.  Logs: Go back to your logs, run tail -500 /var/log/messages | more and start reading through and seeing what's been going on. Hopefully, the logs will be able to point you in the direction you need to go next.

A well maintained Linux server can run for years without problems. We just shut one down that had been running for 748 days, and we only shut it down because we had migrated the application over to new hardware. Hopefully, this will help you get your feet wet, and get you off to a good start.

One last thing, always make a copy of a config file you intend to change, and always copy the line you are changing, and comment out the original, adding your reason for changing it. This will get you into the habit of documenting as you go, and may save your hide 9 months down the road.