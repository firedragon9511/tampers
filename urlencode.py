#!/usr/bin/env python

import urllib

from lib.core.enums import PRIORITY
__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
	result = ""
	for i in payload:
		hx = i.encode('utf-8').hex()
		if len(hx) == 1:
			hx = "0" + hx

		result = result + "%" + hx

	return result
