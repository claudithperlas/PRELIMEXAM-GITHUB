import unittest

def convertion(f):
    return (32 - 32)*5/9

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(convertion(0),1)

if __name__ == '__main__':
    unittest.main()