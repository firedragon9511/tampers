#!/usr/bin/env python

import urllib
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
	return payload.replace("'","\"")
