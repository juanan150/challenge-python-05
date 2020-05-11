import math


def square_area(side):
    """Returns the area of a square"""
    return side**2


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return base*height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return base*height/2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return diagonal_1*diagonal_2/2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return ((base_major+base_minor)/2)*height


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return (perimeter*apothem)/2


def circumference_area(radius):
    """Returns the area of a circumference"""
    return(round(math.pi*radius**2,3))


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.areas={'square':[16,4],
                        'rectangle':[30,6,5],
                        'triangle':[7.5,5,3],
                        'rhombus':[25,5,10],
                        'trapezoid':[8,3,5,2],
                        'polygon':[168,48,7],
                        'circumference':[12.566,2]
                        }

        def test_square_area(self):
            self.assertEqual(self.areas['square'][0],square_area(self.areas['square'][1]))

        def test_rectangle_area(self):
            self.assertEqual(self.areas['rectangle'][0],rectangle_area(self.areas['rectangle'][1],self.areas['rectangle'][2]))

        def test_triangle_area(self):
            self.assertEqual(self.areas['triangle'][0],triangle_area(self.areas['triangle'][1],self.areas['triangle'][2]))

        def test_rhombus_area(self):
            self.assertEqual(self.areas['rhombus'][0],rhombus_area(self.areas['rhombus'][1],self.areas['rhombus'][2]))

        def test_trapezoid_area(self):
            self.assertEqual(self.areas['trapezoid'][0],trapezoid_area(self.areas['trapezoid'][1],self.areas['trapezoid'][2],self.areas['trapezoid'][3]))

        def test_regular_polygon_area(self):
            self.assertEqual(self.areas['polygon'][0],regular_polygon_area(self.areas['polygon'][1],self.areas['polygon'][2]))

        def test_circumference_area(self):
            self.assertEqual(self.areas['circumference'][0],circumference_area(self.areas['circumference'][1]))

        def tearDown(self):
            del(self.areas)
            pass

    unittest.main()
