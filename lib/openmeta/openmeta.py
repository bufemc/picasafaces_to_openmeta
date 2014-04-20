#!/usr/bin/env python
# encoding: utf-8
"""
openmeta.py

wraps the openmeta command line client - http://code.google.com/p/openmeta/ -  to assign metadata to files

Created by dan mackinlay on 2011-01-23.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import os.path
import subprocess
from subprocess import Popen, PIPE
import shlex

def is_openmeta_working():
    """I run these scripts on platforms that don't support openmeta, or don't
    have the binary, or a working binary, or..."""
    try:
        Popen('openmeta', stdout=PIPE, stderr=PIPE
          ).communicate()
        return True
    except OSError:
        return False

def _pathify(filename):
    """openmeta cli has broken path handling. see
    http://code.google.com/p/openmeta/issues/detail?id=14"""
    return os.path.realpath(os.path.join('.', filename))
    
def _run_om_cli_with_path(filename, *extra_args):
    """open meta cli has a slightly off command syntax, with paths after a -p 
    option. this helper soothes using it."""
    #allow the specification of command arguments in the most convenient fashion
    cli_args = ['openmeta']
    cli_args.extend(extra_args)
    cli_args.append('-p')
    cli_args.append(_pathify(filename))
    proc = Popen(
      cli_args,
      stdout=PIPE
    )
    stdout, stderr = proc.communicate()
    return stdout
    
def parse_output(clioutputstring):
    """output may be parsed into tag parts and rating parts, and filename parts.
    Output is not quite sane - filename is always included for one thing.
    Humph."""    
    metadata = {}
    lines = clioutputstring.splitlines()
    tags = shlex.split(lines[1][6:]) #naive split futzes multiword tags
    rating_string = lines[2][8:]
    try:
        rating = float(rating_string)
    except ValueError:
        #ratings of zero are counted as non-existent
        rating = 0
    metadata['tags'] = tags
    metadata['rating'] = rating
    return metadata
    
def get_meta(filename):
    return parse_output(
      _run_om_cli_with_path(filename))

def set_tags(filename, tags):
    _run_om_cli_with_path(filename, '-s', *tags)

    
