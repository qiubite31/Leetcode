"""
500. Keyboard Row
Difficulty: Easy
Related Topic: Hash Table

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

American keyboard

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        KEYBOARD_MAP = dict(zip(list("qwertyuiopasdfghjklzxcvbnm"), list("11111111112222222223333333")))
        
        same_row_words = []
        for word in words:
            line_loc = KEYBOARD_MAP[word[0].lower()]
            row_flag = True
            for char in word:
                if not KEYBOARD_MAP[char.lower()] == line_loc:
                    row_flag = False
                    break
            if row_flag:
                same_row_words.append(word)

        return same_row_words
            

words = ["Hello", "Alaska", "Dad", "Peace"]
solution = Solution()
output = solution.findWords(words)

print(output)
