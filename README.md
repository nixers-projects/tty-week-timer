The TTY week timer
------------------

This repo will host the program that will be used during the tty-only week at nixers.net.


### Requirements ###

* It has a daemon interface and a client
* The client displays the time left
* The daemon automatically kills all X sessions
* The daemon checks an online timer/or local, once it expires it displays "END!" and the daemon is automatically stopped
* An admin can set the online timer
