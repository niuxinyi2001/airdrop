#def test_copy():
#    assert False


import sys
sys.path.append("..")
import unittest
import computer as pc


class Test_computer(unittest.TestCase):

    def test_upload(self):
        self.assertTrue(pc.upload("bubble","123"))
        self.assertTrue(pc.upload("hh","123"))

    def test_download(self):
        self.assertTrue(pc.download("bubble","123"))
        self.assertTrue(pc.download("hh","123"))

    def test_register(self):
        self.assertTrue(pc.register("red", "123"))
        self.assertTrue(pc.register("pink,"123"))



if __name__ == '__main__':
    unittest.main()