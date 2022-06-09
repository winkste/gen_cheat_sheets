import unittest
import mymodule

# https://docs.python.org/3/library/unittest.html
# execute the unit test module by:
# python -m unittest
# behaviour:
# the class object will be generated new for each test case execution
# use the setUp and TearDown functions to prepare each test case


class TestMyModuleMethods(unittest.TestCase):

# setup function called for each test case
    def setUp(self):
        print("\nTest case preparation...")

    def test_foo_true(self):
        self.assertTrue(mymodule.foo(42))
    
    def test_foo_false(self):
        self.assertFalse(mymodule.foo(43))

    def test_foo_false2(self):
        self.assertEqual(mymodule.foo(43), False)
 
    def test_split(self):
        """
        This text will be displayed during test case execution.
        """
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_even2(self):
        """
        Test that number is even
        """
        self.assertEqual(2 % 2, 0)
    
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
    
    def tearDown(self):
        print("Test Case tear down function...")


if __name__ == '__main__':
    unittest.main()