import unittest
import ucbreq
from collections import OrderedDict

class LoadTest(unittest.TestCase):
    def test_loads_default(self):
        d = OrderedDict()
        d['foo'] = 'bar'
        d['baz'] = ['alpha', 'beta', 'gamma']
        d['delta'] = 'eins'
        d['zwei'] = ['drei', 'vier']
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz_5|alpha\nbaz_6|beta\nbaz_7|gamma\ndelta|eins\nzwei_5|drei\nzwei_6|vier\n",
                cls=OrderedDict,
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo=bar\nbaz_1=alpha\nbaz_2=beta\nbaz_3=gamma\ndelta=eins\nzwei_1=drei\nzwei_2=vier\n",
                cls=OrderedDict,
                separator='=',
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz,1|alpha\nbaz,2|beta\nbaz,3|gamma\ndelta|eins\nzwei,1|drei\nzwei,2|vier\n",
                cls=OrderedDict,
                index_separator=',',
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz_1|alpha\ndelta|eins\nbaz_3|gamma\nzwei_1|vier\nbaz_2|beta\nzwei|drei\n",
                cls=OrderedDict,
                ))

    def test_loads_tuple(self):
        d = OrderedDict()
        d['foo'] = 'bar'
        d['baz'] = ('alpha', 'beta', 'gamma')
        d['delta'] = 'eins'
        d['zwei'] = ('drei', 'vier')
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz_5|alpha\nbaz_6|beta\nbaz_7|gamma\ndelta|eins\nzwei_5|drei\nzwei_6|vier\n",
                cls=OrderedDict,
                list_cls=tuple,
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo=bar\nbaz_1=alpha\nbaz_2=beta\nbaz_3=gamma\ndelta=eins\nzwei_1=drei\nzwei_2=vier\n",
                cls=OrderedDict,
                list_cls=tuple,
                separator='=',
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz,1|alpha\nbaz,2|beta\nbaz,3|gamma\ndelta|eins\nzwei,1|drei\nzwei,2|vier\n",
                cls=OrderedDict,
                list_cls=tuple,
                index_separator=',',
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz_1|alpha\ndelta|eins\nbaz_3|gamma\nzwei_1|vier\nbaz_2|beta\nzwei|drei\n",
                cls=OrderedDict,
                list_cls=tuple,
                ))

    def test_loads_set(self):
        d = OrderedDict()
        d['foo'] = 'bar'
        d['baz'] = frozenset({'alpha', 'beta', 'gamma'})
        d['delta'] = 'eins'
        d['zwei'] = frozenset({'drei', 'vier'})
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz_5|alpha\nbaz_6|beta\nbaz_7|gamma\ndelta|eins\nzwei_5|drei\nzwei_6|vier\n",
                cls=OrderedDict,
                list_cls=frozenset,
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo=bar\nbaz_1=alpha\nbaz_2=beta\nbaz_3=gamma\ndelta=eins\nzwei_1=drei\nzwei_2=vier\n",
                cls=OrderedDict,
                list_cls=frozenset,
                separator='=',
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz,1|alpha\nbaz,2|beta\nbaz,3|gamma\ndelta|eins\nzwei,1|drei\nzwei,2|vier\n",
                cls=OrderedDict,
                list_cls=frozenset,
                index_separator=',',
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz_1|alpha\ndelta|eins\nbaz_3|gamma\nzwei_1|vier\nbaz_2|beta\nzwei|drei\n",
                cls=OrderedDict,
                list_cls=frozenset,
                ))

    def test_loads_bytes(self):
        d = OrderedDict()
        d[b'foo'] = b'bar'
        d[b'baz'] = [b'alpha', b'beta', b'gamma']
        d[b'delta'] = b'eins'
        d[b'zwei'] = [b'drei', b'vier']
        self.assertEqual(
            d,
            ucbreq.loads(
                b"foo|bar\nbaz_5|alpha\nbaz_6|beta\nbaz_7|gamma\ndelta|eins\nzwei_5|drei\nzwei_6|vier\n",
                cls=OrderedDict,
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                b"foo=bar\nbaz_1=alpha\nbaz_2=beta\nbaz_3=gamma\ndelta=eins\nzwei_1=drei\nzwei_2=vier\n",
                cls=OrderedDict,
                separator=b'=',
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                b"foo|bar\nbaz,1|alpha\nbaz,2|beta\nbaz,3|gamma\ndelta|eins\nzwei,1|drei\nzwei,2|vier\n",
                cls=OrderedDict,
                index_separator=b',',
                ))

    def test_loads_unicode(self):
        d = OrderedDict()
        d['foo'] = 'bar'
        d['baz'] = ['alpha', 'beta', 'gamma']
        d['delta'] = 'eins'
        d['zwei'] = ['drei', 'vier']
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz_5|alpha\nbaz_6|beta\nbaz_7|gamma\ndelta|eins\nzwei_5|drei\nzwei_6|vier\n",
                cls=OrderedDict,
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo=bar\nbaz_1=alpha\nbaz_2=beta\nbaz_3=gamma\ndelta=eins\nzwei_1=drei\nzwei_2=vier\n",
                cls=OrderedDict,
                separator='=',
                ))
        self.assertEqual(
            d,
            ucbreq.loads(
                "foo|bar\nbaz,1|alpha\nbaz,2|beta\nbaz,3|gamma\ndelta|eins\nzwei,1|drei\nzwei,2|vier\n",
                cls=OrderedDict,
                index_separator=',',
                ))
