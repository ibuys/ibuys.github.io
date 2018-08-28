---
layout: post
title: Simple File Encryption for macOS
date: 2018-08-28 12:44:22
tags: 
---

For years now I’ve wanted a simple way to encrypt or decrypt a file in macOS, so this morning I built it. This takes five to ten minutes to setup, and provides the encryption service as a right-click menu item and a pair of folders with folder actions enabled. Here’s what I did. 

First, I installed the command line utility `ccrypt` with Homebrew: `brew install ccrypt`.

Next, I added a hidden config file containing my secret key in `~/.ccrypt` and saved the key to 1Password. 

Then, I created two new services in Automator with a single action of “Run Shell Script. The services accept files or folders in Finder, and have the “Pass input: “ setting of the Run Shell Script action set to “as arguments”.  The  Encrypt File service looks like this:

```bash
EXTEN="cpt"

for FILENAME in "$@"
do
	if test "${FILENAME#*$EXTEN}" != "$FILENAME"
	then
		echo "Already encrypted."
	else
		/usr/local/bin/ccencrypt -k ~/.ccrypt $FILENAME
	fi

done

```

And the Decrypt File service is only slightly different: 

```bash
EXTEN="cpt"

for FILENAME in "$@"
do
	if test "${FILENAME#*$EXTEN}" != "$FILENAME"
	then
		/usr/local/bin/ccdecrypt -k ~/.ccrypt $FILENAME
	else
		echo "Already decrypted."
	fi

done

```

The first line in the script sets the EXTEN variable to “cpt”, which is what the `ccrypt` executable adds as a file extension when it encrypts a file. Next I setup a for loop to cycle through all of the selected files, and then do a test to see if the file being looked at already has the “cpt” extension or not. This is especially important when setting up a folder action, because when the file is encrypted it will drop in as a new file in the folder, which will then attempt to encrypt it again unless this check is preset. 

After saving these two Automator services you should be able to right click on any file in the Finder and encrypt it, and then the same again to decrypt. I’ve also added the two scripts as folder actions to two folders name “Encrypted” and “Decrypted”, so if I’d rather move and encrypt the files, I can just drag and drop them on the folders. 

All in all, this gives me a little more peace of mind about saving files in iCloud and syncing them between my two Macs. They won’t be available in iOS, but for the types of files I need on both machines, that’s not a problem. 