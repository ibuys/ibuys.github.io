--- 
layout: post 
title: Writing about Jekyll 
tags: blogging online 
--- 

I'm writing an article for [TAB][1] about my new blogging engine, [Jekyll][2]. I've taken most of the reliance on the command line out of dealing with Jekyll on a day to day basis, and instead have a few Automator workflows in the scripts menu in the Mac menubar. It's a great setup, I'm really enjoying it. I'm sure there will be quite a bit of enhancement yet to come, but my initial workflow looks like this:

  1. Click "New Blog Post"
  2. Write the article
  3. Click "Run Jekyll"
  4. Make sure everything worked using the local [webrick][3] web server.
  5. Click "Kill Jekyll"
  6. Click "Sync Site"

Here's what I've got so far in the automator workflows:

### New Blog Post

First, I run the "Ask for Text" action to get the name of the post. Then, I run this script:

    
    NAME=`echo $1 | sed s/\ /-/g`
    USERNAME=`whoami`
    POSTNAME=`date "+%Y-%m-%d"-$NAME`
    POST_FQN=/Users/$USERNAME/Sites/_posts/$POSTNAME.markdown
    touch $POST_FQN
    echo "---" >> $POST_FQN
    echo "layout: post" >> $POST_FQN
    echo "title: $1" >> $POST_FQN
    echo "---" >> $POST_FQN
    /usr/bin/mate $POST_FQN
    

### Run Jekyll

First, I run this script:

    
    USERNAME=`whoami`
    cd /Users/$USERNAME/Sites
    /usr/bin/jekyll > /dev/null
    /usr/bin/jekyll --server  > /dev/null 2>&1 &
    /usr/local/bin/growlnotify --appIcon Automator Jekyll is Done -m 'And there was much rejoicing.'
    echo "http://localhost:4000"
    

Followed by the "New Safari Document" Automator action. This runs Jekyll which converts the blog post I just wrote in [markdown][4] syntax to html, updates the site navigation, starts the local web server and opens the site in Safari to preview.
  
### Kill Jekyll

Since I start the local server in the last step, I need to kill it in this step. This action does just that.

    
    PID=`ps -eaf | grep "jekyll --server" | grep -v grep | awk '{ print $2 }'`
    kill $PID
    /usr/local/bin/growlnotify --appIcon Automator Jekyll is Dead -m 'Long Live Jekyll.'
    

This is entered in as a shell script action, and is the only action in this workflow.
  
### Sync Site

Once I'm certain everything looks good, I run the final Automator action to upload the site: 
    
    cd /Users/USERNAME/Sites/_site/
    rsync -avz -e ssh . USERNAME@jonathanbuys.com:/home/USERNAME/jonathanbuys.com/ > /dev/null
    /usr/local/bin/growlnotify --appIcon Automator Site Sync Complete -m 'Check it out.'
    

This is also a single Automator action workflow. You'll notice that I use [Growl][5] to notify me that the script is finished. This is also not really necessary, but it's fun anyway.
  
Like I said, there's a lot of improvement yet to go, but I think it's a solid start. I'm at a point now where I'm tempted to start writing a Wordpress import feature, which seems to be the only major piece missing from the Jekyll puzzle. I'm not sure what this would take just yet, but I've got a few ideas.  I haven't tried uploading any images or media yet, but since everything is static, I assume it would just be a matter of placing the image in a /images folder and embedding it in html. So far, I'm having a lot of fun, and that's what blogging is really all about.  

[1]: http://theappleblog.com
[2]: http://jekyllrb.com/
[3]: http://www.webrick.org/
[4]: http://daringfireball.net/projects/markdown/
[5]: http://growl.info/
