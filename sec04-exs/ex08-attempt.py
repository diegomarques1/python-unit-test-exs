# References
# https://www.w3schools.com/python/ref_string_lstrip.asp
# https://www.w3schools.com/python/ref_string_rstrip.asp

import unittest

class TestLstripMethod(unittest.TestCase):
    def test_lstrip_by_default(self):
        self.assertEqual('  diego  '.lstrip(), 'diego  ')
        
    def test_lstrip_by_set(self):
        self.assertEqual('.xyABCxy.'.lstrip(".xy"), 'ABCxy.')

class TestStripMethod(unittest.TestCase):
    def test_strip_by_default(self):
        self.assertEqual('  diego  '.strip(), 'diego')
    
    def test_strip_by_set(self):
        self.assertEqual('.xyABCxy.'.strip(".xy"), 'ABC')

class TestRstripMethod(unittest.TestCase):
    def test_rstrip_by_default(self):
        self.assertEqual('  diego  '.rstrip(), '  diego')
    
    def test_rstrip_by_set(self):
        self.assertEqual('.xyABCxy.'.rstrip(".xy"), '.xyABC')

# enter your solution here
if __name__ == '__main__':
    unittest.main()