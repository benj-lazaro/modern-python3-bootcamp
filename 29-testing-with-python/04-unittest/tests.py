# Unit Testing - test smallest parts of an application in isolation (e.g. units)
# Good candidates -> invidiaul classes, modules or functions
# Bad candidates -> entire application, dependencies across several classes or modules

# unittest - popular built-in testing framework/module
# Write unit tests encapsulated as classes that inherits from unittest.TestCase
# Inheritance provide access to assertion helpers -> test the behavior of your functions
# Run the test by calling unittest.main()

# NOTE: Run the code using Python interpreter via command-line or terminal:
# python <filename>.py -v

import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
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


    def test_short_nap(self):
        """Short naps should be refreshing."""
        self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap.")


    def test_long_nap(self):
        """Long naps should be discouraged."""
        self.assertEqual(nap(3), "Ugh I overslept. I didn't mean to nap 3 hours.")


if __name__ == "__main__":
    unittest.main()
