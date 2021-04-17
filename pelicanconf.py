#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from distutils.sysconfig import get_python_lib

AUTHOR = 'Rexu'
SITENAME = "On a Wooden Block"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('email: rexu@onawoodenblock.com', 'mailto:rexu@onawoodenblock.com'),)

# Social widget
# SOCIAL = (('Instagram (mostly pottery)', 'https://www.instagram.com/kvazhir/'),)

# Better not, not into showing myself.
# GITHUB_URL = 'https://github.com/qtov'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

# Plugins
PLUGIN_PATHS = ['/venv/Lib/site-packages', get_python_lib()]
PLUGINS = [
    'pelican_image_process',
]
