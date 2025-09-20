#User function Template for python3

class Solution:
    def characterReplacement(self, s, k):
        # Code here\\
        
        dict = {}
        
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
                

        maxSub = 0        
        for char in dict:
            i = 0
            mis = 0
            for j in range(len(s)):
                if s[j] != char:
                   mis += 1
                if mis > k:
                    while s[i] == char:
                        i += 1
                    i+=1
                    mis -= 1
                maxSub = max(maxSub, j-i+1)
            # print(char)
            # print(j)
            # print(i)
        
        return maxSub
                
                    