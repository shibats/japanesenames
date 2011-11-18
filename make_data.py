#!/usr/bin/env python

from scrapers import scraper1, scraper2

# This is a script to make japanese name data.
#
# This module calls scraping function to retrieve names from website etc. .
# Each module must have scrape(gender) function.
# scrape() takes gender argument (0: boy, 1:girl),
# returns a list of retrieved names,
# which contains paris of kanji, furigana conbined by '\t'.
#
# The scrape() function should wait while every time after reading a resource.


# making the unique list of boys name

s1 = set(scraper1.scrape(0))
s2 = set(scraper2.scrape(0))

s1.update(s2)
f = open('./data/bname.tsv', 'w')
f.write('\n'.join(s1))


# making the unique list of girls name

s1 = set(scraper1.scrape(1))
s2 = set(scraper2.scrape(1))

s1.update(s2)
f = open('./data/gname.tsv', 'w')
f.write('\n'.join(s1))
