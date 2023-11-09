# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"none"


import unittest


from bot import Object


class Obj(Object):

    o = Object()


class TestDetect(unittest.TestCase):

    def test_detect(self):
        o = Obj()
        print(type(o.o))
        self.assertTrue(type(o.o), Object)
