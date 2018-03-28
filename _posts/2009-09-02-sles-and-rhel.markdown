---
layout: post
title: SLES and RHEL
tags: work linux sysadmin
---

Comparing two server operating systems, like SuSE Linux Enterprise Server (SLES) and RedHat Enterprise Linux (RHEL), needs to answer one question, "what do we want to do with the overall system"? The version of Linux running underneath the application is immaterial, as long as the application supports that version. It is my opinion that we should choose the OS that supports all of our applications, and gives us the best value for our money.

**Price**

RHEL advertises "Unlimited Virtual Machines", but what they put in the small print is that the number of virtual machines you can run is unlimited only if you are using their Xen virtualization. We already have a significant investment in both money and knowledge in VMWare, so the RHEL license doesn't apply, and we have to purchase a new license for each virtual machine. There is an option to purchase a RHEL for VMWare license, but it is expensive, and still limits you to a maximum of 10 virtual machines per-server.

SLES allows unlimited virtual machines regardless of the virtualization technology used. SLES also has a special license for an entire blade center, which (and I'd have to double check on this fact) may let us license the blade center, and purchase additional blades without having to license those blades separately. This license would allow us to run unlimited virtual machines and add physical capacity to the blade center as needed. This is the license we have for one of our blade centers, and I believe it cost $4500 for a three year contract. As I understand it, that means that for the 9 blades we have in it now, we spent $500 each for a three year license, which equates to $167 per blade per year. We also have the ability to add an additional five blades to this blade center, which would also be covered under the agreement. Doing so would bring our total per blade per year cost down to $108, for unlimited virtual machines.

For a comparison, right now, if we want to bring up a new RHEL server in our environment, we have to purchase another minimal RHEL license for $350, more if we actually want support and not just patches.

Even without the special blade center pricing (which may be IBM only), a single license for SLES priced by CDW costs $910 for three years. So, for $304 per blade per year, we can license two blade centers for $6,080 annually, which will cover all virtual machines. That price is off-the-shelf, so I'm sure our vendors could lower the price even more. In another pre-production environment, which resides on three physical servers running VMWare, there are 40 virtual machines, which, if we migrate them to REHL, would cost $14,000 annually.

Related to base price is what is included with the base price. SLES gives you the option to create a local patching mirror and synchronize regularly with their servers. This same functionality is available for RHEL as the "[RHN Satellite Server](https://www.redhat.com/products/enterprise-linux/rhn-satellite/)" at a cost of $13,500, annually.

**Performance**

As far as I can tell, neither RHEL or SLES have a significant performance advantage. However, SLES has the option to do a very bare-bones, minimal install with no reliance on a graphical user interface. RHEL requires either a remote or local X windows session running to access its management tools. There are versions of the management tools in the command line, but they are either marked as depreciated, or do not offer all of the options of the GUI. 

One of our environments is run on SLES 9, and another ran on SLES 8 for several years and all systems have had excellent performance. 

**Elsewheres**

RHEL has no YaST equivalent, and the individual command line configuration tools do not have all of the options of their GUI counterparts. To effectively manage RHEL, we either have to keep an X server running locally and tunnel X, or use the old school Unix tools, and edit text files. Also, RedHat keeps its text files in several different places, and it has taken us a lot of trial and error to find out which one is right. Admittedly, that's more of an annoyance than anything, but it still takes time.

RHEL has major problems with LDAP. We had an outage on a database server that was a result of an improper LDAP configuration, the same LDAP config we have on all of the other servers. RHEL was attempting to authenticate a local daemon that inspects hardware against LDAP, before the NIC card was even discovered, much less started. I can think of no good reason that would ever be an option. 

I'm not sure how RedHat is competing these days.  Cent OS and Scientific Linux distribute the source of RHEL for free, Oracle has a lower price option, and Novell's SLES kills RedHat in pricing.  It almost seems to me that RedHat is living on it's name alone.

