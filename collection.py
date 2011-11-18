# -*- coding: utf-8 -*-
#
# collection.py
# A collection class of japanese name.
#
# Copyright 2011 Atsushi Shibata
#
"""
A collection class of japanese name.

$Id: forms.py 649 2010-08-16 07:44:47Z ats $
"""

__author__  = 'Atsushi Shibata <shibata@webcore.co.jp>'
__docformat__ = 'plaintext'
__licence__ = 'MIT'

import re
import codecs
from name import Name

class CollectionBase:
    """
    """
    GENDER = Name.BOY

    FILENAME = ''

    def __init__(self, contains=[], contains_in_furigana=[]):
        """
        Initialize function.
        """
        self.patterns = []
        if contains:
            self.contains(contains)
        if contains_in_furigana:
            self.contains_in_furigana(contains_in_furigana)


    def contains(self, *qlist):
        """
        a method to filter results only with given letters.
        """

        for i in qlist:
            self.patterns.append('^.*?%s.*?\s' % i)


    def contains_in_furigana(self, *qlist):
        """
        a method to filter results only with given letters.
        """

        for i in qlist:
            self.patterns.append('^.+?\s.*?%s.*?' % i)


    def __iter__(self):
        """
        A special method to returns iterator of the result.
        """
        f = codecs.open(self.FILENAME, 'r', 'utf-8')
        for line in f:
            go = True
            for pat in self.patterns:
                if not re.findall(pat, line):
                    go = False
                    break
            if go:
                yield Name(line = line.replace('\n', ''), gender=self.GENDER)


class BoysNameCollection(CollectionBase):
    FILENAME = 'data/bname.tsv'
    GENDER = Name.BOY


class GirlsNameCollection(CollectionBase):
    FILENAME = 'data/gname.tsv'
    GENDER = Name.GIRL


