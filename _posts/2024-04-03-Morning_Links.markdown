---
layout: post
title: Morning Links
date: 2024-04-03 07:01:00
tags: 
---

#### Tackle complex reasoning tasks with Mistral Large, now available on Amazon Bedrock

- [Link](https://aws.amazon.com/blogs/aws/tackle-complex-reasoning-tasks-with-mistral-large-now-available-on-amazon-bedrock/)

> Calculate the difference in payment dates between the two customers whose payment amounts are closest to each other in the given dataset:
> 
> '{
> "transaction_id":{"0":"T1001","1":"T1002","2":"T1003","3":"T1004","4":"T1005"},
> "customer_id":{"0":"C001","1":"C002","2":"C003","3":"C002","4":"C001"},
> "payment_amount":{"0":125.5,"1":89.99,"2":120.0,"3":54.3,"4":210.2},
> "payment_date":{"0":"2021-10-05","1":"2021-10-06","2":"2021-10-07","3":"2021-10-05","4":"2021-10-08"},
> "payment_status":{"0":"Paid","1":"Unpaid","2":"Paid","3":"Paid","4":"Pending"}
> }'
> 
> Output
> 
> To find the difference in payment dates between the two customers whose payment amounts are closest to each other, we first need to identify the two closest payment amounts and then find their respective payment dates.
> 
> The payment amounts are: 125.5, 89.99, 120.0, 54.3, 210.2
> 
> The two closest payment amounts are 125.5 and 120.0. The payment date for the payment amount 125.5 is '2021-10-05' and for the payment amount 120.0 is '2021-10-07'.
> 
> The difference in payment dates can be calculated as follows:
> 
> Date difference = |'2021-10-07' - '2021-10-05'| = 2 days
> 
> So, the difference in payment dates between the two customers whose payment amounts are closest to each other is 2 days.
> 

AWS does well when taking complex systems and packaging them up for consumers. I don't think we've seen the full impact of AI yet. Not even close. 


#### Casey Liss - Every Failure is an Opportunity

> So, I called Sonos support this morning, and braced for a fight — I’m about six months out of the warranty coverage.
> 
> Thirty minutes later, without any sort of arguing nor complaining, I have a RMA, and I’ll get a new Roam in a couple of weeks.

Reminds me of a time when I took my newly broken iPod Mini into an Apple Store. I showed it to the guy at the counter, he said he couldn't say for sure if it was accidental or manufacturing defect, so he went in the back and brought me a brand new one. I've been a fan since. Sounds like Sonos learned the right lesson.

#### New Spatial Personas

A pair of links for this one, one from each point of view:

- [Jason Snell at Six Colors](https://sixcolors.com/post/2024/04/spatial-persona-on-vision-pro-changes-the-game/)
- [Stephen Hacket at 512 Pixels](https://512pixels.net/2024/04/my-spatial-persona-impressions/)

> I was able to invite my friend Stephen Hackett’s Persona over to my house for a play date and we were able to chat face to face in a way that just seemed more natural than talking to a persona in a box. It felt more like it was him.

> After our excellent ideation session, we played a round of Battleship in the excellent Game Room on Apple Arcade. After I sunk all of his ships, we watched a few minutes of For All Mankind in a couple of immersive environments.

I had always wondered about SharePlay, prior to the Vision Pro. Why would I want to keep my phone up looking at someone on FaceTime while we both watched a movie? Never made sense. Now in the light of immersive virtual reality, it makes perfect sense. 

#### The one about the web developer job market

- [Baldur Bjarnason](https://www.baldurbjarnason.com/2024/the-one-about-the-web-developer-job-market/)

> We have the worst job environment for tech in over two decades and that’s with the “AI” bubble in full force. If that bubble pops hard before the job market recovers, the repercussions to the tech industry will likely eclipse the dot-com crash.

Well, this gave me a lot of food for thought. 

#### xz Utils Backdoor

- [Schneier on Security](https://www.schneier.com/blog/archives/2024/04/xz-utils-backdoor.html)

> I simply don’t believe this was the only attempt to slip a backdoor into a critical piece of Internet software, either closed source or open source. Given how lucky we were to detect this one, I believe this kind of operation has been successful in the past. We simply have to stop building our critical national infrastructure on top of random software libraries managed by lone unpaid distracted—or worse—individuals.

Not great news the past couple days from the software industry. 

