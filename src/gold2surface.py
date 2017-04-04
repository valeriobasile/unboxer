#!/usr/bin/env python
"""Usage: gold2surface.py [-vc]

Reads a gold standard DRG from the standard input and generates its
corresponding surface form.

Options:
  -h --help
  -v       debug mode
  -c       only generates concepts
"""
from docopt import docopt
import sys
from unboxer.drg2txt import unbox
from unboxer.drg import DRGParser

arguments = docopt(__doc__, version='Naval Fate 2.0')
parser = DRGParser()
parser.parse_tup_lines(sys.stdin.readlines())

print (unbox(parser.drg, debug=arguments['-v'], concepts=arguments['-c']))
