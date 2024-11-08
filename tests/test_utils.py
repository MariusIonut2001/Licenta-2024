import unittest
from backend.utils import image_utils


class ImageUtilsTestCase(unittest.TestCase):
    def test_allowed_file(self):
        self.assertTrue(image_utils.allowed_file('test.jpg'))
        self.assertFalse(image_utils.allowed_file('test.txt'))

if __name__ == '__main__':
    unittest.main()
