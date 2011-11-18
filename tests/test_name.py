# -*- coding: utf-8 -*-

import os
import unittest

from nose.tools import *

from name import Name, count_kakusuu


class NameTest(unittest.TestCase):

    def test_contains(self):
        n1 = Name('foo bar')
        n2 = Name('foo\tbaz')
        n3 = Name('foo bar')
        n4 = Name(u'あき あき')

        assert_equal(n1.name, 'foo')
        assert_equal(n1.furigana, 'bar')
        assert_equal(n2.name, 'foo')
        assert_equal(n2.furigana, 'baz')

        assert_equal(n1, n3)

        s = set( ['1', '2'] )
        s = set( [n1, n2, n3] )
        assert_equal(s, set( (n1, n2) ) )

        assert_equal(n4.kakusu(), 7)
        assert_equal(n4.kakusu_at(0), 3)
        assert_equal(n4.kakusu_at(1), 4)


    def test_countkakusu(self):
        assert_equal(count_kakusu(u'あ'), 3)
        assert_equal(count_kakusu(u'わ'), 3)
        assert_equal(count_kakusu(u'あわ'), 6)
        assert_equal(count_kakusu(u'狂'), 7)
        assert_raises(ValueError, count_kakusu, u'薔')