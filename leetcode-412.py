"""
412. Fizz Buzz
Difficulty: Easy
Related Topic: 

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output_ans = []
        output_str = ''
        for num in range(1, n+1):
            if num % 3 == 0:
                output_str += 'Fizz'
            if num % 5 == 0:
                output_str += 'Buzz'
            if output_str == '':
                output_str += str(num)
            output_ans.append(output_str)
            output_str = ''

        return output_ans


n = 15
solution = Solution()
output = solution.fizzBuzz(n)

print(output)
