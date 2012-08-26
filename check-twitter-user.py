"""
Copyright (c) 2012 Casey Dunham <casey.dunham@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__author__ = 'Casey Dunham <casey.dunham@gmail.com>'
__version__ = '0.1'

import argparse
import urllib2
import json
import sys

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'
URL_TEMPLATE = 'https://www.twitter.com/users/username_available?suggest=1&username=%s&full_name=&email=&suggest_on_username=true&context=front&custom=1'

def check_name(screen_name):
    url = URL_TEMPLATE % screen_name

    req = urllib2.Request(url)

    """
        Response will be in the form

        {"desc":"Available!","reason":"available","msg":"Available!","valid":true,"suggestions":[]}
        {"suggestions":[],"desc":"That username has been taken. Please choose another.","reason":"taken","msg":"Username has already been taken","valid":false}
    """
    try:
        json_res = urllib2.urlopen(req).read()
        resp = json.loads(json_res)
        return resp["reason"]
    except urllib2.HTTPError, e:
        return "error: %s" % (e.code,)

def print_result(screen_name, msg):
    display = "[%s] %s %s"
    if "available" in msg:
        sys.stdout.write(display % ("+", screen_name, msg,))
    elif "error" in msg:
        sys.stdout.write(display % ("!", screen_name, msg))
    else:
        sys.stdout.write(display % ("-", screen_name, msg))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="check-twitter-user")
    parser.add_argument('username', help="name to check for")
    args = parser.parse_args()

    screen_name = args.username

    msg = check_name(screen_name)
    print_result(screen_name, msg)