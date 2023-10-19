---
layout: post
title: Loading and Indexing SQLite
date: 2023-10-19 13:54:03
tags: linux
---

What a difference a couple of lines of code can make. 

I recognize that databases have always been a weak point for me, so I've been trying to correct that lately. I have a lot of experience with management of the database engines, failover, filesystems, and networking, but too little working with the internals of the databases themselves. Early this morning I decided I didn't know enough about how database indexes worked. So I did some reading, got to the point where I had a good mental model for them, and decided I'd like to do some testing myself. I figured 40 million records was a nice round number, so I used [fakedata](https://github.com/lucapette/fakedata) to generate 40 million SQL inserts that looked something like this:

```
INSERT INTO contacts (name,email,country) VALUES ("Milo Morris","pmeissner@test.tienda","Italy");
INSERT INTO contacts (name,email,country) VALUES ("Hosea Burgess","kolage@example.walmart","Dominica");
INSERT INTO contacts (name,email,country) VALUES ("Adaline Frank","shaneIxD@example.talk","Slovenia");
```

I saved this as fakedata.sql and piped it into `sqlite3` and figured I'd just let it run in the background. After about *six hours* I realized this was taking a ridiculously long time, and I estimated I'd only loaded about a quarter of the data. I believe that's because SQLite was treating each `INSERT` as a separate *transaction*. 

A transaction in SQLite is a unit of work. SQLite ensures that the write to the database is Atomic, Consistent, Isolated, and Durable, which means that for each of the 40 million lines I was piping into `sqlite3`, the engine was ensuring that every line was fully committed to the database before moving on to the next line. That's a lot of work for a very, very small amount of data. So, I did some more reading and found one recommendation of explicitly wrapping the entire load into a single transaction, so my file now looked like:

```
BEGIN TRANSACTION;

INSERT INTO contacts (name,email,country) VALUES ("Milo Morris","pmeissner@test.tienda","Italy");
INSERT INTO contacts (name,email,country) VALUES ("Hosea Burgess","kolage@example.walmart","Dominica");
INSERT INTO contacts (name,email,country) VALUES ("Adaline Frank","shaneIxD@example.talk","Slovenia");

COMMIT;
```

I set a timer and ran the import again:

```
➜  var time cat fakedata.sql| sqlite3 test.db
cat fakedata.sql  0.07s user 0.90s system 1% cpu 1:13.66 total
sqlite3 test.db  70.81s user 2.19s system 98% cpu 1:13.79 total
```

So, that went from 6+ hours to about 71 seconds. And I imagine if I did some more optimization (possibly using the Write Ahead Log?) I might be able to get that import faster still. But a little over a minute is good enough for some local curiosity testing. 

## Indexes

So… back to indexes. 

Indexing is a way of sorting a number of records on multiple fields. Creating an index on a field in a table creates another data structure that holds the field values and a pointer to the record it relates to. Once the index is created it is sorted. This allows binary searches to be performed on the new data structure. 

One good analogy is the index of a physical book. Imagine that a book has ten chapters and each chapter has 100 pages. Now imagine you’d like to find all instances of the word “continuum” in the book. If the book doesn’t have an index, you’d have to read through every page in every chapter to find the word. 

However, if the book is already indexed, you can find the word in the alphabetical list, which will then have a pointer to the page numbers where the word can be found. 

The downside to the index is that it does take additional space. In the book analogy, while the book itself is 1000 pages, we’d need another ten or so for the index, bringing up the total size to 1010 pages. Same with a database, the additional index data structure requires more space to hold both the original data field being indexed, and a small (4-byte, for example) pointer to the record. 



Oh, and the results of creating the index are below. 

```
SELECT * from contacts WHERE name is 'Hank Perry';
Run Time: real 2.124 user 1.771679 sys 0.322396


CREATE INDEX IF NOT EXISTS name_index on contacts (name);
Run Time: real 22.129 user 16.048308 sys 2.274184


SELECT * from contacts WHERE name is 'Hank Perry';
Run Time: real 0.003 user 0.001287 sys 0.001598

```

That's a massive improvement. And now I know a little more than I did.
