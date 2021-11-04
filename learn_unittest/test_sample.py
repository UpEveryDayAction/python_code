import unittest
import sample

class Test_Sample(unittest.TestCase):
    def test_do_something(self):
        obj = sample.Sample()
        result = obj.do_something()
        self.assertEqual(result, 'Hello, World!')

if __name__ == "__main__":
    unittest.main()

