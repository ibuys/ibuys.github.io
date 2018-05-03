---
layout: post
title: The Hardware Racket
tags: work hardware sysadmin
date: 2013-04-15 10:40:11
---

Every now and then something just gets to me, and for the past few weeks, that something has been the process of purchasing enterprise hardware. Servers, SANs, load balancers, the kind of equipment that, instead of a price and an "Add to Cart" link, comes with directions on who to call. 

Most hardware is not purchased *directly* from the manufacturer. It's purchased through resellers, and each reseller will have a regional representative who will want to meet with you. The resellers don't really want to just sell you the hardware, they want to "partner" with you to "build a solution". They want to add consulting fees to your hardware purchase, and they want to jack up their margin on selling the hardware as much as possible. 

It's not small money we are talking about either. I've seen purchases of a single piece of equipment drop by $22,000 by modifying a single software line item. How much of that cost was the actual price of the software, and how much of it was reseller markup we will never know. The reseller program is built to keep us in the dark. For example, NetApp has a few nice bullet points on their "[Become a NetApp Partner](http://www.netapp.com/us/partners/become-a-partner/resellers.aspx)" page:

> The NetApp Partner Program for Resellers is designed to help you grow your business and maximize profitability. With NetApp® products and services in your portfolio, you can deliver innovative storage and data management solutions that satisfy even your most demanding customers.
> 
> As a NetApp Reseller, you can:
> 
> * Increase revenue
> * Earn greater returns on your investment
> * Leverage our tools, best practices, and technical experts
> * Create opportunities with our co-marketing resources, sales enablement programs, and prequalified leads
> 
> The combination of market momentum, increased demand for storage products, and innovative technology from NetApp makes this a great time to be a NetApp partner.

Pay special attention to "maximize profitability" and "increase revenue", because as a consumer of these goods, that's money out of your pocket. It's not that companies like NetApp don't have a price list, they do, it's just that the price goes through an algorithm first. I believe the algorithm takes into account the volume of sales by the reseller, the number of discounts available to the reseller, and probably a few other items. I'd love to get a look at it someday. 

In fact, I'd love to see a centralize, crowd-created database of hardware costs. A Web site that let me check on what the going rate was on a 10TB SAN. I'm not sure if I could convince anyone to do it, but it would be fantastic if sysadmins and IT managers around the country would upload the PDF quotes they get from resellers. Then we could parse the quotes, and come up with a general idea of what the market price is for the equipment. Right now, we just have to trust that whatever regional reseller we are working with is being honest and not gouging us. Hard to do with the salesmen arrive in BMWs and talk about their private pilots license. 


I've heard that it is "unethical" to share the quote we get from one reseller with another. I'm not sure about that. I believe that if the vendor knew that anything they gave to us had no expectation of privacy, we would be free to share the quote with whoever we choose. The resellers are the ones deciding the practice would be unethical because it would be bad for their business if they had to fairly compete on price. Personally, I would be satisfied with whichever reseller let me know up front what their cut of the deal was, and how I could calculate the most honest transaction for my company. Dealing with resellers is like trying to buy a used car or a gym membership. It's shady.

Here's another example of resellers behaving badly. We were in a meeting with a salesman, and an engineer from his company, and they had a manufacturer on a conference call to discuss the equipment we were pricing out. When we got to the end of the meeting and we thought we had all of our questions answered, we hung up on the manufacturer, and the resellers started undercutting their manufacturer "partner" to try to sell us a similar piece of equipment from another manufacturer. They said it was because they wanted to partner with us to make sure we got the best deal, but I was left with the impression that the equipment they tried to pitch simply gave them a fatter margin. 

This is the biggest draw, in my opinion, for open source software and [hardware](http://www.opencompute.org). If we can match the performance of these big name vendors using hardware that we can purchase from NewEgg, we won't have to deal with slimy resellers.


