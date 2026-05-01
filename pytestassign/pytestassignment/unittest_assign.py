import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 3, 5)

class TestList(unittest.TestCase):
    def setUp(self):
        self.sample_list = [1, 2, 3]
    def tearDown(self):
        print("Test completed")
    def test_list_length(self):
        self.assertEqual(len(self.sample_list), 3)

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")
    def test_isupper(self):
        self.assertFalse("hello".isupper())

class TestExceptions(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0

class TestAdd(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(5 + 5, 10)

class TestSubtract(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(10 - 5, 5)

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSubtract))

    runner = unittest.TextTestRunner()
    runner.run(suite)