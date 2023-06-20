# use pytest to make sure and test that the shorten function from twttr.py returns what it is supposed to
from twttr import shorten

def test_shorten():
    assert shorten('apple') == 'ppl'
    assert shorten('CENTRAL') == 'cntrl'
    assert shorten('twttr') == 'twttr'
    assert shorten('flOrIdA') == 'flrd'
    assert shorten('foo bar baz') == 'f br bz'