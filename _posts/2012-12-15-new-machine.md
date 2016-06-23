---
layout: post
title: A New Machine
---

I recently got a new home computer - my first Mac.  As with any new machine, it takes a while to set it up just as you like it.  Here are some of the basics that I started off with.

#### iTunes

All our music is stored on a remote disk and I want it to stay there so before importing into iTunes, I unchecked the 'Copy files to iTunes when importing' in Preferences/Advanced.

In my existing iTunes, I saved playlists as XML, mail them over and imported the playlists into the new machine.

#### DVD Sharing

Since my machine lacks an optical drive, I enabled DVD sharing on my wife's iMac in System Preferences/Sharing.

#### App Store

It seemed to be random whether an app I wanted was in the App Store or came direct from a company's website but here's what I found.

* XCode (Apple)
* Evernote - I'm experimenting with using Evernote to maintain notes on how I configure all the machines I use. (I may use Zim instead)
* Pocket - previously ReadItLater - save web pages for later reading. (I may use Instapaper instead)
* Caffeine - temporarily disable the screensaver while watching movies, etc.
* Twitter - I really feel I should use this more - but never do

#### Miscellaneous Apps

A lot of what I wanted came from websites

* Dropbox - shared web-accessible disk
* [Google Drive][1] - shared web-accessible disk with spreadsheets, text editors, etc.  
* [Skype][2] - free internet chatting  
* [Adium][3] - instant messaging clients that works with almost everything (but I don't IM much)  
* [Google Earth][4]
* [Skim][5] - PDF reader with annotation ability
* [MacPorts][6]
Install XCode (App Store), enable command line toolsInstall XQuartz https://xquartz.macosforge.orgInstall mac ports package from http://www.macports.org/install.php
* [Zim][7] - Desktop wiki (better formatting options then Evernote, no sharing between machines - I may use Evernote instead)
    * This required a bit of setup
sudo port install py27-gtk py27-xdg py27-simplejson  
cd Downloads/zim-0.57  
sudo ./setup.py install  
zim
    * This hasn't been working very well for me because it uses Linux conventions (e.g., ctrl-C not cmd-C to copy)

[1]: https://www.google.com/intl/en/drive/start/download.html
[2]: http://beta.skype.com/en/download-skype/skype-for-computer/
[3]: http://adium.im
[4]: http://www.google.co.uk/intl/en_uk/earth/download/ge/agree.html
[5]: http://sourceforge.net/projects/skim-app/files/Skim/Skim-1.3.22/Skim-1.3.22.dmg/download
[6]: http://www.macports.org
[7]: http://zim-wiki.org/downloads.html
