import unittest


class MyTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

    # def setUp(self):
    #     self.widget = Widget('The widget')
    #
    # def tearDown(self):
    #     self.widget.dispose()

    def test_string(self):
        self.assertEqual('FOO','foo'.upper())


if __name__ == '__main__':
    unittest.main()
