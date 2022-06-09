---
layout: post
title: GPG Signing Git Commits
date: 2022-06-09 10:54:51
tags: security
---

On my way towards completing another project I needed to setup `gpg` public key infrastructure. There are many tutorials and explanations about gpg on the web, so I won't try to explain what it is here. My goal is to simply record how I went about setting it up for myself to securely sign my Git commits. 

Most everything here I gathered from [this tutorial](https://dev.to/benjaminblack/signing-git-commits-with-modern-encryption-1koh) on `dev.to`, but since I'm sure I'll never be able to find it again after today, I'm going to document it here. 

First, install gpg with Homebrew:

```
brew install gpg
```

Next, generate a new Ed25519 key:

```
gpg --full-generate-key --expert
```

We pick option (9) for the first prompt, Elliptic Curve Cryptography, and option (1) for the second, Curve 25519. Pick the defaults for the rest of the prompts, giving the key a descriptive name. 

Once finished you should be able to see your key by running:

```
gpg --list-keys --keyid-format short
```

The tutorial recommends using a second subkey generated from the first key to actually do the signing. So, we edit the master key by running:

```
gpg --expert --edit-key XXXXXXX
```

Replacing XXXXX with the ID of your newly generated key. Once in the gpg command line, enter `addkey`, and again select ECC and Curve 25519 for the options. Finally, enter `save` to save the key and exit the command line.

Now when we run `gpg --list-keys --keyid-format short` we should be able to see a second key listed with the designation `[S]` after it. The ID will look similar to this:

```
sub   ed25519/599D272D 2021-01-02 [S]
```

We will need the part after `ed25519/`, in this case `599D272D`. Add that to your global Git configuration file by running:

```
git config --global user.signingkey 599D272D
```

If you'd like `git` to sign every commit, you can add this to your config file:

```
git config --global commit.gpgsign true
```

Otherwise, pass the `-S` flag to your `git` command to sign individual commits. I'd never remember to do that, so I just sign all of them. 

Make sure that gpg is unlocked and ready to use by running:

```
echo "test"  | gpg --clearsign
```

If that fails, run `export GPG_TTY=$(tty)` and try again. You should be prompted to unlock GPG with the passphrase set during creation of the key. Enter the export command in your `~/.zshrc` to fix this issue.

Finally, Github has a simple way to add gpg keys, but first we'll need to export the public key:

```
gpg --armor --export 599D272D
```

Copy the entire output of that command and enter it into the Github console under Settings, "SSH and GPG keys", and click on "New GPG key". Once that's finished, you should start seeing nice green "Verified" icons next to your commits. 

