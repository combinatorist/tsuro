import unittest
import tsuro as ts

canonical_result = [
    ((0, 1), (2, 3), (4, 5), (6, 7)),
    ((0, 1), (2, 3), (4, 6), (5, 7)),
    ((0, 1), (2, 3), (4, 7), (5, 6)),
    ((0, 1), (2, 4), (3, 6), (5, 7)),
    ((0, 1), (2, 4), (3, 7), (5, 6)),
    ((0, 1), (2, 5), (3, 6), (4, 7)),
    ((0, 1), (2, 5), (3, 7), (4, 6)),
    ((0, 1), (2, 6), (3, 4), (5, 7)),
    ((0, 1), (2, 6), (3, 5), (4, 7)),
    ((0, 1), (2, 6), (3, 7), (4, 5)),
    ((0, 1), (2, 7), (3, 4), (5, 6)),
    ((0, 1), (2, 7), (3, 5), (4, 6)),
    ((0, 1), (2, 7), (3, 6), (4, 5)),
    ((0, 2), (1, 3), (4, 6), (5, 7)),
    ((0, 2), (1, 3), (4, 7), (5, 6)),
    ((0, 2), (1, 4), (3, 6), (5, 7)),
    ((0, 2), (1, 4), (3, 7), (5, 6)),
    ((0, 2), (1, 5), (3, 6), (4, 7)),
    ((0, 2), (1, 5), (3, 7), (4, 6)),
    ((0, 2), (1, 6), (3, 4), (5, 7)),
    ((0, 2), (1, 6), (3, 5), (4, 7)),
    ((0, 2), (1, 7), (3, 4), (5, 6)),
    ((0, 2), (1, 7), (3, 5), (4, 6)),
    ((0, 3), (1, 2), (4, 7), (5, 6)),
    ((0, 3), (1, 4), (2, 6), (5, 7)),
    ((0, 3), (1, 4), (2, 7), (5, 6)),
    ((0, 3), (1, 5), (2, 6), (4, 7)),
    ((0, 3), (1, 6), (2, 5), (4, 7)),
    ((0, 4), (1, 2), (3, 6), (5, 7)),
    ((0, 4), (1, 2), (3, 7), (5, 6)),
    ((0, 4), (1, 3), (2, 6), (5, 7)),
    ((0, 4), (1, 5), (2, 6), (3, 7)),
    ((0, 4), (1, 5), (2, 7), (3, 6)),
    ((0, 5), (1, 4), (2, 7), (3, 6)),
    ((0, 7), (1, 2), (3, 4), (5, 6))]

class TsuroTests(unittest.TestCase):
    def test001_canonical_results(self):
        self.assertEqual(
            canonical_result,
            ts.main()
        )

if __name__ == '__main__':
        unittest.main()
