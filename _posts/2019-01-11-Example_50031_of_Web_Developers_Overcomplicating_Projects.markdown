---
layout: post
title: Example 50031 of Web Developers Overcomplicating Projects
date: 2019-01-11 20:39:51
tags: [web, jekyll, blogging]
---

I spent some time over the past couple nights adopting a new theme for the old digs here at jb. I found the [beautiful Chalk theme][1] by Nielsen Ramon and adopted my site to use it, including, finally, a working tags system. I'm quite happy with the tags, but I'm less happy with the bundled deployment system the theme shipped with. 

The theme depended on NodeJS to build and deploy to GitHub for reasons that I'm sure made complete sense to the developer but I simply don't care about. The documentation says to run `npm run publish` to build and push the site, doing so runs a script that does quite a bit of mucking about with the structure of the site.  

```bash
# Checkout gh-pages branch.
if [ `git branch | grep gh-pages` ]
then
  git branch -D gh-pages
fi
git checkout -b gh-pages

```

First thing we do is create a new branch and check it out. So far so good, I guess. 

```bash
# Build site.
yarn install --modules-folder ./_assets/yarn
bundle exec jekyll build
```

I'm not familier with `yarn`, but the site says that it provides "fast, reliable, and secure dependency management". Ok, fair enough, but what dependencies could my little blog possibly have? Apparently, the `package.json` file it lists what `yarn` is downloading:

```javascript
  "dependencies": {
    "jquery": "^3.2.1",
    "npm": "^6.0.1",
    "retinajs": "^2.1.1",
    "svgxuse": "^1.2.4",
    "webfontloader": "^1.6.28",
    "zooming": "^2.0.0"
  }
```

Eh… ok. Why do I need NodeJS for this again? So, Yarn installs a bunch of Javascript and then Jekyll builds the site. Moving on… 

```bash
# Delete and move files.
find . -maxdepth 1 ! -name '_site' ! -name '.git' ! -name '.gitignore' -exec rm -rf {} \;
mv _site/* .
rm -R _site/

```

Now things are getting interesting. This deletes everything except the git directory, the `.gitignore` file, and the site Jekyll just built. Then it moves everything out of the `_site` directory into the root and deletes that directory as well. 

```bash
# Push to gh-pages.
git add -fA
git commit --allow-empty -m "$(git log -1 --pretty=%B) [ci skip]"
git push -f -q origin gh-pages

# Move back to previous branch.
git checkout -
yarn install --modules-folder ./_assets/yarn

```
Add, commit, and push the changes to Github under the gh-pages branch, then checkout whatever you had previously and reinstall all the javascript. When I tried this my site went offline. I think this script might be out of date. GitHub requires sites that won't build in Jekyll to be in the master branch, and if you want to use a custom domain name you have to add a `CNAME` file with the domain name you want to use. 

To work around this I setup a separate repository just for the source of the site and moved the built site into the master branch of the main repository. But, when I pulled everything down on my MacBook, the site wouldn't compile, with Jekyll complaining about not being able to find Jquery. It was at this point I knew that I had gone down a terrible rabbit hole.

Luckily, I was able to get the site built once, so I had all the "*compiled*" code to work with. All I needed to do was use those files to build my own Jekyll theme with static assets and none of this Javascript build nonesene. Apparently the original theme was trying to do something fancy with the assets by dynamically renaming them and adding assets selectively to the compiled site. I don't care about any of that. 

Jekyll uses the liquid templating system, so it's trivial to go through the site and add tags to pull in the content you need during build time. Using the theme as shipped caused me to need three different package managers to build a static site. That's just not right. What's so wrong with HTML, CSS, and just a little bit of Javascript?

I don't know Nielsen, and I'm sure he had good reasons to build the theme like he did. I do think it's beautiful and I'm thankful that he released it as open source so I could use it. For me though, I don't need all those layers in my life. I just want an easy way to write and publish my site, and have it look and feel like something I care to have my name on. 

It used to be you could learn how to build a web site by right-clicking and selecting "view source". But now, [everything easy is hard again][2].


[1]: https://github.com/nielsenramon/chalk
[2]: https://frankchimero.com/writing/everything-easy-is-hard-again/