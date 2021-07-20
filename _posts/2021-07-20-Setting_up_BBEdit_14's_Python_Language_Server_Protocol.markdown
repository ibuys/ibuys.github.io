---
layout: post
title: Setting up BBEdit 14's Python Language Server Protocol
date: 2021-07-20 08:11:15
tags: python unix
---

Bare Bones released the new version of BBEdit recently and it's packed with features that teach the old dog some modern IDE tricks. When programming I mainly work in Python these days, so I obviously wanted to take advantage of BBEdit's new Langage Server Protocol support. This lets BBEdit start a daemon for you in the background that you install separately, and the daemon takes care of things like code completion, error highlighting, and documentation. However, how to set this up specifically for Python development was unclear.

First, and you've probably already got this setup, install `python3` with Homebrew and use it to install a virtual environment.

```
brew install python3
python3 -m venv ~/Unix/env/lsp
```

Next, activate the new virtual environment and install the Jedi Language Server. Once installed, copy the full path to the executable:

```
source ~/Unix/env/lsp/bin/activate 
pip install -U jedi-language-server
which jedi-language-server | pbcopy
```

Finally, open the preferences for BBEdit, find the Languages section, and towards the botton add a Language-specific setting for Python. Under the Server tab, make sure you've checked the box to "Enable language server", and paste the path copied from the previous command.

![bbedit-python-lsp-prefs](../media/bbedit-python-lsp-prefs.png, "bbedit-python-lsp-prefs")

If BBEdit finds the executable at the path, there will be a green dot at the bottom labeled "Ready to start server". Otherwise, you'll see a red dot that says "absolute command path not found". If you see that make sure the commands above completed successfully. 

Now, whenever you open a Python file BBEdit will automatically start the LSP daemon in the background and start working it's magic.
