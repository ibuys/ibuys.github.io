---
layout: post
title: Nostalgic Development
date: 2019-11-01 15:43:53
tags: development mac web
---

Like many my age, my first introduction to writing code was creating basic web pages, mimicking what I could find by right-clicking on a site and selecting "view source". HTML was, and continues to be, simple. There are nested elements inside the top and bottom tags, and the styling sheet defines how those elements are presented. But, somewhere along the line we've collectively lost our way. 

For example, I recently worked on a rather large Python web app. The basic concept of a web app is fine, it dynamically creates the HTML on the backend and handles the input from the page. A layer on top of the HTML, but a necessary one to develop anything dynamic. The Python environment has its own package manager, and bundling things up is fairly simple. Then the developers decided to do some *modernization* of the UI, which required significant modifications to the build pipeline. 

Instead of a pure Python environment, we now needed Node.js. We aren't running a node server, we only need it for the build process. Not to build the actual application, mind you, just the CSS and javascript. Node famously comes with its own package manager, `npm`, and thank goodness, because our site suddenly needs 899 packages in the `node_modules` directory. Building on top of node we've got [React](https://reactjs.org) and [webpack](https://webpack.js.org). Webpack is a bundler used to process javascript and SASS files to compile them into javascript and CSS suitable for deployment. Why do we need [SASS](https://sass-lang.com)? I have no idea. I also don't know why we need to compile our javascript down into bundled javascript.

We've taken what was simple and beautiful and piled on so much clutter and junk that it's nearly unrecognizable from the days of "view source". As in all things, I'm sure there's a lot about this situation that I don't understand. I'm sure that the developers of these projects have good intentions, and see a definite need for their work. It's just that I don't see it. I don't understand why we need these layers of abstraction. 

I've been creating web pages for 20 years, in one form or another. I really thought that HTML 5 would be a renaissance of simple, usable web development, but for the most part, that hasn't happened. Well, at least we finally got rid of Flash. 
