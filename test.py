import unittest
import coverage

# Bắt đầu tích hợp với coverage.py
cov = coverage.Coverage()
cov.start()

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
        self.assertEqual(trim_whitespace("  "), "")

    def test_reverse_string_coverage(self):
        self.assertEqual(reverse_string("Hello, world!"), "!dlrow ,olleH")
        self.assertEqual(reverse_string("   Meat   "), "   taeM   ")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_trim_whitespace_coverage(self):
        self.assertEqual(trim_whitespace("   Welcome to UET   "), "Welcome to UET")
        self.assertEqual(trim_whitespace("  NoTrimming "), "NoTrimming")
        self.assertEqual(trim_whitespace("  "), "")

    def test_reverse_string_empty(self):
        # Kiểm tra trường hợp chuỗi rỗng
        self.assertEqual(reverse_string(""), "")

    def test_trim_whitespace_no_whitespace(self):
        # Kiểm tra trường hợp không có khoảng trắng để trim
        self.assertEqual(trim_whitespace("NoWhitespace"), "NoWhitespace")

# Dừng tích hợp với coverage.py và tạo báo cáo
cov.stop()
cov.save()
cov.report()

if __name__ == '__main__':
    unittest.main()
