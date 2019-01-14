---
layout: post
title: Should All Software Be Free
---

## Introduction ##

We live in the information age. Digital devices and Internet connected, hand held computers are the prevalent way we communicate. The price for computers and for access to the Internet has dropped, and availability of publicly accessible Internet connected computers has risen. Schools across the country are providing computers to their students, some as early as sixth grade, and public libraries have been equipped with computers and, in some cases, free wireless Internet access. With the prevalence of computers of all shapes and sizes across nearly all parts of our society, questions about their ethical use and the purpose and place of computers in our lives have risen. One such question that has been debated since the early 1980s is “Should all software be free?”

“Free” in the English language is a fairly relative term. The New Oxford American Dictionary contains eight definitions of the word “free”, as well as an additional two adverb uses of the word. In the context of the question above, “Should all software be free”, the obvious meaning of the word is the fifth definition, which reads “given or available without charge”. However, the more academically interesting, accurate, and perhaps even subversive meaning of the word free is the first definition, which reads “not under the control or in the power of another; able to act or be done as one wishes”. Most computers shipped today come pre-installed with software that does not fall under either of these definitions of free, but should they? From a purely ethical context, should the user of software be able to copy, modify, and redistribute software as he sees fit? What are the social implications of an enmasse migration to free software?

There are many answers to this question, depending on who you ask. On one end of the spectrum are large proprietary software companies like Microsoft, Adobe, and Apple. These companies view software the same as they would a physical product, like a toaster. They design, engineer, and test the software, then package it and sell it to consumers to run on their computers.

On the other end of the spectrum is the Free Software Foundation, founded by Richard Stallman, who evangelizes the philosophy that all software, independent of the original author, should be free of restrictions.

## History ##

In 1983 Richard Stallman was working as a programmer in the artificial intelligence lab at the Massachusetts Institute of Technology (MIT). By this time in his career, he had already garnered a certain amount of recognition in the small but burgeoning hacker community as a talented developer, largely due to his creation of the EMACS text editor, and his academic papers on artificial intelligence. Stallman embraced the openness and sharing of the hacker community, and found an ethos that would shape his career in the years to come. Towards the end of his work at MIT, Stallman found an increasing amount of proprietary software in use where he worked. One example in particular was a new printer that was installed on the network, which he was unable to gain access to the source code to. In a previous printer, he was able to expand the functionality of it to send messages when a printing job completed. Stallman’s inability to enhance the functionality of the printer based on the companies unwillingness to share source code with him was instrumental in convincing Stallman that proprietary software was ethically wrong. Stallman recalled the beginnings of the GNU project at a talk he gave at Google:


>“So I found myself in a situation where the only way you could get a modern computer and start to use it was to sign a non-disclosure agreement for some proprietary operating system. Because all the operating systems for modern computers in 1983 were proprietary, and there was no lawful way to get a copy of those operating systems without signing a non-disclosure agreement, which was unethical.” ([Stallman, 2004][1])

Shortly thereafter, he started the GNU project.

GNU is a recursive acronym for “GNUs Not Unix” , a play on words to indicate the purpose of the project, to create a Unix-like operating system that is freely available to anyone. The project was announced in late 1983, and officially started in early 1984. Stallman created a debugger (gdb), and a C compiler (gcc), and ported his popular text editor EMACS to the project as GNU EMACS. Launching the GNU project officially started the Free Software Movement, and Richard Stallman created a non-profit corporation named the Free Software Foundation to support the objectives of the new movement. ([Stallman, 2010][2])

The GNU project worked for the next several years to develop the operating system, but were unable to successfully develop a reliable kernel, the core of the system. In 1991, an unexpected answer to this problem came in the form of a Finnish college student named Linus Torvalds who developed a clone of an educational version of the Unix kernel and named it Linux. Linus licensed his new kernel under the GNU GPL, and combined his new kernel with the GNU userland tools to create a fully functional operating system, properly named GNU/Linux.

The Free Software Foundation defines four essential “freedoms” that all people using software should have the right to enjoy. Using a hacker mentality, the freedoms are numbered starting at zero, a common programming practice. The four software freedoms are:

* Freedom 0: The freedom to run the program, for any purpose
* Freedom 1: The freedom to study how the program works, and change it to make it do what you wish. Access to the source code is a precondition for this.
* Freedom 2: The freedom to redistribute copies so you can help your neighbor
* Freedom 3: The freedom to distribute copies of your modified versions to others. By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

