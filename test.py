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

    def test_whitespace_only_input(self):
        # Kiểm tra khi chuỗi đầu vào chỉ chứa khoảng trắng
        self.assertEqual(trim_whitespace("    "), "")

    def test_special_characters(self):
        # Kiểm tra khi chuỗi đầu vào chứa ký tự đặc biệt (Unicode)
        self.assertEqual(reverse_string("Hello, 🌟 World!"), "!dlroW 🌟 ,olleH")

    def test_mixed_case(self):
        # Kiểm tra khi chuỗi đầu vào chứa cả chữ hoa và chữ thường
        self.assertEqual(trim_whitespace("HeLlO WoRlD"), "HeLlO WoRlD")

    def test_alphanumeric(self):
        # Kiểm tra khi chuỗi đầu vào chứa cả ký tự số và chữ cái
        self.assertEqual(trim_whitespace("123abcXYZ"), "123abcXYZ")

    def test_special_characters_and_whitespace(self):
        # Kiểm tra khi chuỗi đầu vào chứa các ký tự đặc biệt và khoảng trắng
        self.assertEqual(reverse_string("  @#$ Hello, 123 World! 🌟   "), "🌟 !dlroW 321 ,olleH #$@  ")

    def test_large_input(self):
        # Kiểm tra khi chuỗi đầu vào có chiều dài lớn
        input_str = "A" * 10000
        self.assertEqual(reverse_string(input_str), input_str[::-1])

# Dừng tích hợp với coverage.py và tạo báo cáo
cov.stop()
cov.save()
cov.report()

if __name__ == '__main__':
    unittest.main()
