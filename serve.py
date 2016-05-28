#!/usr/bin/env python

from sys import argv, path
path.append('/home/docxstudios/localpylibs/lib/python2.7/site-packages/')
from src.bot import *
from src.config.config import *

bot = Roboraj(config).run()
