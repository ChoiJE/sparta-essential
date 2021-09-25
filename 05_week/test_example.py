import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.common_value = "FOO"

    def tearDown(self):
        print("tearDown")
        self.common_value = None

    def test_upper(self):
        self.assertEqual('foo'.upper(), self.common_value)

    def test_isupper(self):
        self.assertTrue(self.common_value.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()