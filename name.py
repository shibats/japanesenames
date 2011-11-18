# -*- coding: utf-8 -*-
#
# query.py
# A class that represents a single name. They can be contents of set object.
#
# Copyright 2011 Atsushi Shibata
#
"""
A class that represents a single name. They can be contents of set object.

$Id: forms.py 649 2010-08-16 07:44:47Z ats $
"""

__author__  = 'Atsushi Shibata <shibata@webcore.co.jp>'
__docformat__ = 'plaintext'
__licence__ = 'MIT'

import codecs

class Name:
    """
    A class that represents a single name. They can be contents of set object.
    """
    BOY = 1
    GIRL = 2

    def __init__(self, line='', name='', furigana='', gender=BOY):
        """
        A initialization function, gives a line of the file and split it to
            name and furigana.
        """
        if line:
            self.name, self.furigana = line.split()
        elif name and furigana:
            self.name = name
            self.furigana = furigana
        self.gender = gender
        self._origline = line


    def __hash__(self):
        """
        A special method to return hash of the object.
        """
        return hash(self._origline)


    def __eq__(self, dest):
        """
        A special method to compare two objects.
        """
        return bool(dest._origline == self._origline)


    def __repr__(self):
        """
        A method to return repr string.
        """
        return "Name(name=u'%s', furigana=u'%s')" % (self.name, self.furigana)


    def kakusu(self):
        """
        A method to count kakusuu of the name.
        """
        return count_kakusuu(self.name)


    def kakusu_at(self, index):
        """
        A method to count kakusuu of one character at given index.
        """
        return count_kakusuu(self.name[index])


    def is_boy(self):
        """
        A method to return boolean value to determin the name is of boys.
        """
        if self.gneder == self.BOY: return True;


    def is_girl(self):
        """
        A method to return boolean value to determin the name is of girls.
        """
        if self.gneder == self.GIRL: return True;


# kakusu counter

kf = codecs.open('data/kakusu.tsv', 'r', 'utf-8')
kdic = {}

for line in kf:
    line = line.replace('\n', '')
    numstr, c = line.split()
    try:
        kdic[c] = int(numstr)
    except:
        print line

def count_kakusu(chars):
    """
    A method to count kakusu of given characters.
    """
    cnt = 0
    for letter in chars:
        if letter in kdic:
            cnt += kdic[letter]
        else:
            raise ValueError( ('One of the given character (%s)'
                               'is not included in allowed kanji of naming') % \
                               letter )
    return cnt

