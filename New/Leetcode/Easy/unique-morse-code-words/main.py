from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = []
        asc = 97
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for i in words:
            w = ''
            for j in range(len(i)):
                c = morse_code[ord(i[j])-asc]
                w += c
            result.append(w)

        return len(list(set(result)))

        
s = Solution()
print(s.uniqueMorseRepresentations(["gin","zen","gig","msg"]))