import unittest

class StringReverser:
    def reverse(self, string):
        return string[::-1]

class TestStringReverser(unittest.TestCase):
    def test_reverse(self):
        reverser = StringReverser()
        self.assertEqual(reverser.reverse("hello"), "olleh")
        self.assertEqual(reverser.reverse("12345"), "54321")
        self.assertEqual(reverser.reverse(""), "")

if __name__ == '__main__':
    unittest.main()