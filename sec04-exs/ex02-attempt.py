import unittest

class TestJoinMethod(unittest.TestCase):
    def test_join_with_space(self):
        self.assertEqual(' '.join(['Python', '3.8']), 'Python 3.8')
    
    def test_join_with_comma(self):
        self.assertEqual(','.join(['open', 'high', 'low', 'close']), 'open,high,low,close')
        
    def test_join_with_new_line_char(self):
        self.assertEqual('\n'.join(['open', 'high', 'low', 'close']), 'open\nhigh\nlow\nclose')

if __name__ == '__main__':
    unittest.main()