In order to meet the Free Software Foundation’s definition of free software, an application’s licensing must meet all of these requirements. The FSF maintains a list of licenses that they find meet the definition of free software on their web site. The four freedoms are devised to give the user of the software complete control over their computing environment. For example, in an office environment where there are several computers, free software would enable the users to modify the application to suit their needs, and install the application on as many computers as they wished, without having to worry about additional software licensing or the possibility of breaking a contract with the developers of the software.

While the GNU project was founded to recreate a Unix-like operating system from scratch, another project was created that derived it’s source code from the original Bell Labs Unix directly.
During the late 1970’s the University of California, Berkeley worked closely with Bell Labs developing the Unix operating system, sharing source code and fixes between the two. Berkley’s version of Unix became known as the Berkeley Systems Distribution, or BSD, and was distributed to colleges along with a license. When Bell Labs was bought out by AT&T, the focus of Unix development shifted to a stable, proprietary model for marketing to clients. AT&T changed the terms of the source code license to charge a substantial fee for universities to gain access to the source code. Around this same time, Berkeley independently developed a networking stack for the TCP/IP protocol for Unix, combined it with their BSD version, and made the source code available for a substantially lower fee. Encouraged by other universities and people interested in BSD, Berkeley continued working on rewriting utilities developed by AT&T for inclusion in BSD.

Through several iterations, splits, and rewriting of source code utilities and kernel files, there eventually appeared three versions of BSD: NetBSD, FreeBSD, and OpenBSD. There was also a fourth version, BSDi which was a commercial venture based off of the earlier works of Berkeley and their own rewritten kernel. (Bretthauer, 2002) Although BSD can clearly trace the ancestry of its code back to the original Unix of Bell Labs, due to a legal complication, no version of BSD can officially be called “Unix”. The Unix name is a trademark owned by Novell, who was recently purchased by Attachmate.

The commercial version of Unix was adopted by several vendors, and is now actively being sold and supported by IBM as AIX, HP as HP-UX, and Oracle as Solaris. Before being acquired by Oracle, Sun Microsystems released the source code of Solaris as OpenSolaris. Since the acquisition, the OpenSolaris project has been rumored to be disbanded in the near future. In response to the rumors, OpenSolaris has spawned the Illumos project to continue development of the released code.

BSD, along with the Mach kernel, also provides the core of both Apple’s Mac OS X and iOS operating systems. 4.4BSD was incorporated into NEXTSTEP, which was developed by NeXT corporation. Apple acquired NeXT in 1996, and began work incorporating NEXTSTEP into the Mac OS. Mac OS X Developer Preview 1, based on NEXTSTEP, which was based on BSD, was released in May 1999. (Singh, 2003) In 2007, Apple released the iPhone, running a stripped down, minimalistic version of OS X which was later renamed iOS. iOS and Mac OS X share a common ancestry that maps back to BSD, and from there back to Bell Labs and the original Unix.

## Software Licenses ##

Although Mac OS X shares it’s history with the BSD variants, only a limited subset of its source code is available outside of Apple. Apple has made significant changes to the core source files of BSD, and released their version of BSD in a limited fashion as Darwin. Apple released a downloadable installer for Darwin as an image file (ISO) that could be burned to a CD-R, up until 2007, which corresponded with the release of Mac OS 10.5, Leopard. After this point, Apple released only the source code required by the license for open source tools included in Mac OS X or iOS. Apple utilized the BSD operating system, wrote their own tools and layers on top of it, repackage it, and sell the new operating system as their own. They were able to do this because of the liberal BSD license, which states:

>Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
> * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
> * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. ("Open source initiative," )

The BSD license does not place restrictions on how the source code or binary programs are used or distributed, allowing that the redistributed application attribute BSD. This license reflects the academic roots and philosophy of the developers of BSD, who wished to make the system as open as possible to contribution. This style of license is very different from the license adopted by the GNU project, who developed the license based not only on their own philosophy that software should be free of restrictions, but also their own moral code.

