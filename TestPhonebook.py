import unittest

from phonebook import PhoneBook


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "1235")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("1235", number)  # add assertion here

    def test_with_exception(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    #@unittest.skip("WIP")
    def test_empty_phonebook_consistency(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Sue","0123")
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_not_consistent_with_same_entries(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Sue","12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_is_not_consistent_with_same_prefix_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_add_phonebook_numbers_and_names(self):
        self.phonebook.add("Sue","123")
        self.assertIn(self.phonebook.get_names("Sue"))
        self.assertIn(self.phonebook.get_numbers("123"))






if __name__ == '__main__':
    unittest.main()
