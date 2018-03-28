---
layout: post
title: A Technical Education - Base Level Hardware
date: 2014-09-20 21:19:18
tags: ate, hardare
---

The first and most important thing to remember when considering a computer is that computers are machines. Incredible, wondrous, bordering on magical machines, but machines nonetheless. They were built by people who are no smarter than you, and designed by people every bit as fallible as you. There are no magic incantations, no special spells, and no generational gap that make one group of people better able to understand computers than another. Computers are machines, machines that **you** can understand. 

So let's get started.

Viewing a computer from the outside, there are four main components. Normally two ways to interact with the computer, a mouse and a keyboard. There will be a way to view the results of your interaction through the monitor, the screen that is the most visible part of the machine, and there will be the case that encloses the actual guts of the machine, the engine if you will. 

These main external parts are present in computers of all sizes, even a smart phone, although the input mechanism and the screen have been combined. 

Inside the case, all computers share the same basic components: CPU, RAM, storage, networking, and input and output ports. Let's go over each component. 

*CPU* 

The central processing unit, CPU, can be considered the brain of the computer. At a high level, you can think of it as making decisions, very simple decisions, very, very quickly. The speed at which it makes these decisions is measured in hertz. A CPU that operated at one hertz would make one decision per second, but that would be an incredibly slow computer. Most computers now work with CPU's measured in Gigahertz. For example, the computer I'm using to type this on has a CPU speed of 2.66 GHz, which means it can make 2,660,000,000 decisions per second. 

Secondly, most CPUs come with multiple *cores*. A single CPU with two or more cores can be thought of as having the ability to make more than one decision, or threads of decisions, at a time. Each core runs at the same speed, but can operate on different information.

Generally, the faster the CPU speed, the faster the computer can process information, which *should* make it feel faster to the user. However, the other parts of the computer contribute to the overall feel of responsiveness too. 

*RAM*

While the CPU is working on making all those decisions, it needs a place to put things. RAM, which stands for Random Access Memory, and is also known as primary storage, is a fast, convenient place for the CPU to put things that it’s currently working on, or that it has worked on recently, and might work on again. Here’s an example: if you open up a document in Word, everything you are typing into the document is being stored in RAM, up until the moment you choose to save the document. Unfortunately, RAM doesn’t persist between reboots, so everything that is saved *only* in RAM is lost if the computer reboots. If we want to save things on the computer for good, we have to save it to *secondary storage*, also known as the hard drive. 

*Storage*

There are two options for storage in computers today: traditional spinning disk hard drives, and the newer and much, much faster solid state drives, called SSDs. Hard drives are slow because on the inside there is a metal platter spinning at thousands of revolutions per second, and a mechanical arm holding a head that moves across the disk to read and write the data. While advances in hard drive technology have made access faster over time, the physical limitations of the mechanics make this part the slowest on the computer. 

On the other hand, an SSD has no moving parts, and access to reading and writing the data is done entirely electronically. An SSD is an order of magnitude faster than a hard drive, but for the moment it holds less data and is more expensive than hard drives. That’s the trade off, today, you either pay more for a faster computer with less storage, or less for a slower computer with more storage. 

In my opinion, the price of solid state drives has come down enough that unless you know you need *lots* of internal storage, go for the SSD. It will make the entire computer feel faster.

*Networking*

Networking is a complex topic, and to fully understand it is beyond the scope of this introductory article. In a future ATE article we will cover the basics of how the Internet works, but not today. Suffice to say that there are two forms of networking to be concerned with: wired and wireless. Wireless, or WiFi, uses a small radio inside of the computer to connect to a network. The stronger the signal, and the less interference there is with the signal, the better your connection will be. Generally, if you are connecting at home or at school, your computer will share a network with other devices, and will connect to one or more wireless routers or access points. The router will most likely connect to a cable modem (assuming a home network), and the cable modem provides access to the Internet. 

Wired networking uses a standard called [Ethernet](http://en.wikipedia.org/wiki/Ethernet). Basically, there is a cable that connects your computer to a router, and the router connects to the modem for Internet access. Again, there are trade-offs. Wireless access is simple to setup, and lets you move your computer all around your house or school without loosing access to the Internet. The cost of this convenience is speed. Although WiFI is getting faster, it is still nowhere near as fast or as reliable as a directly cabled connection. 

For me, the convenience of wireless outweighs the speed and reliability benefits of a wired connection. If I used a desktop computer that was always in the same spot, then a wired connection would make far more sense. 

*Input/Output Ports*

Along the side or back of your computer will be a series of ports; different shaped plugs for different types of cables. These ports allow you to connect additional devices to your computer to extend the usefulness of the machine. For example, you may wish to add an external display to a notebook computer, and would plug into the mini-display port. Or, you may wish to plug in an external hard drive to backup your computer, and would plug the drive into the Universal Serial Bus (USB) port. There are normally ports for headphones and microphones, and possibly a place to plug in storage cards from cameras. 

Most modern computers will allow you to plug a device into one of these ports have have the computer automatically configure the device for use. Don’t be afraid to plug something in, and if it doesn’t work, don’t be afraid to pull it back out again. That’s what the ports are there for. Some devices, like hard drives, want to be “ejected” before pulling the cable out of the computer, but even that may soon be a thing of the past. 


*Motherboard*

One last part I forgot to mention above: the motherboard. Also known as the “system board”, the motherboard is the glue that connects all the other components together. Everything connects to the motherboard, and thin strips of conductive material printed onto the board called the bus connect the different parts together. 

*Conclusion*

You look at the screen, type on the keyboard, and interact with the mouse or touchpad. Internally, the computer uses the CPU to make decisions, stores things temporarily in RAM, writes data permanently to a storage drive, connects to the Internet over a wired or wireless network connection, and is extensible via the input/output ports. And, all the different parts connect through the motherboard. 

Now that we’ve covered the basics of hardware, next week we will talk about some of the software that makes the machine come to life. 

