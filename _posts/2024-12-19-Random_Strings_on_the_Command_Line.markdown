---
layout: post
title: Random Strings on the Command Line
date: 2024-12-19 15:41:23
tags: shell, linux, unix, macos
---

Browsing through some old files today I came across this note:

```
To Generate A Random String:

tr -dc A-Za-z0-9_ < /dev/urandom | head -c 8 | xargs

```
Curios if it still worked I pasted it into my terminal and, unsurprisingly, was met with an error: 

```
tr: Illegal byte sequence
```

The `tr` utility is one of the many old-school Unix programs with history reaching way back to System V. It stands for "translate characters", and with the `-dc` flags on, it should have ignored all input except for alphabet characters A-Z, both upper and lower case, and the integers 0 through 9, and the underscore character. The "Illegal byte sequence" error means it was really not happy with the input it was getting from `/dev/urandom`. 

On macOS, the pseudo-device `/dev/urandom` is, according to the man page, "a compatibility nod to Linux". The device generates random bytes, so if we read it we'll get back raw binary data that looks like:

```
00010101 01011001 10111101
```

The reason the command is not working like it used to is because most modern computing system expect text character encoding to be UTF-8. When `tr` gets the string of random bytes from `/dev/urandom`, it expects the bytes to be in a specific sequence that it can translate into printable characters on the screen. Since we are intentionally generating random bytes though, we might get a few characters that translate properly, but eventually we'll encounter the "illegal byte sequence" error above. 

To fix the problem, all we need to do is set `LC_ALL=C` before running `tr`:

```
LC_ALL=C tr -dc A-Za-z0-9_ < /dev/urandom | head -c 14 | xargs
```

Setting `LC_ALL=C` sets the language setting back to POSIX, or the original C ASCII encoding for text. That means when `tr` is fed a random string of bytes, it interprets each byte as a character, according to the ASCII table, which looks something like this:

| Character | ASCII Decimal | ASCII Hexadecimal | Binary Representation |
|-----------|---------------|-------------------|-----------------------|
| A         | 65            | 41                | 01000001              |
| B         | 66            | 42                | 01000010              |
| C         | 67            | 43                | 01000011              |

Now each byte is interpreted as a character that matches the list passed as an argument to `tr`. 

```
➜ LC_ALL=C tr -dc A-Za-z0-9_ < /dev/urandom | head -c 14 | xargs

Rhac_WGis7tHzS
```

So, to break down each command in the pipeline:

- `tr`: filters out all characters except those in the sets A-Z, a-z, 0-9, and `_`
- `head -c 14`: displays the first 14 characters of the input from `tr`
- `xargs`: adds a nice newline character at the end of the string, so it's easy to copy. 

This command could be easily adopted to use `base64` instead of `tr` without setting `LC_ALL=C` if you wanted more random characters in the string:

```
base64 < /dev/random | head -c 14 | xargs
```

Expanding `head -c` to 34 or so makes for a nice password generator. 

In fact, I've aliased this to `pgen` in my `.zshrc`:

```
pgen()
{
    base64 < /dev/random | head -c 32 | xargs
}
```

There's almost certainly easier ways to generate a random string in the shell, but I like this, and it works for me. 


---

> Update: The good Dr. Drang suggested ending the pipeline and running `echo` instead of `xargs` for clairity, which makes a lot of sense to me. I updated the alias to `base64 < /dev/random | head -c 32; echo`.