To enforce the four essential freedoms, the GNU project created the GNU General Public License, or GPL for short. The GPL is a copyright license, legally enforceable, that protects the rights of users to create, modify, and distribute free software. The GPL also restricts what developers can do with code that they use that is already covered under the GPL. The GPL explicitly prevents developers from adding to, or deriving from, GPL code to create a new product, without also covering that code under the GPL. This restriction gives the GPL a viral aspect, as it can be seen to infect all other code it touches. If Apple had based Mac OS X on a core of GNU/Linux instead of BSD, it is very likely that Apple could have become entangled in a costly legal battle over he right to distribute their code in binary form.

For applications to comply with Freedom 0 as defined by the Free Software Foundation, the applications must allow no possibility to restrict the application from running. (Stallman, 2004)
This means that any type of license key enforcement or digital rights management software would be prohibited. In contrast, the iPhone contains software which can only be used for one purpose, as stated by the [iPhone Software License Agreement][3], section 2a, which states:

> Subject to the terms and conditions of this License, you are granted a limited non- exclusive license to use the iPhone Software on a single Apple-branded iPhone. 

The definitions of freedom offered by the Free Software Foundation act on the assumption that computers are central to a persons well being, and that there should be a natural right possessed by the user of any computer to have full and complete access to the computer based on that natural right to well being. However, it is my position that computers, or any other form of technology, only serve to increase personal freedom of the user in proportion to the increase in overall quality of life of the user of the technology. If the user possesses no knowledge of programming languages, than access to the source code does him little good. However, the user can hire a programmer to modify the source code for him, or group together with other users to raise a larger amount of money for the programmer, depending on the difficulty of the change requested.

## Intellectual Property ##

In chapter four, section 2, of the textbook Ethics for the Information Age, intellectual property is defined as “any unique product of the human intellect that has commercial value”. 

This concept of property is derived from John Locke’s writing The Second Treatise of Government, where Locke states that people have a right to their own labor, and a right to things that they have removed from nature through their own labor. The text then brings up an example of how this right can be misconstrued with the concept of intellectual property using William Shakespeare writing Hamlet. If Shakespeare writes Hamlet in a pub one night after listening to the rumors of royal intrigue, than it is agreed that the play is the result of his labor, and therefor he should have the right of ownership to it. However, if Ben Jonson listens to the same rumors in a separate pub across town, and then simultaneously with, but independent of, Shakespeare, writes Hamlet, then the text claims that ownership of the intellectual work is in question. There were two authors, but only one work, which creates a paradox when viewed in light of Locke’s reasoning.

The text is using flawed reasoning in this example. According to the text, “even though Jonson and Shakespeare worked independently, there is only one Hamlet”, but that two creative people could work independently to create the exact same work is impossible. The actual outcome of the Shakespeare example would be that there were two plays, Hamlet, and a very similar, but different, play written by Jonson. The text appears to be begging the question, since it assumes that the possibility of identical creative works is realistic.


If we assume that software is a creative work, similar to writing, art, or music, than it is logically assumed that the original author of the software is entitled to some form of ownership. 

Copyright law dates back to the original printing press and the first ability to create copies of creative works quickly and efficiently. The first copyright law was passed in 1735 by the English Parliament as the First English Copyright Act, recognizing an original authors right to his creative work. ([Ballon, & Westermann, 2006][4])

The GNU project takes a contrary stand on the subject of ownership of software. Richard Stallman, in his essay entitled “Why Software Should Not Have Owners” claims that authors of software can claim no natural right to their work, citing the difference between physical products and software, and rejecting the concept of a tradition of copyright. Stallman uses an example of cooking a plate of spaghetti to explain the difference between software and physical products:

> “When I cook spaghetti, I do object if someone else eats it, because then I cannot eat it. His action hurts me exactly as much as it benefits him; only one of us can eat the spaghetti, so the question is, which one? The smallest distinction between us is enough to tip the ethical balance.
> But whether you run or change a program I wrote affects you directly and me only indirectly. Whether you give a copy to your friend affects you and your friend much more than it affects me. I shouldn't have the power to tell you not to do these things. No one should.” ([Stallman, 2010](http://www.gnu.org/philosophy/why-free.html))

However, Stallman does not address what gives the second person who receives the software the right to benefit from the authors work without giving something in return.


## Ethical Frameworks ##

Before the industrial revolution, most people learned a skill and worked for themselves in small communities. A single village would have all of the skill sets necessary to sustain itself, and each member of the community would apprentice into a particular skill set to contribute and earn a living. The industrial revolution pushed skilled workers into factories and assembly lines, work that was both distasteful and disdainful to an artisan in the craft. However, corporations were able to reduce cost and increase profits, and the platform has persisted into current work environments. 

