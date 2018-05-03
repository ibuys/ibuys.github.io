---
layout: post
title: Serverless Jekyll Hosting on AWS
date: 2017-07-07 09:38:14
tags: 
---

This is a bit silly, I’ll be the first to admit. The contraption I’ve built to host this site is clearly unnecessary, especially when I could host the site on [Github][1] for free, with very little effort, but I was curious, so down the rabbit hole I went. 

I thought it would be interesting to [host my site on S3][2]. The site is entirely static,  no database back end or dynamic programming required to generate the site, it’s just HTML, CSS, and Javascript. I also wanted to understand the [AWS CodeBuild][3] service, and how I might be able to use it for other projects. 

There are four components of this system: Github, which hosts the code for the state. The domain name is registered and managed through [Route53][4], where I’ve configured an “A” record as an alias to point at the S3 bucket which hosts the site. Finally, CodeBuild is the glue which pulls the code from Github, runs `jekyll build`, and pushes the site to S3. 

CodeBuild works by starting a Docker container and pulling the repository down. It then looks for a file named `buildspec.yml` which contains the instructions to build the project. This file contains arbitrary Linux commands, whatever you need to build your code. Mine looks something like this:

	version: 0.2
	
	env:
	  variables:
	SITEBUILD: "yes"
	phases:
	  install:
	commands:
	apt-get update -y
	  pre_build:
	commands:
	gem install bundler
		bundle install
	  build:
	commands:
	echo Build started on date
		bundle exec jekyll build
		aws s3 sync _site/ s3://jonathanbuys.com
	  post_build:
	commands:
	echo Build completed on date

The interesting thing about this system is that I could replace Jekyll with [Hugo][5], [Hakyll][6], or any other static site generator, even my own scripts, and the system would stay the same. I’d just need to update `buildspec.yml` with the new commands to install the right tools and build the site. Hosting costs so far have been pennies, my cost this month *might* reach $1.27, and for the past couple months the cost has been below one dollar. 

I’ve been considering making this system more user friendly and monetizing it somehow. There’s a business model to be had in here somewhere, if I care to pursue it. Even though blogging in general appears to be in somewhat of a decline, publishing platforms will always be needed. 

[1]:	https://pages.github.com
[2]:	http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html
[3]:	https://aws.amazon.com/codebuild/
[4]:	https://aws.amazon.com/route53/
[5]:	https://gohugo.io
[6]:	https://jaspervdj.be/hakyll/