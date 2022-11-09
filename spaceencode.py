#!/usr/bin/env python

from lib.core.enums import PRIORITY
__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
	return result.replace(' ', '%20')
