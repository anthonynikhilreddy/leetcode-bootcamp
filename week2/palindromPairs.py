#URL: https://leetcode.com/problems/palindrome-pairs/

'''
Approach:
1. We use a dictionary to store the index of the words.
2. We iterate through the words and check if the reverse of the word is present in the dictionary and the index of the reverse word is not the same as the index of the word.
3. If it is, we add the indices to the result.
4. We also check if the word is not empty and if the empty string is present in the dictionary. If it is, we add the indices to the result.
5. We then iterate through the word and check if the word[:j] is a palindrome and the reverse of word[j:] is present in the dictionary. If it is, we add the indices to the result.
6. We also check if the word[j:] is a palindrome and the reverse of word[:j] is present in the dictionary. If it is, we add the indices to the result.
7. We return the result.
'''

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words =  {word:ind for ind,word in enumerate(words)}
        r = []
        for word, i in words.items():
            if word[::-1] in words and words[word[::-1]]!=i:
                r.append([i, words[word[::-1]]])
            if(word!="" and "" in words and word==word[::-1]):
                r.append([words[""], i])
                r.append([i, words[""]])
            # else:
            for j in range(len(word)):
                # print(i, j, "word[j:]", word[j:], "word[:j]", word[:j], "word[j-1::-1]", word[j-1::-1], "word[:j-1:-1]", word[:j-1:-1])
                if word[j:][::-1] in words and word[:j] == word[j-1::-1]:
                    # print("line 15")
                    r.append([words[word[j:][::-1]], i])
                if word[:j][::-1] in words and word[j:] == word[:j-1:-1]:
                    # print("line 18")
                    r.append([i, words[word[:j][::-1]]])
                # print(r)
        return r