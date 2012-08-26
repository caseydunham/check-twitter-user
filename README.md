## check-twitter-user: Check if a twitter screen name is available [![endorse](http://api.coderwall.com/caseydunham/endorse.png)](http://coderwall.com/caseydunham)

This uses the same endpoint (HTTPS) that the web based Twitter signup form uses to determine if a user name is available or not.

Can pass a single username to check via the command line

usage:

    usage: check-twitter-user [-h] username

    positional arguments:
      username    name to check for

    optional arguments:
      -h, --help  show this help message and exit



todo:

 * check for proper twitter username format before api call
 * read names to check from a file


Authors: Casey Dunham <casey.dunham@gmail.com>

Version: 0.1