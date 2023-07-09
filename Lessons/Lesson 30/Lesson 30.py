import unittest

def cube_area(side):
    if side <= 0: raise ValueError
    if type(side) == bool: raise TypeError
    if not isinstance(side(int, float)): raise TypeError
    return 6*side**2

class TestCubeArea(unittest.TestCase):
    def test_cube_area(self):
        self.assertEqual(cube_area(3), 54)
        #self.assertEqual(cube_area(0), 0)
    def test_value(self):
        self.assertRaises(ValueError, cube_area, 0)
    def test_types(self):
        self.assertRaises(TypeError, cube_area, True)
        self.assertRaises(TypeError, cube_area, [0])
        self.assertRaises(TypeError, cube_area, {})
        self.assertRaises(TypeError, cube_area, (1,2))

if __name__ == '__main__':
    unittest.main()