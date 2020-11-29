#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_makedepends(['git'])

def post_build():
    aur_post_build()
