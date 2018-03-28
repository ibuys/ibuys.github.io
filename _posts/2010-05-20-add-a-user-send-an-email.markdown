---
layout: post
title: Add a User - Send an Email
tags: sysadmin work badsoftware
---
I was asked on Twitter the other day why I <a href="http://twitter.com/ibuys/status/14230359975">disliked</a> IBM's enterprise software.  This, in addition to my <a href="http://jonathanbuys.net/2009/01/22/the-sorry-state-of-enterprise-software/">previous</a> TWS rant, is my answer to that question.

We wanted to do two simple tasks.  Add a new user to the system, and have the system send emails automatically when there's a problem.  Seems easy enough, unless you are using the Tivoli Workload Scheduler.  Then it's an entirely different matter.  

*Add A User*

Some new websites like Postulous create a new user for you when you send them an email.  Others like Tumblr need only three the username and password to get them setup.  To add a user to TWS, you would think that there would be a nice GUI with a menu option that says "Add User", but none exist.  Instead, you have to log into the command line on the server, run the command "dumpsec", and redirect it's output to a file.  Then, you have to vi that file, and edit the XML to add the username to the correct group.  Save that file, and run "makesec filename" to load the new user into the system.  

Then, restart the TWS application server.  IBM is not sure if this is  a required step or not, or a least the help I had on the phone wasn't sure.  

Then, you need to go into the web interface for TWS, and add the user into WebSphere as well.  

It's like the creators of TWS got together for a brainstorming session one day and asked "What is the most difficult, unintuitive way we can add a user to the system?"  Congratulations, folks... I think you nailed it.

*Send An Email*

The heart of TWS is scheduling jobs, and then acting on the results of those jobs.  One task we wanted from it was to let us know if it couldn't run a job by sending us an email.  For two years we worked with consultants and IBM to get this to work.  We wound up having to get some of the original developers on the phone from Rome, and with their help we finally found the problem.

TWS stores <strong>some</strong> of it's settings in  a DB2 database.  That right there is enough for me to toss the entire application in the trash.  In Unix, configuration settings are stored in a plain text file, one file per application if possible.  And if that wasn't bad enough, we found that one of the binaries was modifying the configuration settings in the DB2 database when it was launched, changing the port that a certain daemon was supposed to be listening on.  This daemon was responsible for listening for incoming configurations from the main server, including the configuration telling it to send the email.  It's hard for me to express how wrong this is, but I'll try.

Any daemon should read its configuration from a file under the /etc directory.  That's how it works in Unix, and for the past thirty years its worked out pretty great.  No daemon should have access to modify the configuration of any other daemon.  Also, if listening on a certain port is central to the communications and functioning of the application, don't make that configurable, just hard code the daemon to listen on that port.  I suppose it would also be acceptable to allow configuration that would override the default, but only if the daemon reads its configuration from a plain text file and only if in the absence of the overriding configuration the default port is chosen to listen on.  

Again, $30,000 and the application is held together with duct tape and silly putty.  
