import os
import unittest
import json
import shutil
from PIL import Image
from implace import create_index, create_images
from os.path import abspath, dirname, join as pjoin


here = abspath(dirname(__file__))
tmp = pjoin(here, 'tmp')


class BasicTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not os.path.isdir(tmp):
            os.makedirs(tmp)
        Image.new('L', (100, 100)).save(pjoin(tmp, '1.jpg'), 'JPEG')
        Image.new('L', (200, 200)).save(pjoin(tmp, '2.jpg'), 'JPEG')

    def test_1_create_index(self):
        idx = pjoin(tmp, 'ims.idx')
        create_index(tmp, idx)
        with open(idx) as fp:
            data = json.loads(fp.read())
        self.assertEqual(data['1.jpg'], [100, 100])
        self.assertEqual(data['2.jpg'], [200, 200])

    def test_2_create_images(self):
        idx = pjoin(tmp, 'ims.idx')
        sync = pjoin(tmp, 'sync')
        if not os.path.isdir(sync):
            os.makedirs(sync)
        create_images(sync, idx)
        self.assertTrue(os.path.isfile(pjoin(sync, '1.jpg')))
        self.assertTrue(os.path.isfile(pjoin(sync, '2.jpg')))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(tmp)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(BasicTestCase)