In the information age, the assembly line mindset has created oceans of cubicles filled with programmers who use their skills in small parts of large software projects, sometimes to great success, but far too often to failure. The Internet and popularity of lower priced computers has created a market for high quality third party software, the kind that is created by someone with a passion for what they are doing. This passion comes from learning a craft, and using that skill to earn a living, just like the workers from before the industrial revolution. Instead of living physically in small villages, these new age artisans live online and create communities built around social networking. ([van Meeteren, 2008](http://indie-research.blogspot.com/)) 
    
In many ways, this is a return to a more natural way of life, and a simple form of commerce. One person can create an application and sell it, and another person can buy it from him. The person selling the software benefits from being able to purchase shelter, food, and clothing for his family, and the person who buys the software benefits from the use of the software. It is a very simple transaction, and a model that is not adequately explained in the GNU essays. If all proprietary software is wrong, then an independent developer who sells software as his only job is also wrong.

GNU supporters could argue that there is nothing stopping the programmer from selling his software, but he should give away the source code under a license that permits redistribution along with the software once it is sold. At this point, selling the original program no longer becomes a viable business model. A programmer can not continue to sell his software when the user can, and is encouraged to, download his software from somewhere else for free.

While it may be the ethically right thing to do to purchase the software if you intend to use it, ethics alone are often insignificant motivation to encourage people to spend their money. If the choice of supporting the development of the software or not is entirely up to the user of the software, then purchasing the software becomes a choice that the user can make on a whim, with no real implications on the conscience of the user with either decision. GNU and the GPL place this decision squarely on the user, and encourage the users to not feel in any way obligated to pay.

The ethics of open source come into question when the requirement of adhering to the free software philosophies result in an independent developer not being able to support a moderate, middle-class lifestyle by developing a relatively popular application. Kant’s first formulation asks what would happen if all developers gave away the source of their code for free. The developer being the agent, his maxim would be giving away the source code of the application he developed to earn money. In this imaginary world where all developers did this, the quality of software would go down to the lowest common denominator of acceptability. Each developers motivation would be to develop for himself, and since he would need to find a source of income elsewhere, only in the free time allotted to him. This would result in a wide variety of software availability, with very little integration, testing, or source control, mirroring the current state of GNU/Linux based desktop operating systems.

Current software companies would move to a business model arranged around providing support to customers of their software. Competition, and therefore innovation, based on pure software features would decrease, since the source code of any feature another group could develop would be easily copied and integrated into competitors products.

From a utilitarian point of view, the outcome of proprietary software has clearly been to produce more pleasure for more people than open source has up to this point. Open source software is often more complicated, difficult to learn and maintain, and harder for the average computer user to use. Apple produces proprietary software and hardware, and states their mission to “make the best stuff”. Using their position as a leading software company, and leveraging their control over their computing environment, including iPads, iPods, iPhones, and Mac computers, Apple has been able to successfully negotiate deals with entertainment companies. The deals Apple has made allow the consumer to download music, television shows, and movies off of the Internet and watch them on any Apple branded device, and output the media to their televisions or home stereo systems. Because of the limits of Digital Rights Management, open source or free systems have not been able to provide this level of entertainment.

## Conclusion ##

To answer the question of whether all software should be free, this article has examined a brief history of open source software, the concept of intellectual property, and finally an ethical analysis of the concepts of open source. I have found that there is a strong connection between an original author and their work, but have found no evidence or compelling argument that all software, or all forms of any genre of creative work, should be free of restrictions. I have found that there is a benefit of open source and free software to the public, cited numerous times in the essays of Richard Stallman and the GNU project. Free software enables the user to learn the intricacies of how the software works, and modify the software to suit his needs. Free software also provides a legal and ethical alternative to expensive proprietary software in developing nations or areas where the cost of obtaining a license for legal use of the software is prohibitive. Public institutions, like schools and government offices, where the focus of the organization is the public good, have the option to use software that is in the public domain and is not controlled by any one company. Free software also gives the user the option to “help their friend” by giving them a copy of the software, without having to worry about payment or licensing restrictions.

I have also found compelling evidence that proprietary software is beneficial to the public, as well as respectful of the original authors rights regarding their creative work. Software is the result of a person’s labor; it does not matter how easy it is to copy that work, the author still retains a natural right of ownership, according to John Locke’s The Second Treatise of Government.
Proprietary software enables products like the iPad, which is being used to enable elderly people, nearly blind with cataracts, to create creative works of their own. ([Newell, 2010](http://www.portlandtribune.com/features/story.php?story_id=128882605915653000)) The iPad is also being used by caretakers of severely disabled children to enable them to communicate and express themselves. ([Hager, 2010](http://www .nytimes.com/2010/10/31/nyregion/31owen.html)) It is possible that the iPad would have been created if the software used to power it had been free, but that is unknown. What is known is that the net result of the device is to better peoples lives, which is the true purpose of technology. Any technology is merely an enabler to get more satisfaction and enjoyment out of life.

The free software movement exaggerates the importance of a specific type of freedom, without addressing the proper place of technology in our lives.

The existence of free and open source software alongside proprietary software creates a mutually beneficial loop, wherein consumers and developers are able to reap the rewards of constant innovation and competition. I have found that there is a place for both proprietary and free software, and that the authors natural right to their creative work gives them the freedom to choose how and why their software will be distributed.


## References ##

Ballon, H, & Westermann, M. (2006, December 1). Copyright ownership in works of art and images. Retrieved from http://cnx.org/content/m13912/1.2/#footnote1

Bertot, J, McClure, C, & Jaeger, P. (2008). The impact of free public internet access of public library patrons and communities. Library Quarterly, 78, 285-302.

Bretthauer, D. (2002). Open source software: a history. Information Technology and Libraries, 21(1), 3-11.

Crawford, M. (2009). Shop class as soulcraft; an inquiry into the value of work. New York, NY: Penguin Group.

Hager, E. (2010, October 29). Ipad opens world to a disabled boy. Retrieved from http://www .nytimes.com/2010/10/31/nyregion/31owen.html

iPhone software license agreement. (n.d.). Retrieved from http://www .apple.com/legal/iphone/us/terms/sla.html

Kain, R, & Bruce, I. (2010, November 22). Novell agrees to be acquired by attachmate corporation. Retrieved from http://www.novell.com/news/press/novell-agrees-to-be-acquired- by-attachmate-corporation/

Newell, C. (2010, November 4). Life is a limerick for centenarian virginia campbell. Retrieved from http://www.portlandtribune.com/features/story.php?story_id=128882605915653000

Open source initiative osi - the bsd license. (n.d.). Retrieved from http://www .opensource.org/licenses/bsd-license.php


Quinn, M. (2009). Ethics for the information age. Boston, MA: Pearson Education Inc. Singh, A. (2003, December 1). A brief history of mac os x. Retrieved from http://osxbook.com/book/bonus/ancient/whatismacosx//history.html


Stallman, R. (1977). Forward reasoning and dependency-directed backtracking in a system for computer-aided circuit analysis. Artificial Intelligence, 9(2), 135-196.

Stallman, R. (2004, June 11). Gnu and the free software foundation engineering tech talk at google. Retrieved from http://www.gnu.org/philosophy/google-engineering-talk.html

Stallman, R. (2010, November 12). The gnu project. Retrieved from http://www .gnu.org/gnu/thegnuproject.html

Stallman, R. (2010, November 14). Why software should not have owners. Retrieved from http://www .gnu.org/philosophy/why-free.html

Teli, M. (2010). Collective ownership in free/libre and open source software: the opensolaris case. Conference Proceedings of JITP 2010: The Politics of Open Source, 138-159.

van Meeteren, M. (2008). Indie fever; the genesis, culture and economy of a community of independent software developers on the macintosh os x platform. Informally published manuscript, Human Geography, University of Amsterdam, Amsterdam, Holland. Retrieved from http://indie-research.blogspot.com/

Williams, Jonathan. (2009, December 6). Free computers given to students. Retrieved from http://articles.baltimoresun.com/2009-12-06/news/bal-ho.computers06dec06_1_bright-minds- foundation-computer-refurbishing-organization-freshmen-laptops












[1]: http://www.gnu.org/philosophy/google-engineering-talk.html
[2]: http://www.gnu.org/gnu/thegnuproject.html
[3]: http://www.apple.com/legal/iphone/us/terms/sla.html
[4]: http://cnx.org/content/m13912/1.2/#footnote1
