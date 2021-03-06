--- 
layout: post
title: Shell Script Style
tags: [linux, work, productivity]
---

My co-worker and I spent the better part of yesterday afternoon going through a former employee's shell scripts to try to determine what they were and what he was trying to do. The script worked, for a while, but there were several mistakes. The mistakes were not in strict syntax, they were in style. Here are a few simple rules to follow to write great scripts:
 
1. Always, always, always start off each and every script with a shbang line: `#!/bin/sh`. Starting off your script with this line tells your shell where to find the interpreter for the commands in the script. Without this line, the script is using your user's existing shell, the one you are typing in at the moment. This is bad because you are sharing environmental variables, and maybe changing environmental variables outside of your script, and not keeping it self contained and portable. 
 
2. Keep your script self contained: If at all possible, try to avoid writing files in different directories. Or, even better, try to avoid writing files at all. Use variables when you can, write files when you have to. 

3. Avoid sourcing other scripts or files containing functions: I read about this method in [Wicked Cool Shell Scripts][1], but I disagree that it is as useful as they say. Writing a custom function to send an email is a great idea. separating it out of the script you are working on at the time is not. Again, keep the script self contained. There are obvious exceptions to this rule. If your function is over 50 lines of code, and reused in multiple other scripts, then by all means, source it. If your function is 10 lines, create a [vi shortcut for it][2] and add it to the top of the script. 

4. Comment tasks: Each block of code in your shell script is meant for a specific task. Add a comment for this block. Make it easy to read, and simple to understand. Assume that you will not work there forever, and someone else will need to read your code and make sense out of it. Also assume that in a year, you will forget everything you did and why you did it and need a reminder.

5. Keep it simple: Scripts should flow logically from top to bottom. If you are creating functions, make it obvious using a comment. Reading a script should be as easy as reading a book, if it's not, then you are intentionally making things overly complicated and difficult to read. 

6. End each script with `#EOF`: This is purely a matter of taste, but I find it adds a nice closure to the script. 

The easiest thing to do is to create another script who's purpose in life is to create new scripts. Couple this script with a vi shortcut (mine is ,t) to create the skeleton of the script and you can quickly create powerful, well formatted, easy to read scripts. Here's an example of mine: 
    
    #!/bin/sh
    # 
    # scripty.sh: This script creates other scripts
    # Created: 25 Feb. 2009 -- inbound@jonathanbuys.com 
    #
    ##############################################################
    
    # A place for variables
    VAR1="Set any variables at the top"
    DATE=`date`
    ANDTHEN="Whatever"
    
    # A place for functions
    some_func(){
        echo `date`
        echo "Whatever's Clever!"
    }
    
    # Get down to writing the script
    
    echo $VAR1
    echo $DATE
    echo $ANDTHEN
    some_func
    # etc...
    
    ##############################################################
    #EOF
    

This article doesn't talk about syntax, only style. There's plenty of help with syntax available on the Intertubes. Also, this is _my_ style, as you progress as a sysadmin or scripter of some sort or another, you are bound to come up with your own style that suits you. My style is based on the documentation at grox.net. My style has evolved over time, as will yours, but this is a good place to start.  

[1]: http://www.intuitive.com/wicked/
[2]: http://grox.net/doc/unix/exrc.php
