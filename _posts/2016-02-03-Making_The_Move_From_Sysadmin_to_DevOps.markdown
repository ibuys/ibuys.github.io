---
layout: post
title: Making The Move From Sysadmin to DevOps
date: 2016-02-03 11:57:06
tags: [work, devops]
---

Everyone’s professional path follows a slightly different trajectory. We are each a unique recipe of skills, experience, and interests, which shape who we are and how we come to be in the careers that we have. My experience in moving from a systems administrator to a devops role is unique, because, well, we are all unique. 

Somewhere around January of 2010 I saw a shift in the future of the systems administrator role. Automation systems and cloud services were going to change things, and I knew that to stay relevant I was going to have to change too. At the time I felt a bit of an entrepreneurial pull, and decided I was going to be an  independent Mac developer. I bought [the book][1], set my alarm for an hour earlier each morning, and spent that hour digging through the book learning Cocoa and Objective-C. I did this for months, reading every page, every chapter, and finishing every programming challenge. At the end of the book I started working on my first app, an adoption of a shell script I called “go”. 

Go was basically a bookmark manager, but it let you bookmark *anything* on your Mac. I used it to quickly SSH to servers, mount NFS shares, launch internal management web apps, and other administrative tasks. I was a bit enamored by the delicious generation at the time, and made some rather, well, regrettable UI choices. When the Mac App Store was announced, I knew that I wanted to get my app in there on day one, so I started working right away on version two, or, [Go2][2]. Go2 launched in the MAS in 2011, but never sold enough to make it worthwhile. So, after taking a break from development, I started working on the next app, a static blogging app I called “[Paragraphs][3]”. I worked on this app for months, launched it, watched it fizzle out, and decided I needed to rethink my professional goals. 

During this same period I went to grad school for [Human-Computer Interaction][4]. I still saw that I needed to change my professional career path, I was fascinated by design and the science of how we use these machines, and felt it a personal goal of mine to have a graduate degree. So, nights and weekends for two years I was neck deep in a mix of psychology, Adobe Illustrator, OmniGraffle, [Silverback][5], and Python. I graduated with a Masters degree in HCI in 2012, spent a few months at a start up in Des Moines, went back to CDS, and the following year [shut down my development company][6]. All while holding down a full time job and raising a family. To say I was stressed doesn’t even come close. 

At CDS I was a Linux sysadmin, but I was also very deeply involved in the design and deployment of the architecture. After my boss quit I applied for and was appointed to a new position titled “Systems Architect Consultant”, which was kind of a fancy term for special projects and development. I had been studying automation, cloud architecture, high availability, and the myriad of other topics surrounding devops, but as the systems architect I was solely devoted to researching those topics and designing solutions based on my research. Around the end of my time there CDS sent me to AWS re:Connect, where I was kickstarted into learning just how big AWS was, and the reality of what I foresaw years before hit me with full force. 

I could tell that things were not going well at the company though, and two months before a big round of layoffs I made the move to work for a small software shop named Future Health Software as a systems automation engineer. Unfortunately, between the time I interviewed for the position and the time I was hired, the company was acquired by an investment firm that also acquired Future Health’s biggest competitor, Chirotouch. 

Not wanting to concern myself with any of the internal politics or rivalries involved in merging two previously competing companies, I dug into my work and learned everything I could about running production workloads on AWS. I kept an open mind, and learned that the AWS systems were meant to be used like a development framework, bootstrapping an application in the most efficient way possible. Of course, most places hadn’t used the service like this, especially the ones that had been using AWS since all that was available was EC2 and S3. So, I set about rebuilding the entire architecture, six years of it, in CloudFormation code, and developing a deployment system based on CodeDeploy. 

After several months of setbacks, wrong turns, and distractions of managing the legacy environment, I had a system that could rebuild the entire infrastructure from scratch. I’m quite proud of that work, and hope to someday put it under a production workload. Unfortunately, before I got the chance, the company closed our office and announced that we were going to be let go.  Which brings us to today.

Over the years as I’ve worked out where I want to be in my professional life I’ve learned many different technologies. I’ve spent time digging through the Linux kernel source and reading RFCs, I’ve learned to think pragmatically, read and understand code, and build systems from the ground up. I’ve also learned how the people who use the systems I build actually *use* them, and how the design choices I make affect the usability and reliability of the system. 

For me, the path to get from a sysadmin to a devops engineer travelled from Unix to Linux, through Cocoa and Objective-C, past Python and PHP, stopping in HCI, design, and UX, back to Linux, Docker, and now on to the cloud. And you know, what? It’ll never stop. The tech industry moves fast, you’ve got to keep learning your entire life to stay on the right side of that wave. You’ll either ride it, or be crushed by it, but it’ll never stop. 

So, be open to learning new things, try something out of the ordinary, push yourself to try something you haven’t done before, and always [do your absolute best][7]. I promise it’ll be a heck of a ride.


[1]: http://www.amazon.com/Cocoa-Programming-Mac-4th-Edition/dp/0321774086
[2]: https://github.com/ibuys/Go2
[3]: https://github.com/ibuys/Paragraphs
[4]: http://www.vrac.iastate.edu/hci/degree-programs/online-masters/
[5]: https://silverbackapp.com
[6]: https://jonathanbuys.com/06-06-2013/Farmdog_Co._Sold.html
[7]: https://jonathanbuys.com/05-14-2008/the-master-craftsman.html
