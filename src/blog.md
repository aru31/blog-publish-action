---
title: Avoid rm
date: 2021-12-22
description: A small article on why your should avoid using rm in *nix based OS whenever possible.
tags:
  - post
  - linux
devto_series: "Linux"
published: True
---

This article discusses why you should avoid `rm` command in `*nix` based operating systems. It is impossible to prevent it entirely since you will need to delete files/folders from your system. But it is generally a good idea to move the files/folders you want to delete to a recycle bin and then delete them after some time. I will also share the script and modification I used to adopt this setup.

But before diving in those of you unfamiliar with `rm`, it is a command used to remove objects such as files, directories, symbolic links, etc. More precisely, `rm` removes reference/pointer to objects from the filesystem. If you have multiple pointers to the file (hard links), then deleting one of those pointers with `rm` leaves the others completely untouched and the data still available. Deleting all of those links still does not touch the data; however, the OS is now free to reuse the previously reserved blocks for storing that data.

It is important to note that the command works silently, and once you delete your files and folders, you won't be able to get them back. At least easily. You can find various "undelete" utilities. But depending on the filesystem, it can get relatively complex.

So I use a custom script that sends it to a recycle bin instead of deleting anything directly. Depending upon your OS, you may or may not have a recycle bin. If you don't have one, you can always make one.

last line
