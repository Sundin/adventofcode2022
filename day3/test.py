import unittest
import day3

class Tests(unittest.TestCase):

    def test_prio(self):
        self.assertEqual(day3.get_priority("a"), 1)
        self.assertEqual(day3.get_priority("z"), 26)
        self.assertEqual(day3.get_priority("A"), 27)
        self.assertEqual(day3.get_priority("Z"), 52)

    def test_letter(self):
        self.assertEqual(day3.find_letter("vJrwpWtwJgWrhcsFMMfFFhFp"), "p")
        self.assertEqual(day3.find_letter("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"), "L")
        self.assertEqual(day3.find_letter("PmmdzqPrVvPwwTWBwg"), "P")
        self.assertEqual(day3.find_letter("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"), "v")
        self.assertEqual(day3.find_letter("ttgJtRGJQctTZtZT"), "t")
        self.assertEqual(day3.find_letter("CrZsJsPPZsGzwwsLwLmpwMDw"), "s")

    def test_solve(self):
        self.assertEqual(day3.solve("vJrwpWtwJgWrhcsFMMfFFhFp"), 16)
        self.assertEqual(day3.solve("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"), 38)
        self.assertEqual(day3.solve("PmmdzqPrVvPwwTWBwg"), 42)
        self.assertEqual(day3.solve("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"), 22)
        self.assertEqual(day3.solve("ttgJtRGJQctTZtZT"), 20)
        self.assertEqual(day3.solve("CrZsJsPPZsGzwwsLwLmpwMDw"), 19)

    def test_solve_all(self):
        self.assertEqual(day3.solve_input_file("test.txt"), 157)

    def test_find_badge(self):
        self.assertEqual(day3.find_badge("vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"), "r")
        self.assertEqual(day3.find_badge("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"), "Z")

    def test_sum_badges(self):
        self.assertEqual(day3.sum_badges("test.txt"), 70)
        

if __name__ == '__main__':
    unittest.main()