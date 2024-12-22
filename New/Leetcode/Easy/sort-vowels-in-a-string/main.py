class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        arr = list(s)

        # Extract vowels from the string
        vowel_chars = sorted([char for char in arr if char in vowels])
        print(vowel_chars)

        # Replace vowels in their original positions
        vowel_index = 0
        for i in range(len(arr)):
            if arr[i] in vowels:
                print(arr[i])
                print(vowel_chars[vowel_index])
                arr[i] = vowel_chars[vowel_index]
                vowel_index += 1

        return ''.join(arr)

s = Solution()
print(s.sortVowels("lEetcOde"))