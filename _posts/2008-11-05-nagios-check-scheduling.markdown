--- 
layout: post
title: Nagios Check Scheduling
tags: [nagios, sysadmin, linux, work]
---

Or, maybe a better title for this would be "They rebooted the server, why didn't I get a page?"  I've had that question asked of me a few times, and I've never had a good answer, so I thought I'd take a closer look at Nagios and see what is going on. 

Inside of nagios.conf are six values that are important to consider. The first is the Service Inter-Check Delay Method. This is the method that Nagios should use initially. 

> spreading out service checks when it starts monitoring. The default is to use smart delay calculation, which will try to space all service checks out evenly to minimize CPU load. Using the dumb setting will cause all checks to be scheduled at the same time (with no delay between them)! This is not a good thing for production, but is useful when testing the parallelization functionality.  

* n = None - don't use any delay between checks
* d = Use a "dumb" delay of 1 second between checks
* s = Use "smart" inter-check delay calculation
* x.xx = Use an inter-check delay of x.xx seconds

The next setting to look at is the Service Check Interleave Factor. 

> This variable determines how service checks are interleaved. Interleaving the service checks allows for a more even distribution of service checks and reduced load on remote hosts. Setting this value to 1 is equivalent to how versions of Nagios previous to 0.0.5 did service checks. Set this value to s (smart) for automatic calculation of the interleave factor unless you have a specific reason to change it.  
> 
> * s = Use "smart" interleave factor calculation
> * x = Use an interleave factor of x, where x is a number greater than or equal to 1.

I love it when there is good documentation in the config files. So, there are several checks running at once, and they are spaced out how the Nagios application thinks is best, but how many are running at once?  This is determined by the next variable, *Maximum Concurrent Service Checks*. 

> This option allows you to specify the maximum number of service checks that can be run in parallel at any given time. Specifying a value of 1 for this variable essentially prevents any service checks from being parallelized. A value of 0 will not restrict the number of concurrent checks that are being executed.  

Our variable here is set to 0, unrestricted.

The third item that caught my eye is the Service Reaper Frequency variable. 

> This is the frequency (in seconds!) that Nagios will process the results of services that have been checked. 

Our variable here is set to 10, so every 10 seconds Nagios processes the results of the checks.

The last value is actually a group of values collectively known as Timeout Values. 

> These options control how much time Nagios will allow various types of commands to execute before killing them off. Options are available for controlling maximum time allotted for service checks, host checks, event handlers, notifications, the ocsp command, and performance data commands. All values are in seconds. 

Our values are:

* service_check_timeout=60
* host_check_timeout=30
* event_handler_timeout=30
* notification_timeout=30
* ocsp_timeout=5
* perfdata_timeout=5

Knowing the theory is good, but it is also good to know the exact times between checks. In the Nagios web interface there is a page for each service that is monitored with the label "Service State Information". On this page I found the timestamp for the "Last Check Time" and the "Next Scheduled Check". *Looking at several of these I found that each service check is five minutes apart... down to the second.*

One last item to consider is that Nagios gives each check three chances to correct itself. This means that if Nagios finds an error, it immediately schedules the next check of the service. (Ping also being considered a "service") 

So, what all this means is a very long-winded explanation of what I thought was happening. The server was rebooted right after a service check, and it came back up before the next service check was executed. 

