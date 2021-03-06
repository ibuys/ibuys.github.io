---
layout: post
title: Recovering Data From FileVault Full Disk Encryption 
tags: [mac, filevault]
date: 2011-10-14 10:49:11
---

>*Disclaimer*: If you do not have your recovery key, or if you have lost your passphrase, this post will not help you. Sorry.

So, just for kicks, say you did not backup your Mac for a couple of weeks. Further, let's say that, being shrewd about security, you turned on full disk encryption on your Mac. This was me, Wednesday, deciding to upgrade to OS X 10.7.2, knowing full well that I had skipped the last weekends scheduled [SuperDuper!][1] backup. Foolish and foolhearty, I know. I found out exactly how foolish it was when my precious MacBook Pro began to exhibit progressively stranger behavior as the day went on. Thursday morning, it would not boot at all, and would power off after unlocking the FileVault encrypted drive.  

So, no problem, I have a clone, which, true, is a couple weeks old, but I thought I could just boot off of that and copy the newer data off my failed OS X install. A plan which would have worked perfectly if I had not encrypted the drive. I could see my internal disk when booted off the clone drive, but I could find no way to unlock the disk to get to the data. Disk Utility showed the internal drive as being present and fine, but the one partition on it was marked as "unknown", since it was not unlocked at boot time. 

Luckily, Disk Utility has a command line version called *diskutil*, with more options and fine grained control. However, the command that I needed called for knowing the *UUID* of the disk, which I did not have. The command `diskutil ca list` will show you the UUID, sometimes, but I could not see the UUID of the logical volume of the disk I needed, I could only see the UUID of the physical volume (Incidentally, for more information on the new volume manager, check out the Ars Technica Lion review covering Core Storage [here][2].) I'm not sure what the rules are governing how and why diskutil will show the UUID, but I could not see the internal drive's UUID when booted from the clone. Without the UUID, I could not get to my data. 

So, I booted off the Lion recovery partition by holding down *⌘ R* after pressing the power button. After booting up, I opened the Terminal and typed `diskutil cs list`. Now we were getting somewhere. 

    
    Logical Volume B15D4021-F519-4F7B-9B78-D4001361BA32 B15D4021-F519-4F7B-9B44444001361BA32
 

The recovery partition *was* able to see the logical volume, but it was locked. To unlock the volume, I entered this command:

    diskutil cs unlockVolume B15D4021-F519-4F7B-9B78-D4001361BA32 -stdinpassphrase


The diskutil command prompted me for my passphrase, unlocked the disk, and mounted it under */Volumes*. The next trick was actually getting the data off the disk and onto my external disk. The recovery environment is very bare bones, there was no intention of using it as a file manager. The easiest thing to do was to rsync my home directory over to my clone disk. Since rsync is not available in the recovery manager, I used the version from my cloned disk, so the command looked something like this:

    /Volumes/Flux/usr/bin/rsync -avz /Volumes/Prime/Users/Me/ /Volumes/Flux/Users/Me


Where Flux is the name of my clone, and Prime is the name of my internal drive.

This effectively cloned only my home directory, saving the source code, college papers, photographs, and everything else I've collected in the two weeks since the last backup. Next, I booted off of my clone drive again, verified that my important stuff was there, including a few pictures I took yesterday morning, and used Disk Utility to wipe my internal drive. Finally, I started SuperDuper! on the clone, and tried to copy the good image back to the internal disk. 

Just then the internal drive failed. My problem was not with the 10.7.2 update, it was with the spinning rust inside my Mac. It seems I retrieved the data off of the internal drive just in time.





[1]: http://www.shirt-pocket.com/SuperDuper/SuperDuperDescription.html
[2]: http://arstechnica.com/apple/reviews/2011/07/mac-os-x-10-7.ars/13
