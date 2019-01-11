class Solution(object):
    def countEncoding (self, trie, count):
        if (not trie):
            return count + 1
        else:
            tempCount = 0
            for subTrieKey in trie:
                tempCount += self.countEncoding(trie[subTrieKey],count+1)
            return tempCount
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #build a hashmap tree
        trie = {}
        for word in words:
            tempTrie = trie
            for charIndex in range(len(word)-1,-1,-1):
                if(str(word[charIndex]) in tempTrie):
                    tempTrie = tempTrie[str(word[charIndex])]
                else:
                    tempTrie[str(word[charIndex])] = {}
                    tempTrie=tempTrie[str(word[charIndex])]
        #count the letters and words, using DFS
        return self.countEncoding(trie,0)
sol = Solution()
print(sol.minimumLengthEncoding(["time", "atime", "btime"]))
