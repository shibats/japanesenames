# -*- coding: utf-8 -*-

"""
A test script to perform validation test.
It tests wheather each characters in names are included in
valid character list.
"""

import codecs

# reading kakusuu data and make dictionary.

kd = {}
f = codecs.open('../data/kakusu.tsv', 'r', 'utf-8')
for line in f:
    l = line.split()
    if len(l) >= 2:
        kd[l[1]] = 1

def test(f):
    for line in f:
        l = line.split()
        if len(l) >= 2:
            if not [x for x in l[0] if x in kd]:
                print line


f = codecs.open('../data/bname.tsv', 'r', 'utf-8')
print "test for boys name"
test(f)

f = codecs.open('../data/gname.tsv', 'r', 'utf-8')
print "test for girls name"
test(f)

