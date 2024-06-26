--- 
layout: post
title: My Optimized Windows Workflow
tags: [work, productivity]
---

I love Linux, I really do. Compared to the older UNIX systems like AIX, HP-UX, and Solaris (who is trying really hard to catch up) Linux is head and shoulders above the rest. The main reason for this is that a lot of really smart people also love Linux, and try their best to make it the best server on the planet. For the most part, I'd agree that we are succeeding on that front. On the other hand, to date, I simply can't run Linux on my desktop. If there are servers down, or an application fault somewhere, I need to be able to rely on my tools to be there for me. That's why I run XP on my laptop.

Now, just because I'm running XP doesn't mean that it has to suck. I spend most of my time either in the command line or in Firefox. Oh... uhhh... and, most unfortunately, in Lotus Notes (holding back gag reflex). I'm not sure if there has ever been a worse email client created than Lotus Notes, but that's a post for another day. So, to make the most of what I have, there are three tools that I've come to rely on:

1. [PuTTY][1] - Outstanding SSH client. Always there for me, never craps out, and an awesome Alt-Tab to full screen command line goodness.
2. [Launchy][2] - Now on my permanent list of apps I can't live without.
3. [Emerge Desktop][3] - I've got a small screen, and that damn "Start" menu always bothered me. With Emerge, I've replaced the Explorer shell with a very small, very minimal, no task bars or anything else desktop. If I need the Start menu, I just right click on the desktop and there it is.

With PuTTY, I've traded out my SSH keys with my management server, where I run everything else from. I set up a saved session in PuTTY for the management server, and make sure that I can log in without a password. Next, I create a "Launchy Indexed" folder in my home directory on my laptop, and create a shortcut with the following as the "Target:"

    "C:Program FilesPuTTYputty.exe" -load my.management.server

Next, reload the launchy index, and we are in business. Now I'm just a couple of keystrokes away from my management server. Since my management server is secure and on the same network as most of the rest of my servers, I've set up some custom scripts there as well. My most used script is named "go":

    #!/bin/sh
    # go - ssh into the specified server
    #
    # jonbuys@os-zen.com - Wed Jul 25 09:52:09 CDT 2007
    #
    ############################################################
    # Make sure the user actually entered something here
    if [ -z "$1" ]; then
            echo "Usage: go [servername]"
      exit 1
    else
            # Set the variables
            SERVERNAME=`echo $1`
            USERNAME=`whoami`
            # run the command
            ssh $USERNAME@$SERVERNAME
    fi
    ############################################################
    # EOF: go

Very simple, but still, fewer keystrokes than actually typing ssh myusername@whatever.server.com. I've also been known to abbreviate server names as well in /etc/hosts for folks who insist on ridiculous names that make sense only to them. Fewer keystrokes, quick access, and less to think about when I absolutely need to get to that server ASAP. Luckily, there are very few times when the need is that great. It is, however, very satisfying to see the looks on the faces of my old-school co-workers when they realize that "He hasn't touched his mouse yet..."

[1]: http://www.chiark.greenend.org.uk/~sgtatham/putty/
[2]: http://www.launchy.net/
[3]: http://emergedesktop.org/

