-*- mode: org -*-
#+title: Gnome-Connection-Manager

Get the latest version here:
https://github.com/seppeljordan/gcm/tree/stable

* REQUIREMENTS:
  you must have python 2.6 or later, python-gtk2, expect, python-vte, libglade2-0, python-glade2
* INSTALLATION:
  - Linux/Unix :: copy the gcm files wherever you want, then execute
                  the gnome_connection_manager.py example:
                  /home/someuser/gcm/gnome_connection_manager.py
  - FreeBSD :: Edit the file gnome_connection_manager.py and use the
               full path of the "ssh" and "telnet" binaries in the
               lines:
    * SSH_BIN = 'ssh'
    * TEL_BIN = 'telnet'
    * Edit the file ssh.expect and replace the first line with the
      full path of the "expect" command: #!/usr/bin/expect
** Arch Linux
   You can install the following packages to make
   gnome-terminal-manager running:
   * pygtk
   * expect
   * vte
   * python2

* LANGUAGE: 
  to force a language start the application with this command: 
  LANGUAGE=en /home/someuser/gcm/gnome_connection_manager.py 
  if that doesn't work, try with: 
  env LANGUAGE=en python2 /home/someuser/gcm/gnome_connection_manager.py
