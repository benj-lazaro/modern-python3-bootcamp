# NOTE: Run the code using Python interpreter via command-line or terminal:
# python <filename>.py -v

import unittest
from activities import eat, nap, is_funny, laugh


class ActivityTests(unittest.TestCase):
    # Define test case below
    def test_eat_healthy(self):
        """Eat should have a positive message for healthy eating."""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because my body is a temple"
        )

    def test_eat_unhealthy(self):
        """Eat should indicate you've given up for eating unhealthy."""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO!"
        )

    # Test for error / raise error
    def test_eat_healhy_boolean(self):
        """is_healthy MUST be a boolean value."""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")

    def test_short_nap(self):
        """Short naps should be refreshing."""
        self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap.")

    def test_long_nap(self):
        """Long naps should be discouraged."""
        self.assertEqual(nap(3), "Ugh I overslept. I didn't mean to nap 3 hours.")

    def test_is_funny_tim(self):
        """Tim ain't funny."""
        self.assertEqual(is_funny("tim"), False)  # Checks for a False value
        # self.assertFalse(is_funny("tim"), "Tim shouldn't be funny") # Check for falsey value (including False)

    def test_is_funny_anyone_else(self):
        """Anyone else but Tim should be funny."""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

    def test_laugh(self):
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))


if __name__ == "__main__":  # Runs the written test case(s)
    unittest.main()
