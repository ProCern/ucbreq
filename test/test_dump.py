from __future__ import division, absolute_import, print_function

import unittest

import req
from collections import OrderedDict

class DumpTest(unittest.TestCase):
    def test_dumps_default(self):
        d = OrderedDict()
        d['foo'] = 'bar'
        d['baz'] = ('alpha', 'beta', 'gamma')
        d['delta'] = 'eins'
        d['zwei'] = ('drei', 'vier')
        self.assertEqual(req.dumps(d), "foo|bar\nbaz_1|alpha\nbaz_2|beta\nbaz_3|gamma\ndelta|eins\nzwei_1|drei\nzwei_2|vier\n")
        self.assertEqual(req.dumps(d, startindex=5), "foo|bar\nbaz_5|alpha\nbaz_6|beta\nbaz_7|gamma\ndelta|eins\nzwei_5|drei\nzwei_6|vier\n")
        self.assertEqual(req.dumps(d, separator='='), "foo=bar\nbaz_1=alpha\nbaz_2=beta\nbaz_3=gamma\ndelta=eins\nzwei_1=drei\nzwei_2=vier\n")
        self.assertEqual(req.dumps(d, index_separator=','), "foo|bar\nbaz,1|alpha\nbaz,2|beta\nbaz,3|gamma\ndelta|eins\nzwei,1|drei\nzwei,2|vier\n")

        with self.assertRaises(ValueError):
            req.dumps(d, startindex=-1)

    def test_dumps_bytes(self):
        d = OrderedDict()
        d[b'foo'] = b'bar'
        d[b'baz'] = (b'alpha', b'beta', b'gamma')
        d[b'delta'] = b'eins'
        d[b'zwei'] = (b'drei', b'vier')
        self.assertEqual(req.dumps(d), b"foo|bar\nbaz_1|alpha\nbaz_2|beta\nbaz_3|gamma\ndelta|eins\nzwei_1|drei\nzwei_2|vier\n")
        self.assertEqual(req.dumps(d, startindex=5), b"foo|bar\nbaz_5|alpha\nbaz_6|beta\nbaz_7|gamma\ndelta|eins\nzwei_5|drei\nzwei_6|vier\n")
        self.assertEqual(req.dumps(d, separator=b'='), b"foo=bar\nbaz_1=alpha\nbaz_2=beta\nbaz_3=gamma\ndelta=eins\nzwei_1=drei\nzwei_2=vier\n")
        self.assertEqual(req.dumps(d, index_separator=b','), b"foo|bar\nbaz,1|alpha\nbaz,2|beta\nbaz,3|gamma\ndelta|eins\nzwei,1|drei\nzwei,2|vier\n")

        with self.assertRaises(ValueError):
            req.dumps(d, startindex=-1)

    def test_dumps_unicode(self):
        d = OrderedDict()
        d[u'foo'] = u'bar'
        d[u'baz'] = (u'alpha', u'beta', u'gamma')
        d[u'delta'] = u'eins'
        d[u'zwei'] = (u'drei', u'vier')
        self.assertEqual(req.dumps(d), u"foo|bar\nbaz_1|alpha\nbaz_2|beta\nbaz_3|gamma\ndelta|eins\nzwei_1|drei\nzwei_2|vier\n")
        self.assertEqual(req.dumps(d, startindex=5), u"foo|bar\nbaz_5|alpha\nbaz_6|beta\nbaz_7|gamma\ndelta|eins\nzwei_5|drei\nzwei_6|vier\n")
        self.assertEqual(req.dumps(d, separator=u'='), u"foo=bar\nbaz_1=alpha\nbaz_2=beta\nbaz_3=gamma\ndelta=eins\nzwei_1=drei\nzwei_2=vier\n")
        self.assertEqual(req.dumps(d, index_separator=u','), u"foo|bar\nbaz,1|alpha\nbaz,2|beta\nbaz,3|gamma\ndelta|eins\nzwei,1|drei\nzwei,2|vier\n")

        with self.assertRaises(ValueError):
            req.dumps(d, startindex=-1)
