"""
804. Unique Morse Code Words
Difficulty: Easy
Related Topic: Hash Table

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
 

Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0

        MORSE_WORDS = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        MORSE_WORD_MAP = dict(zip(list("abcdefghijklmnopqrstuvwxyz"), MORSE_WORDS))

        morse_word_cnt = dict()

        for word in words:
            morse_word = ''
            for char in word:
                morse_word += MORSE_WORD_MAP[char]

            morse_word_cnt[morse_word] = morse_word_cnt.setdefault(morse_word, 0) + 1

        return len(morse_word_cnt.keys())

words = ["rwjje", "aittjje", "auyyn", "lqtktn", "lmjwn"]
solution = Solution()
output = solution.uniqueMorseRepresentations(words)

print(output)
