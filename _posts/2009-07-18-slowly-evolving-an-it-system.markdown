--- 
layout: post
title: Slowly Evolving an IT System
tags: work sysadmin
---

We are going through a major migration at work, upgrading our four and a half year old IBM blades to brand spanking new HP BL460 G6's.  We run a web infrastructure, and the current plan is to put our F5's, application servers, and databases in place, test them all out, and then take a downtime to swing IPs over and bring up the new system.  It's a great plan, it's going to work perfectly, and we will have the least amount of downtime with this plan.  Also... I hate it.

The reason I hate it has more to do with technical philosophy then with actual hard facts.  I prefer a slow and steady evolution, a recognition that we are not putting in a static system, but a living organism who's parts are made up of bits and silicone.  What I'd like to do is put in the database servers first, then swing over the application servers, and then the F5, which is going to replace our external web servers and load balancers.  One part at a time, and if we really did it right, we could do each part with very little downtime at all.  However, I can see the point in putting in everything at once, you test the entire system from top to bottom, make sure it works, and when everyone is absolutely certain that all the parts work together, flip the switch and go live.  But... then what.

What about six months down the road when we are ready to add capacity to the system, what about adding another database server, what about adding additional application servers to spread out the load, what about patches?

Operating systems are not something that you put into place and never touch again.  IT systems made up of multiple servers should not be viewed as fragile, breakable things that should not be touched.  We can't set this system up and expect it to be the same three years from now when the lease on the hardware is up.  God willing, it's going to grow, flourish, change.  

Our problems are less about technology, and more about our corporate culture.  
