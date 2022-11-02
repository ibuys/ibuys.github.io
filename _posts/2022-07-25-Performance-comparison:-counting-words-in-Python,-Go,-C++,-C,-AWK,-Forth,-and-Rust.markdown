---
layout: post
title: Performance comparison - counting words in Python, Go, C++, C, AWK, Forth, and Rust
date: 2022-07-25 07:21:29
tags: linkpost
---

> A basic solution reads the file line-by-line, converts to lowercase, splits each line into words, and counts the frequencies in a hash table. When that’s done, it converts the hash table to a list of word-count pairs, sorts by count (largest first), and prints them out.

A fascinating read, and the results are surprising. For example, I honestly would have thought the pure Unix implementation would be faster than tested. It also surprises me that Swift is so slow. I wonder if someone who knows the language well could produce an optimized version for this sorting problem.

[Link](https://benhoyt.com/writings/count-words/)

