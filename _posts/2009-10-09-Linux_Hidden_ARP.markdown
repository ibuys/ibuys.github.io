---
layout: post
title: Linux Hidden ARP
tags: [work, linux, sysadmin]
---

To enable an interface on a web server to be part of an IBM load balanced cluster, we need to be able to share an ip address between multiple machines. This breaks the IP protocol however, because you could never be sure which machine will answer for a request for that IP address. To fix this problem, we need to get down into the IP protocol and investigate how the Address Resolution Protocol or ARP, works.

Bear with me as I go into a short description on how an IP device operates on an IP network. When a device receives a packet from its network, it will look at the destination IP address and ask a series of questions from it:

1. Is this MY ip address? 
2. Is this ip address on a network that I am directly connected to? 
3. Do I know how to get to this network?

If the answer to the first question is yes, then the job is done, because the packet reached its destination. If the answer is no, it asks the second question. If the answer to the second question is no, it asks the third question, and either drops the packet as unroutable, or forwards the packet on to the next IP hop, normally the device's default gateway.

However, if the answer to the second question is yes, the device follows another method to determine how to get the packet to it's destination. IP addresses are not really used on local networks except by higher level tools or network aware application. On the lower level, all local subnet traffic is routed by MAC address. So when the device needs to send a packet to an IP address on the subnet that it is attached to, it follows these steps:

1. Check my ARP table for an IP to MAC address mapping 
2. If needed, issue an ARP broadcast for the IP address 
	-- *an ARP broadcast is a question going out to all devices on the subnet that has the simple setup of "if this is your IP address, give me your MAC address"*
3. Once the reply for the ARP address is received, the packet is forwarded to the appropriate host.

So, to put this all in perspective, when multiple machines share the same IP address, each of the machines will reply to the ARP request, and depending on the order in which the replies are received, it is entirely possible that a different machine will respond each time. When this happens, it breaks the load balancing architecture, and brings us down to one server actually in use.

The next question is normally: *Why is that? Why do the web servers need that IP address anyway?* The answer to this is also deep in the IP protocol, and requires a brief explanation of how the load balancing architecture works.

To the outside world, there is one ip address for myserv.whatever. Our public address is 192.268.0.181 (or, whatever). This address is assigned three places on one subnet: load balancer, first web server, and second web server. The only server that is needs to respond to ARP requests is load balancer. When the load balancer receives a packet destined for 192.168.0.181, it replaces the destination MAC address with one of the addresses from one of the web servers, first web server or second web server, and forwards it on. This packet still has the original source and destination IP addresses on it, so remember what happens when an IP device on an IP network receives a packet... it asks the three questions outlined above. So, if the web servers did not have the 192.168.0.181 address assigned to them, they would drop the packet (because they are not set up to route, they would not bother asking the second or third questions). Since the web servers do have the ip address assigned to one of their interfaces, they accept the packet and respond to the request (usually an http request).

So, that covers the *why?*, let's look at *how?*. Enable the hidden ARP function by entering the following into /etc/sysctl.conf:

	# Disable response to broadcasts. 
	# You don't want yourself becoming a Smurf amplifier.
	net.ipv4.icmp_echo_ignore_broadcasts = 1 
	# enable route verification on all interfaces 
	net.ipv4.conf.all.rp_filter = 1 
	# enable ipV6 forwarding 
	#net.ipv6.conf.all.forwarding = 1 
	net.ipv4.conf.all.arp_ignore = 3 
	net.ipv4.conf.all.arp_announce = 2

The relevant settings are explained here: 

**arp_ignore = 3**: *Do not reply for local addresses configured with **scope host**, only resolutions for global and link addresses are replied.*

For this setting the really interesting part is the *configured with scope host* part. Before, using `ifconfig` to assign addresses to interfaces we did not have the option to configure a scope on an interface. A newer (well, relatively speaking) command, `ip addr` is needed to assign the scope of host to the loopback device. The command to do this is:

	ip addr add 192.168.0.181/32 scope host dev lo label lo:1
	
There are some important differences in the syntax of this command that need to be understood to make use of it on a regular basis. The first is the idea of a *label* being added to an interface. `ip addr` does not attempt to fool you into thinking that you have multiple physical interfaces, it will allow you to add multiple addresses to an existing interface and apply labels to them to distinguish them from each other. The labels allow `ifconfig` to read the configuration and see the labels as different devices.

