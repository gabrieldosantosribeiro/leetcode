'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

# solutoin
def reverseVowels(self, s):

    s = list(s)
    x, y = 0, len(s)-1
    vowels = 'AEIOUaeiou'
    response = ''
    
    while x < y:
        if s[x] in vowels:
            while s[y] not in vowels:
                y -= 1
            if x < y:
                support = s[x]
                s[x] = s[y]
                s[y] = support
                y -= 1
        x += 1

    for i in range(len(s)):
        response += s[i]

    return response