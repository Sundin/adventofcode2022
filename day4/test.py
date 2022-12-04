import unittest
import code

class Tests(unittest.TestCase):

    def test_is_fully_covered(self):
        self.assertEqual(code.is_fully_covered("2-4,6-8"), False)
        self.assertEqual(code.is_fully_covered("2-3,4-5"), False)
        self.assertEqual(code.is_fully_covered("5-7,7-9"), False)
        self.assertEqual(code.is_fully_covered("2-8,3-7"), True)
        self.assertEqual(code.is_fully_covered("6-6,4-6"), True)
        self.assertEqual(code.is_fully_covered("2-6,4-8"), False)

    def test_solve_input_file(self):
        self.assertEqual(code.solve_input_file("test.txt"), 2)

    def test_overlap(self):
        self.assertEqual(code.overlap("2-4,6-8"), False)
        self.assertEqual(code.overlap("2-3,4-5"), False)
        self.assertEqual(code.overlap("5-7,7-9"), True)
        self.assertEqual(code.overlap("2-8,3-7"), True)
        self.assertEqual(code.overlap("6-6,4-6"), True)
        self.assertEqual(code.overlap("2-6,4-8"), True)

    def test_part_2(self):
        self.assertEqual(code.part2("test.txt"), 4)

if __name__ == '__main__':
    unittest.main()