example:

	lo	Link encap:Local Loopback 
		inet addr:127.0.0.1 Mask:255.0.0.0 
		inet6 addr: ::1/128 Scope:Host 
		UP LOOPBACK RUNNING MTU:16436 Metric:1 
		RX packets:9477 errors:0 dropped:0 overruns:0 frame:0 
		TX packets:9477 errors:0 dropped:0 overruns:0 carrier:0 
		collisions:0 txqueuelen:0 
		RX bytes:902055 (880.9 Kb) TX bytes:902055 (880.9 Kb)
		
	lo:1	Link encap:Local Loopback
			inet addr:192.168.0.181 Mask:255.255.255.255
			UP LOOPBACK RUNNING MTU:16436 Metric:1
	lo:2	Link encap:Local Loopback 
			inet addr:192.168.0.184 Mask:255.255.255.255 
			UP LOOPBACK RUNNING MTU:16436 Metric:1
  
Here, `lo`, `lo:1`, and `lo:2` are viewed as separate devices by `ifconfig`. 

Here is the output from the ip addr show command:

	1: lo: <LOOPBACK,UP> mtu 16436 qdisc noqueue 
	    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
	    inet 127.0.0.1/8 brd 127.255.255.255 scope host lo
	    inet 192.168.0.181/32 scope host lo:1
	    inet 192.168.0.184/32 scope host lo:2
	    inet 192.168.0.179/32 scope host lo:3
	    inet 192.168.0.174/32 scope host lo:4
	    inet 192.168.0.199/32 scope host lo:5
	    inet 192.168.0.213/32 scope host lo:8
	    inet 192.168.0.223/32 scope host lo:9
	    inet 192.168.0.145/32 scope host lo:10
	    inet 192.168.0.217/32 scope host lo:11
	    inet 192.168.0.205/32 scope host lo:12
	    inet 192.168.0.202/32 scope host lo:13
	    inet6 ::1/128 scope host 
	       valid_lft forever preferred_lft forever
	

Here we can see that the `lo:1` (etc...) addresses are assigned directly under the standard `lo` interface, and are only differentiated from the standard loopback address by their label.

Here is the same output from the eth2 device:

	4: eth2: <BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast qlen 1000
	    link/ether 00:10:18:2e:2e:a2 brd ff:ff:ff:ff:ff:ff
	    inet 192.168.0.73/24 brd 192.168.0.255 scope global eth2
	    inet 192.168.0.186/24 brd 192.168.0.255 scope global secondary eth2:1
	    inet 192.168.0.183/24 brd 192.168.0.255 scope global secondary eth2:2
	    inet 192.168.0.176/24 brd 192.168.0.255 scope global secondary eth2:3
	    inet 192.168.0.178/24 brd 192.168.0.255 scope global secondary eth2:4
	    inet 192.168.0.201/24 brd 192.168.0.255 scope global secondary eth2:7
	    inet 192.168.0.212/24 brd 192.168.0.255 scope global secondary eth2:8
	    inet 192.168.0.222/24 brd 192.168.0.255 scope global secondary eth2:9
	    inet 192.168.0.147/24 brd 192.168.0.255 scope global secondary eth2:10
	    inet 192.168.0.219/24 brd 192.168.0.255 scope global secondary eth2:11
	    inet 192.168.0.46/24 brd 192.168.0.255 scope global secondary eth2:5
	    inet 192.168.0.208/24 brd 192.168.0.255 scope global secondary eth2:12
	    inet 192.168.0.204/24 brd 192.168.0.255 scope global secondary eth2:13
	    inet6 fe80::210:18ff:fe2e:2ea2/64 scope link 
	       valid_lft forever preferred_lft forever

Same as above, the addresses do not create virtual interfaces, they are simply applied to the real interface and assigned a label for management by `ifconfig`.
Without the label, `ifconfig` will not see the assigned address. 

**arp_announce = 2**:	Always use the best local address for this target. In this mode we ignore the source address in the IP packet and try to select local address that we prefer for talks with the target host. Such local address is selected by looking for primary IP addresses on all our subnets on the outgoing interface that include the target IP address. If no suitable local address is found we select the first local address we have on the outgoing interface or on all other interfaces, with the hope we will receive reply for our request and even sometimes no matter the source IP address we announce.

This one is a little tricky, but I believe it deals with how the web servers talk with the clients requesting web pages. In order for the web page to come up and maintain a session, when the server sends a packet back to the client, it needs to come from the source ip address of the hidden ip address. In order to do this, the web server looks at the destination address of the client packet, and then responds using that as it's source IP address instead of it's actual IP address. Clear as mud, right!

I hope this helps explain things a little better about the hows and whys of the web server's side of load balancing. Note however, that I didn't talk at all about the edge server. That's because the edge servers job is done at the application level, and correct configuration of it does not require special consideration at the OS level.
