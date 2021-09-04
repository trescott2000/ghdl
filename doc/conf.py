# -*- coding: utf-8 -*-
import sys, re
from os.path import abspath
from pathlib import Path
from json import loads


project = u'GHDL'
copyright = u'2002-2021, Tristan Gingold and contributors'
author = u'Tristan Gingold and contributors'

release = 'moved to GitHub Pages'

master_doc = 'index'

source_suffix = {'.rst': 'restructuredtext',}

exclude_patterns = [
	"_build",
	"_theme",
	"Thumbs.db",
	".DS_Store"
]
