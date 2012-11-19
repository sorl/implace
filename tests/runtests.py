import os
import sys
import unittest
from os.path import abspath, dirname, join as pjoin


def runtests():
    here = abspath(dirname(__file__))
    root = pjoin(here, os.pardir)
    sys.path[0:0] = [ here, root ]
    from implace_tests.tests import suite
    unittest.TextTestRunner(verbosity=2).run(suite())


if __name__ == '__main__':
    runtests()

