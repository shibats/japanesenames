# -*- coding: utf-8 -*-

import os
import unittest

from nose.tools import *

from collection import CollectionBase
from name import Name

class QueryBaseTest(unittest.TestCase):

    def test_contains(self):
        q = CollectionBase()
        q.FILENAME = './tests/testnames.tsv'

        q.contains('a')
        assert_equal(list(q), [Name('abc\tcde'), Name('almn\topq')])

        q.patterns = []
        q.contains('ab')
        assert_equal(list(q), [Name('abc\tcde')])

        q.patterns = []
        q.contains('a', 'b')
        assert_equal(list(q), [Name('abc\tcde')])

        q.patterns = []
        q.contains('1')
        assert_equal(list(q), [])

        q.patterns = []
        q.contains('a', '1')
        assert_equal(list(q), [])


    def test_contains_in_furigana(self):
        q = CollectionBase()
        q.FILENAME = './tests/testnames.tsv'

        q.patterns = []
        q.contains_in_furigana('c')
        assert_equal(list(q), [Name('abc\tcde'), Name('rst\tcuvw')])

        q.patterns = []
        q.contains_in_furigana('ij')
        assert_equal(list(q), [Name('fgh\tijk')])

        q.patterns = []
        q.contains_in_furigana('c', 'v')
        assert_equal(list(q), [Name('rst\tcuvw')])

