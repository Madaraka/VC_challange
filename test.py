import unittest
import find_operator


class TestCode(unittest.TestCase):
    def test_example_1(self):
        """
        Test that the example in the assignment is correct
        """
        operators = [{"extension": [1, 268, 46, 4620, 468, 4631, 4673, 46732],
                      "A": [0.9, 5.1, 0.17, 0.0, 0.15, 0.15, 0.9, 1.1]},
                     {"extension": [1, 44, 46, 467, 48],
                      "B": [0.92, 0.5, 0.2, 1.0, 1.2]}]
        phone_nr = 4673212345
        self.assertEqual(find_operator.main(phone_nr, operators), (467, 1.0, 'B'))

    def test_example_2(self):
        """
        Test that the example in the assignment is correct,
        without viable operator
        """
        operators = [{"extension": [1, 268, 46, 4620, 468, 4631, 4673, 46732],
                      "A": [0.9, 5.1, 0.17, 0.0, 0.15, 0.15, 0.9, 1.1]},
                     {"extension": [1, 44, 46, 467, 48],
                      "B": [0.92, 0.5, 0.2, 1.0, 1.2]}]
        phone_nr = 68123456789
        self.assertEqual(find_operator.main(phone_nr, operators), "No operators available for this extension")

    def test_more_operators(self):
        """
        Test adding on more operators
        """
        operators = [{"extension": [1, 268, 46, 4620, 468, 4631, 4673, 46732],
                      "A": [0.9, 5.1, 0.17, 0.0, 0.15, 0.15, 0.9, 1.1]},
                     {"extension": [1, 44, 46, 467, 48],
                      "B": [0.92, 0.5, 0.2, 1.0, 1.2]},
                     {"extension": [1, 44, 68, 467, 48],
                      "C": [0.92, 0.5, 0.3, 1.0, 1.2]},
                     {"extension": [1, 44, 46, 467, 681],
                      "D": [0.92, 0.5, 0.2, 1.0, 0.9]}
                     ]
        phone_nr = 68123456789
        self.assertEqual(find_operator.main(phone_nr, operators), (68, 0.3, 'C'))


if __name__ == '__main__':
    unittest.main()

