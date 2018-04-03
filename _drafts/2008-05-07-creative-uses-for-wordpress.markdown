---
layout: post
title: Creative Uses for Wordpress
tags: work linux shell 
---

Where I spend my days ($WORK), we have multiple monitoring systems for just about every service on every server that we have.  Many of these are <a href="http://www.nagios.org/">Nagios</a>, some are built in, and others are <a href="https://h10078.www1.hp.com/cda/hpms/display/main/hpms_content.jsp?zn=bto&amp;cp=1-11-15-25%5E849_4000_100__">SiteScope</a>.  All of the systems generate email alerts that either go to our pagers, our email, or both.  From time to time, management would ask a question like "How many pages do you get in a week on average", which up till a couple of months ago, our answer was always "It just depends".

Not a great answer, so I decided to start tracking the email alerts with a centralized database.  Now, at this point, I could have whipped up my own home-brew frankenstein creation, but since everything I wanted was already built into Wordpress, I really didn't need to.  Wordpress has the option of posting blogs via email.  So, all I needed to do was set up a special email account on our mail server and make sure the pop3 server was running.  Then, add the server and login information into Wordpress, setup a cron job to trigger the mail check every five minutes, and there.  Instant logging of all pages that are sent out in a searchable, easy to read, web format.  Now, when management gets it in their mind to start asking questions, we can easily say "Let me reference my report." They really like hearing things like that.

Building on the success of the alert log, I thought it might be good to also log all of our changes to the system.  This idea is completely different from traditional "Change Management" systems which require you to log ahead of time what you want to accomplish in some ridiculous form or application.  Instead, I find it much more useful and relevant to build in the change logging where we spend most of our time, the command line.

I've added an alias for "exit" in the shell like so:
    alias exit="exec /scripts/ch_log"
Here is the ch_log script:

    #!/bin/sh
    # ch_log - Prompt the user to log system changes on
    # exit from the root shell.
    #
    # jonbuys@os-zen.com - Wed Apr  2 15:32:43 CDT 2008
    #
    ############################################################
    
    HOST=`hostname`
    DATE=`date +%m-%d-%y`
    echo $DATE
    echo "Did you make any changes to the system? (y/n)"
    read answer
    
    if [ $answer == n ] ; then
       echo "OK, Thanks!"
       exit 0
    else
       echo "Cool, please enter your name, and then describe the changes in the form."
       echo "Name:"
       read NAME
    
        cat /scripts/log_template | sed s/NNN/$NAME/g | sed s/DDD/$DATE/g | sed s/SSS/$HOST/g > /tmp/$$.answer
        vi /tmp/$$.answer
        mail change_log@mail.mydomain.com -s "Change Notification for $HOST"&lt; /tmp/$$.answer
        echo "OK, thanks!"
    fi
    exit 0
    
    ############################################################
    # EOF: ch_log

Basically, when we exit our shell we now have to make a choice… do we log what we did with this quick and easy script, or do we ignore it and risk the consequences.  I've found that for the most part, I choose to log my work.  The email that is sent off to the change_log@mail.mydomain.com address is picked up by a second Wordpress install, and posted to the blog.  Now we have a historical record of what we've done incase something breaks, or (more importantly) when annual review time comes around and we are asked "what have you been up to"

There is one other change that I had to make to get this to work right.  By default, Wordpress holds all posts it recieves via email for approval before posting it to the main page.  This is good security, but not really needed on an internal LAN, and it breaks the system I've laid out above.  So, to fix it, I've made a slight change to the wp-mail.php file:
     // Set $post_status based on $author_found and on author's publish_posts capability
     if ($author_found) {
             $user = new WP_User($post_author);
             if ($user-&gt;has_cap('publish_posts'))
                     $post_status = 'publish';
             else
                     $post_status = 'publish';
     } else {
             // Author not found in DB, set status to pending.  Author already set to admin.
             $post_status = 'publish';
     }

Above, I've changed the "pending" post_status to "publish" for unidentified users, which is everything that it receives via email.  This is a very bad idea to do outside of the LAN, but I don't see any harm in it internally.  Undoubtedly there are those who would disagree, but this works well for us.

This is how we are using Wordpress internally on our corporate LAN right now, I'd be interested to hear how some others are using Wordpress or other blogging software.
