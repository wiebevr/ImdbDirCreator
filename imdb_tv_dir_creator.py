#!/usr/bin/python2
# USAGE: imdb_tv_dir_creator.py <Link to imdb page> <Season number>
from urllib import FancyURLopener
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import os
import sys
import re



url = sys.argv[1]
season = sys.argv[2]

class UrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101230 Firefox/3.6.13'

urlopener = UrlOpener()

soup = BeautifulSoup(urlopener.open(url).read(), smartQuotesTo=None)

regEx = re.compile('Season \\d, Episode (\d+):')
names = []
for name in soup.findAll('h3'):
    if re.search('Season %c, Episode ' % (season), name.text):
        tmp = regEx.sub(r'E\1 - ', name.text)
        names.append(tmp)

for name in names:
    print name
    os.mkdir(name)
