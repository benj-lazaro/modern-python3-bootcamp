# Run test via command-line / terminal: python3 <filename>.py -v

import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    def setUp(self):                                    # Setup Class instance (object) for testing
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()                           # Charge robot's battery to 100
        self.assertEqual(self.mega_man.battery, 100)     # Test if battery level is 100


    def test_say_name(self):
        self.assertEqual(self.mega_man.say_name(), "Beep Boop Beep Boop. I am MEGA MAN") # Check say_name() function
        self.assertEqual(self.mega_man.battery, 49)      # Check battery level after completing previous task



if __name__ == "__main__":
    unittest.main()
