#!/usr/bin/env python

from scrapers import scraper1, scraper2, scraper3

# This is a script to make japanese name data.
#
# This module calls scraping function to retrieve names from website etc. .
# Each module must have scrape(gender) function.
# scrape() takes gender argument (0: boy, 1:girl),
# returns a list of retrieved names,
# which contains paris of kanji, furigana conbined by '\t'.
#
# The scrape() function should wait while every time after reading a resource.

# reading kakusuu data to make dictionary.

import codecs

kd = {}
f = codecs.open('./data/kakusu.tsv', 'r', 'utf-8')
for line in f:
    l = line.split()
    if len(l) >= 2:
        kd[l[1]] = 1


# making the unique list of boys name

s1 = set(scraper1.scrape(0))
s2 = set(scraper2.scrape(0))
s3 = set(scraper3.scrape(0))

s1.update(s2)
s1.update(s3)

# sort, validate
bl = [x for x in list(s1) if len(x.split()) >= 2]
bl.sort(lambda x, y: cmp(x.split()[1], y.split()[1]))
for i in bl:
    if not [x for x in i.split()[0] if x in kd]:
        bl.remove(i)

f = open('./data/bname.tsv', 'w')
f.write('\n'.join(bl))


# making the unique list of girls name

s1 = set(scraper1.scrape(1))
s2 = set(scraper2.scrape(1))
s3 = set(scraper3.scrape(1))

s1.update(s2)
s1.update(s3)

# sort, validate
gl = [x for x in list(s1) if len(x.split()) >= 2]
gl.sort(lambda x, y: cmp(x.split()[1], y.split()[1]))
for i in gl:
    if not [x for x in i.split()[0] if x in kd]:
        gl.remove(i)

f = open('./data/gname.tsv', 'w')
f.write('\n'.join(gl))
