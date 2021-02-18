from unittest import TestCase

from .string_functions import *
class StringTests(TestCase):
    def test_greeting_jeremy(self):
        """Test for greet_by_name"""
        # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

        # Step 2: Decide what the expected outcome is for the scenario
        expected = 'Hello, Jeremy!'

        # Step 3: Call the function being tested to get its actual output
        actual = greet_by_name('Jeremy')

        # Step 4: Compare expected & actual outcomes. If they match, the test 
        # passes
        self.assertEqual(actual, expected)

    def test_greeting_dani(self):
        """Test for greet_by_name"""
        expected = 'Hello, Dani!'
        actual = greet_by_name('Dani')
        self.assertEqual(actual, expected)

    def test_reverse_long(self):
        """Test reversing a long string."""
        expected = '!inaD ,olleH'
        actual = reverse('Hello, Dani!')
        self.assertEqual(actual, expected)

    def test_reverse_short(self):
        """Test reversing a short string."""
        expected = 'olleH'
        actual = reverse('Hello')
        self.assertEqual(actual, expected)

    def test_reverse_words_long(self):
        """Test reversing words in a long string."""
        expected = 'ym eman si'
        actual = reverse_words('my name is')
        self.assertEqual(actual, expected)

    def test_reverse_words_short(self):
        """Test reversing words in a short string."""
        expected = 'olleh'
        actual = reverse_words('hello')
        self.assertEqual(actual, expected)

    def test_sarcastic_long(self):
        """Test sarcastic-ifying a long string."""
        expected = 'HoW aRe YoU'
        actual = sarcastic('how are you')
        self.assertEqual(actual, expected)

    def test_sarcastic_short(self):
        """Test sarcastic-ifying a short string."""
        expected = 'YoU'
        actual = sarcastic('you')
        self.assertEqual(actual, expected)


    def test_find_longest_word_empty(self):
        expected = 'amazing'
        actual = find_longest_word('wow, that was so amazing')
        self.assertEqual(actual, expected)

# run the tests
if __name__ == '__main__':
    unittest.main()