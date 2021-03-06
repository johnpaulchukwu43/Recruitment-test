from unittest import TestCase


def fizzbuzz_val(val):
    answer = ''
    if val % 3 == 0:
        answer += 'Fizz'
    if val % 5 == 0:
        answer += 'Buzz'

    if val % 3 == 0 and val % 5 == 0:
        answer = 'FizzBuzz'
    return answer


class FizzBuzzTestCase(TestCase):
    def test_multiples_of_3_and_5(self):
        self.assertEqual(fizzbuzz_val(15), 'FizzBuzz')

    def test_multiples_of_3_alone(self):
        self.assertTrue(fizzbuzz_val(3) is 'Fizz')
        self.assertTrue(fizzbuzz_val(99) is 'Fizz')
        self.assertFalse(fizzbuzz_val(15) is 'Fizz')
        self.assertFalse(fizzbuzz_val(8) is 'Fizz')

    def test_multiples_of_5_alone(self):
        self.assertTrue(fizzbuzz_val(5) is 'Buzz')
        self.assertTrue(fizzbuzz_val(10) is 'Buzz')
        self.assertTrue(fizzbuzz_val(20) is 'Buzz')
        self.assertFalse(fizzbuzz_val(8) is 'Buzz')

