--- 
layout: post
title: Ping from Cocoa
tags: [cocoa, programming] 
---

One of the features of Servers.app is that it pings the host and shows a little indicator for it's status: green is good, red is dead.  Getting that little feature in here was not quite as easy as I thought it would be.  After searching the Apple documentation for what seemed like years, I stumbled across SimplePing.  It was perfect, exactly what I was looking for.  I dropped the two source code files into into my project, read through the documentation commented out in the header file and added the code to call SimplePing.  It worked, and everything seemed fine.  Except that it kept working, even when I knew for certain that the host did not exist.  

So, I started digging through the source code for SimplePing.c, and found that instead of calling a standard error message, it called [perror][1], which, according to the documentation, doesn't return a value.  This is fine if you want to log the ping results, but I wanted to ping the server and make a decision based on code.  So, I changed a couple of lines of code from this:

    if (error == 0) //was able to wait for reply successfully (whether we got a reply or not)
    {
        if (gotResponse == 1)
	    {
			{numberPacketsReceived = numberPacketsReceived + 1;}
		}
	}
	
to this:

    if (error == 0) //was able to wait for reply successfully (whether we got a reply or not)
    {
        if (gotResponse == 1)
		{
			{numberPacketsReceived = numberPacketsReceived + 1;}
		} else {
			error = 1;
		}
	}


Simply adding an extra else statement in there to return an error code gave my application something to work with.  Now, from my application controller I can call SimplePing like this:

    int systemUp;
    systemUp = SimplePing(cString, 2, 2, 1);

After that, I can make decisions based on the value of the systemUp int.   Now, it's entirely possible that I'm doing this wrong, all I can say is that it works for me now, and it didn't before.  

[1]: http://www.opengroup.org/onlinepubs/000095399/functions/perror.html
