import unittest

def reverse_string(input_string):
    return input_string[::-1]

def trim_whitespace(input_string):
    return input_string.strip()


class TestStringFunctions(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("Hello, world!"), "!dlrow ,olleH")
        self.assertEqual(reverse_string("   Meat   "), "   taeM   ")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_trim_whitespace(self):
        self.assertEqual(trim_whitespace("   Welcome to UET   "), "Welcome to UET")
        self.assertEqual(trim_whitespace("  NoTrimming "), "NoTrimming")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(trim_whitespace("  "), "")

if __name__ == '__main__':
    unittest.main()
