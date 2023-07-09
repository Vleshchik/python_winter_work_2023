#1
def triangle(a, b, c):
    if type(a) == int and type(b) == int and type(c) == int:
        if a+b >= c and a+c >= b and b+c >= a:
            return True
    else:
        return False
print(triangle(3,4,5))
print(triangle(10,10,10))
print(triangle(10,10,20))
print(triangle(20,5,5))
print(triangle(1,7,3))
#2
import unittest
class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    def test_concatenation(self):
        self.assertEqual('fuzz'+'dizz', 'fuzzdizz')
    def test_multiply(selfself):
        self.assertEqual('fuzz'*3, 'fuzzfuzzfuzz')
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__== '__main__':
    unittest.main
#3
