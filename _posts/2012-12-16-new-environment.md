---
layout: post
title: Programming on a Mac
---

What does it take to turn a Mac into a decent programming environment?

I've already installed Xcode from the App store, but I need some editors, compilers and version control.

* [XTerm2][1] - terminal with neat features like replay (scrolling meets TimeMachine!)  
* [Emacs (Aquamacs)][2] - an editor  
* [VIM][3] - another editor (not actually installed yet - will need to build from source)  
* [GitX (Laullon fork)][4] - GUI for GIT distributed version control system
* [HomeBrew][5] - an alternative to Mac Ports (haven't decided which I prefer)
* Scala - programming language
    * brew install scala
    * First time you run 'scala' it installs a JDK
* Haskell - programming language
    * brew install ghc
    * brew install haskell-platform
* ReStructuredText - converts traditionally formatted text files to HTML
    * sudo easy_install pip
    * sudo pip install docutils

[1]: http://www.iterm2.com/#/section/home
[2]: http://sourceforge.net/projects/aquamacs/?source=dlp
[3]: http://www.vim.org/download.php
[4]: http://gitx.laullon.com/
[5]: http://mxcl.github.com/homebrew/
